# TODO
from cs50 import get_string


def main():
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    grade_calculation(letters, words, sentences)


def count_letters(text):
    letters = 0
    for c in text:
        if "a" <= c <= "z" or "A" <= c <= "Z":
            letters += 1
    return letters


def count_words(text):
    words = 0
    for word in text.split():
        words += 1
    return words


def count_sentences(text):
    sentences = 0
    for word in text.split():
        if word.endswith(".") or word.endswith("!") or word.endswith("?"):
            sentences += 1
    return sentences


def grade_calculation(letters, words, sentences):
    grade = round(
        0.0588 * ((letters / words) * 100) - 0.296 * ((sentences / words) * 100) - 15.8
    )
    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print("Grade", grade)


main()
