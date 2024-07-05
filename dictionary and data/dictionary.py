import json
import difflib

# Load JSON data into a Python dictionary
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        dictionary = json.load(file)
    return dictionary

# Function to suggest correct words
def suggest_word(word, dictionary):
    word = word.lower()  # Normalize the word to lowercase
    suggestions = difflib.get_close_matches(word, dictionary.keys(), n=1)
    if suggestions:
        return f"Did you mean '{suggestions[0]}'?"
    else:
        return "No suggestions available."

# Function to get the definition of a word
def get_definition(word, dictionary):
    word = word.lower()  # Normalize the word to lowercase
    if word in dictionary:
        return dictionary[word]
    else:
        suggestion = suggest_word(word, dictionary)
        return f"The word is not in the dictionary. {suggestion}"

# Main function to handle user input
def main():
    file_path = r'dictionary.json'
    dictionary = load_dictionary(file_path)
    
    while True:
        print("Menu:")
        print("1. Search for a word")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == '2':
            print("Exiting the dictionary program. Goodbye!")
            break
        elif choice == '1':
            word = input("Enter a word: ")
            definition = get_definition(word, dictionary)
            print(definition)
            
            # Ask if the user wants to search for another word
            continue_search = input("Do you want to search for another word? (yes/no): ").strip().lower()
            if continue_search != 'yes':
                print("Exiting the dictionary program. Goodbye!")
                break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
