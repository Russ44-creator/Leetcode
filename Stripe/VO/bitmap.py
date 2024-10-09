# Bitmap lookup table
WIDTH = 6
HEIGHT = 10
LETTERS = {
    "J": [
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ],
    "H": [
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
    ],
    "E": [
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
    ],
    "L": [
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
    ],
    "O": [
        [0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 0],
    ],
}


# Phase one: Given some bitmap lookup table, print out some letters in bitmap format.
# This is an example bitmap of the letter "J"
# 0 0 0 0 1 0
# 0 0 0 0 1 0
# 0 0 0 0 1 0
# 0 0 0 0 1 0
# 0 0 0 0 1 0
# 0 0 0 0 1 0
# 1 0 0 0 1 0
# 0 1 1 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0


def print_letter(letter):
    if letter not in LETTERS:
        print(f"Letter '{letter}' not found in the lookup table.")
        return

    bitmap = LETTERS[letter]
    for row in bitmap:
        print("".join("#" if pixel else " " for pixel in row))


print("Phase 1 - Original 'J':\n")

print_letter("J")

# Phase two: compression and decompression on the lookup table,
# print out the same letters


def compress(bitmap):
    return [[i for i, bit in enumerate(row) if bit == 1] for row in bitmap]


def decompress(compressed, width=6):
    return [[1 if i in row else 0 for i in range(width)] for row in compressed]


def print_letter_compressed(letter, use_compression=False):
    if letter not in LETTERS:
        print(f"Letter '{letter}' not found in the lookup table.")
        return

    bitmap = LETTERS[letter]
    if use_compression:
        bitmap = compress(bitmap)
        bitmap = decompress(bitmap)

    for row in bitmap:
        print("".join("#" if pixel else " " for pixel in row))


# Compress all letters in the lookup table
COMPRESSED_LETTERS = {letter: compress(bitmap) for letter, bitmap in LETTERS.items()}

print("\nPhase 2 - Compressed and then decompressed 'J':\n")
print_letter_compressed("J", use_compression=True)
print("Compressed representation of 'J':")
print(COMPRESSED_LETTERS["J"])


# Phase three: some additional manipulation on the lookup table, print out the word and sentence.
# 起手就给了你写好的map，让你打印字。然后让你打印一句话，每行有长度限制，超长的话要分行。
# This should reuse part of phase two code.
def print_word(word):
    if not word:
        return

    lines = [""] * HEIGHT

    for letter in word:
        if letter == " ":
            for i in range(HEIGHT):
                lines[i] += " " * WIDTH
        elif letter not in LETTERS:
            print(f"Letter '{letter}' not found in the lookup table.")
            continue
        else:
            bitmap = LETTERS[letter]
            for i, row in enumerate(bitmap):
                lines[i] += "".join("#" if pixel else " " for pixel in row)

    for line in lines:
        print(line)


def print_sentence(sentence, max_width):
    words = sentence.split()
    current_line = []
    current_width = 0

    for word in words:
        word_width = WIDTH * len(word)

        if current_width + word_width + (WIDTH if current_line else 0) <= max_width:
            current_line.append(word)
            current_width += word_width + (
                WIDTH if current_width > 0 else 0
            )  # Add 6 for space between words
        else:
            print_word(" ".join(current_line))
            print()  # Print a blank line between rows of text
            current_line = [word]
            current_width = word_width

    if current_line:
        print_word(" ".join(current_line))


print("\nPhase 3 - Printing a word and a sentence:\n")
print("Printing a word:")
print_word("HELLO")
print("\n")

print("Printing a sentence with line breaks (max width: 40):")
print_sentence("HELLO OLLEH HELLO HELLO HELLO", 66)
