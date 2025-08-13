# File Read & Write with Error Handling

try:
    # Ask user for the filename to read
    filename = input("Enter the filename to read: ")
    
    # Open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (make it uppercase for example)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("modified_" + filename, "w") as new_file:
        new_file.write(modified_content)

    print("File has been read and modified successfully!")

except FileNotFoundError:
    print("❌ The file does not exist.")
except IOError:
    print("⚠️ An error occurred while reading or writing the file.")
