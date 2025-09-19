# Streamlit App: CORD-19 Data Explorer (Auto Detect Publish Date)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

sns.set(style="whitegrid")

st.title("CORD-19 Data Explorer")
st.write("Upload a CSV file of COVID-19 research papers metadata and explore it interactively.")

# File Uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8", on_bad_lines="skip")
        st.success("CSV loaded successfully!")
    except pd.errors.ParserError:
        st.error("CSV parsing error! Please check the file format.")
        st.stop()

    # Clean column names
    df.columns = df.columns.str.strip()  # remove spaces
    st.write("Columns detected:", df.columns.tolist())

    # Detect publish date column
    possible_date_cols = [c for c in df.columns if "date" in c.lower() or "publish" in c.lower()]
    if not possible_date_cols:
        st.error("No publish date column detected. Please check your CSV.")
        st.stop()
    publish_col = possible_date_cols[0]  # take the first match
    st.write(f"Using '{publish_col}' as the publish date column.")

    # Data Cleaning & Preparation
    df = df.dropna(subset=[publish_col])
    df[publish_col] = pd.to_datetime(df[publish_col], errors="coerce")
    df["year"] = df[publish_col].dt.year
    if "abstract" in df.columns:
        df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))
    else:
        df["abstract_word_count"] = 0  # default if abstract column missing

    # Sidebar Widgets
    # -----------------------------
    st.sidebar.header("Filter Options")
    min_year = int(df["year"].min())
    max_year = int(df["year"].max())

    year_range = st.sidebar.slider("Select publication year range", min_year, max_year, (min_year, max_year))
    filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

    top_n = st.sidebar.selectbox("Number of top journals to display", [5, 10, 15, 20], index=1)

    # -----------------------------
    # Visualization 1: Publications Over Time
    st.subheader("Publications Over Time")
    year_counts = filtered_df["year"].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.bar(year_counts.index, year_counts.values, color="skyblue")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Papers")
    st.pyplot(fig)

    # Visualization 2: Top Journals
    if "journal" in df.columns:
        st.subheader(f"Top {top_n} Journals Publishing COVID-19 Research")
        top_journals = filtered_df["journal"].value_counts().head(top_n)
        fig2, ax2 = plt.subplots()
        sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2)
        ax2.set_xlabel("Number of Papers")
        ax2.set_ylabel("Journal")
        st.pyplot(fig2)

    # Visualization 3: Top Words in Titles
    if "title" in df.columns:
        st.subheader("Top Words in Paper Titles")
        titles = filtered_df["title"].dropna().str.lower()
        words = Counter()
        for title in titles:
            words.update(re.findall(r'\b\w+\b', title))
        top_words = words.most_common(20)
        words_df = pd.DataFrame(top_words, columns=["word", "count"])
        fig3, ax3 = plt.subplots()
        sns.barplot(x="count", y="word", data=words_df, ax=ax3)
        ax3.set_xlabel("Count")
        ax3.set_ylabel("Word")
        st.pyplot(fig3)

    # Display Sample of Data
    st.subheader("Sample of the Data")
    st.dataframe(filtered_df.head())

    # Summary Stats
    st.subheader("Summary")
    st.write("Total papers in selection:", len(filtered_df))
    st.write("Year range:", year_range)
    st.write("Average abstract word count:", int(filtered_df["abstract_word_count"].mean()))

else:
    st.info("Please upload a CSV file to get started.")
