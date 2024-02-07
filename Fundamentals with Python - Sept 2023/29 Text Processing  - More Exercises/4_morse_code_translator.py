def morse_to_english(morse_code):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..'
    }

    morse_words = morse_code.split(' | ')
    english_words = []

    for morse_word in morse_words:
        morse_chars = morse_word.split(' ')
        english_word = ''

        for morse_char in morse_chars:
            for key, value in morse_dict.items():
                if value == morse_char:
                    english_word += key

        english_words.append(english_word)

    return ' '.join(english_words)

# Get user input for Morse code
morse_code = input()

# Translate Morse code to English and print the result
english_message = morse_to_english(morse_code)
print(english_message)
