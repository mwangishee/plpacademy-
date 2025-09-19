
# Iris Dataset Analysis (Tasks 1 - 3)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# ✅ Task 1: Load and Explore

try:
    # Load iris dataset
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    # Add target column with species names
    df["species"] = iris.target
    df["species"] = df["species"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
    print("Dataset loaded successfully!\n")

except FileNotFoundError:
    print("Error: Dataset not found!")

# Display the first few rows
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Clean dataset (drop rows with missing values if any)
df = df.dropna()

# ✅ Task 2: Basic Data Analysis

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Group by species and compute mean
print("\nAverage values per species:")
print(df.groupby("species").mean())

# Observations
print("\nObservations:")
print("- Setosa tends to have the smallest petal length and width.")
print("- Virginica has the largest measurements overall.")
print("- Versicolor lies between Setosa and Virginica in most features.")

# ✅ Task 3: Data Visualization

# 1. Line chart (trend of sepal vs petal length across samples)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Line Chart: Sepal vs Petal Length across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(6,4))
sns.barplot(x="species", y="petal length (cm)", data=df, estimator="mean")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(6,4))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length, colored by species)
plt.figure(figsize=(6,4))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)",
                hue="species", data=df)
plt.title("Scatter Plot: Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
