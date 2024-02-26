import sys


def loadWords():
    return open("words.txt", "r", encoding="utf-8").read().split("\n")

def generiere_pattern(words):
    if not words:
        return "no words given"

    word_length = len(words[0])

    patterns = ['' for _ in range(word_length)]

    index = 0

    for i in range(word_length):
        unique_chars = set(word[i] for word in words)

        if len(unique_chars) == 1:
            char = unique_chars.pop()
            patterns[i] = f'{char}'
        else:
            patterns[i] = f'x{index}'
            index += 1

    return ''.join(patterns)

if __name__ == "__main__":
    words = loadWords()
    print(f"words: {words}")

    word_length = len(words[0])
    if any(len(w) != word_length for w in words[1:]):
        print("Word length isn't correct.")
        sys.exit(-1)

    predictedPattern = generiere_pattern(words)
    print(f"possible pattern: {predictedPattern}")


