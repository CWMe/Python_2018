from bs4 import BeautifulSoup
from operator import itemgetter

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
                if word is not None and word not in common_words and dictionary.get(word) is None:
                    dictionary[word] = 1
                elif word is not None and word not in common_words and dictionary.get(word) is not None:
                    dictionary[word]+= 1


    #sort
    sorted_x = sorted(dictionary.items(), key = itemgetter(1), reverse = True)


    #output
    print(f"{sorted_x[0]} is 1st most common")
    print(f"{sorted_x[1]} is 2nd most common")
    print(f"{sorted_x[2]} is 3rd most common")
    print(f"{sorted_x[3]} is 4th most common")
    print(f"{sorted_x[4]} is 5th most common")

main()