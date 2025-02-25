def remove_duplicates(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            unique_lines = set(infile.readlines())

        with open(output_file, 'w') as outfile:
            outfile.writelines(sorted(unique_lines))

        print(f"Duplicate removal complete. Output written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = "matches.txt"
output_file = "output_files"

remove_duplicates(input_file, output_file)
