def find_duplicates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    unique_lines = set()
    duplicates = []
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line in unique_lines:
            duplicates.append(cleaned_line)
        else:
            unique_lines.add(cleaned_line)
    return duplicates
file_path = 'link.txt'
duplicate_lines = find_duplicates(file_path)

if duplicate_lines:
    print("Duplicates found:")
    for line in duplicate_lines:
        print(line)
else:
    print("No duplicates found.")
