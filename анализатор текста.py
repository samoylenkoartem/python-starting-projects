import string
def analyze_text(text):
    text = text.lower()
    for i in string.punctuation:
        text = text.replace(i, ' ')
    

    words = text.split()
    word_count = len(words)
    unigue_words = len(set(words))
    longest_word = max(words, key=len)
    char_count = len(''.join(words))
    reversed_text = ' '.join(words[::-1])
    return {
        'word_count' : word_count,
        'unigue_words' : unigue_words,
        'longest_word' : longest_word,
        'char_count' : char_count,
        'reversed_text' : reversed_text
    }
print(analyze_text("hello world hello python"))
