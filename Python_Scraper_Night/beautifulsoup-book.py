from bs4 import BeautifulSoup
import collections

def main():
    #open file
    with open("book.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")

    #setup
    # common_words = []
    common_words = ["the", "her", "she", "his", "he", "is",
        "as", "be", "of", "a", "and", "to", "in", "was", "but", 
        "that", "it", "i", "had", "you", "at", "for", "have"]
    dictionary = {}

    #build dictionary
    for child in soup.find(id="book").children:
        if child.name == "p" and child.string:
            words = child.string.split()
            for word in words:
                word = word.lower().strip('?:!.,;')
                if word is not None and word not in common_words:
                    if dictionary.get(word) is None:
                        dictionary[word] = 1
                    else:
                        dictionary[word]+= 1

    #sort
    word_counter = collections.Counter(dictionary)
    for word, count in word_counter.most_common(5):
        print(word, ":\t", count)

main()