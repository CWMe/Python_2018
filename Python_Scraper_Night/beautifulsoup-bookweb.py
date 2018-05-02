from bs4 import BeautifulSoup
import collections
import urllib.request
import certifi

def main():
    html = urllib.request.urlopen('https://www.gutenberg.org/files/161/161-h/161-h.htm',cafile=certifi.where()).read()
    soup = BeautifulSoup(html, "html.parser")

    #setup
    # common_words = []
    common_words = ["the", "her", "she", "his", "he", "is",
        "as", "be", "of", "a", "and", "to", "in", "was", "but", 
        "that", "it", "i", "had", "you", "at", "for", "have"]
    dictionary = {}
    target = soup.findAll(['h3','p'])

    #build dictionary
    for child in target:
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