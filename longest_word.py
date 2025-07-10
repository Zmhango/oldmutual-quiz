import string

def find_longest_words(text):

    for char in string.punctuation:
        text = text.replace(char, "")
    
    words = text.split()

    if not words:
        return [], 0

    max_length = max(len(word) for word in words)

    longest_words = [word for word in words if len(word) == max_length]

    return longest_words, max_length

def main():
    text = input("Enter text: ").strip()

    if not text:
        print("No input provided.")
        return

    longest_words, length = find_longest_words(text)

    print(f"Longest word(s): {', '.join(longest_words)} ({length} characters)")

if __name__ == "__main__":
    main()
