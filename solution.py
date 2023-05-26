import sys
import re

# This function will return the search term
# As per now given requirements we just send it the line and will get back it
#though at this point we are sure its only contains one word but still to add some functionality
# we will bw returning first word
def get_search_term(line):
    search_term = line.strip()
    return search_term

#clean the input to remove numbers and special characters
def clean_input(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s_]', '', text)
    cleaned_text = re.sub(r'_', ' ', cleaned_text)
    return cleaned_text.strip()




def search_matches(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            search_term = lines[-1].strip()
            matches = []

            for line in lines[:-1]:
                cleaned_line = clean_input(line)

                words = cleaned_line.split()
                if any(search_term in word for word in words):
                    matches.append(words)

            for match in matches:
                print('[{}]'.format(' '.join(match)))

    except IOError:
        print("Error: Could not read the file.")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python solution.py <file_path>")
    else:
        file_path = sys.argv[1]
        search_matches(file_path)
