# Dictionary Search Program

This Python program allows users to search for the definition of words in a dictionary stored in a JSON file. It provides suggestions for misspelled words and offers a menu-driven interface for user interaction.

## Features

- Load dictionary data from a JSON file
- Search for word definitions
- Suggest correct words if the entered word is not found in the dictionary
- Menu-driven interface for user interaction

## Requirements

- Python 3.x
- `json` module (standard library)
- `difflib` module (standard library)

## Usage

1. Clone this repository to your local machine:
git clone https://github.com/your-username/dictionary-search.git

2. Navigate to the project directory:
cd dictionary-search

3. Ensure your dictionary JSON file is located at dictionary.json` or update the `file_path` variable in the `main` function with the correct path to your dictionary JSON file.

4. Run the program:

## Program Flow

1. The program displays a menu with options to search for a word or exit.
2. If the user chooses to search for a word, they are prompted to enter a word.
3. The program displays the definition if the word is found in the dictionary.
4. If the word is not found, the program suggests the closest matching word.
5. The user is asked if they want to search for another word or exit.
6. The process repeats until the user chooses to exit.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
