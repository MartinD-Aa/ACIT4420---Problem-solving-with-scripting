import string

def clean_word(word):
    # Remove punctuation and convert to lowercase
    word = word.strip(string.punctuation).lower()
    return word

def main():
    word_count = {}
    
    # Read the file
    with open('python.txt', 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()
            for word in words:
                cleaned_word = clean_word(word)
                if cleaned_word:
                    # Count occurrences of cleaned word
                    word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
    
    # Print words occurring more than 3 times
    for word, count in word_count.items():
        if count > 3:
            print(f'{word}: {count}')

if __name__ == "__main__":
    main()