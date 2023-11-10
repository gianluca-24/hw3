def find_duplicates(file_path):
    # Read the contents of the file into a list
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a set to store unique lines
    unique_lines = set()

    # Create a list to store duplicate lines
    duplicates = []

    # Iterate through each line in the file
    for line in lines:
        # Remove leading and trailing whitespaces
        cleaned_line = line.strip()

        # Check if the line is already in the set
        if cleaned_line in unique_lines:
            # If yes, it's a duplicate
            duplicates.append(cleaned_line)
        else:
            # If not, add it to the set of unique lines
            unique_lines.add(cleaned_line)

    return duplicates

# Example usage
file_path = 'link.txt'
duplicate_lines = find_duplicates(file_path)

if duplicate_lines:
    print("Duplicates found:")
    for line in duplicate_lines:
        print(line)
else:
    print("No duplicates found.")
