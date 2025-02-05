# Word Counter Program

def count_words(text):
    """
    This function takes a string input and returns the word count.
    It splits the text based on spaces and filters out empty strings.
    """
    words = text.split()  # Splitting the input text into words
    return len(words)  # Returning the number of words

def main():
    """
    Main function to take user input and display the word count.
    It also handles empty input cases.
    """
    user_input = input("Enter a sentence or paragraph: ").strip()  # Taking user input and removing extra spaces
    
    if not user_input:  # Checking if input is empty
        print("Error: No text entered. Please enter a valid sentence or paragraph.")
    else:
        word_count = count_words(user_input)  # Calling function to count words
        print(f"Word Count: {word_count}")  # Displaying the word count

# Running the main function
if __name__ == "__main__":
    main()

