import io
import random


def choose_category(categoryList):
    animale = '1'
    film = '2'
    sport = '3'
    print("\nCategoriile de cuvinte sunt:")
    for i in categoryList:
        print(i)
    category = input("\nScrie numarul categoriei dorite ")
    while 1:
        if category == animale or category == film or category == sport:
            return int(category)
        else:
            print("Caracterul introdus nu face parte din lista")
            category = input("Scrie numarul categoriei dorite ")


def random_word(category, fileList):
    try:
        f = io.open(fileList[category - 1], "r", encoding='utf-8')
        words = []
        for line in f:
            words.append(line.strip())
        f.close()
        return words[random.randint(0, len(words))]
    except:
        print("Unable to open file ", fileList[category])


def write_score(word, mistakes):
    try:
        score = word + ', ' + str(mistakes) + '\n'
        f = io.open("score.txt", "a", encoding='utf-8')
        f.write(score)
        f.close()
    except:
        print("Unable to open file score.txt")


def print_word(word):
    cryptotext = []
    mistakes = int(len(word) / 2)
    for i in range(0, len(word)):
        cryptotext.append('_')
    string = ''
    for i in cryptotext:
        string += i
    print("Cuvantul:")
    print(string)
    diacritics = 'ăîâșț'
    while mistakes > 0 and cryptotext.count('_') > 0:
        print("Numar de greseli ramase:", mistakes)
        letter = input("Litera ta este: ").lower()
        if letter <= 'z' and letter >= 'a' or diacritics.count(letter):
            ok = False
            for i in range(0, len(word)):
                if word[i] == letter and cryptotext[i] != letter:
                    cryptotext[i] = letter
                    ok = True
            if ok:
                string = ''
                for i in cryptotext:
                    string += i
                print(string)
            else:
                mistakes -= 1
        elif len(letter) > 1:
            print("Introduceti o singura litera")
        else:
            print("Caracter invalid")

    print("Cuvantul este: ", word)
    print("Numarul de incercari esuate este: ", int(len(word) / 2) - mistakes)
    write_score(word, int(len(word) / 2) - mistakes)


if __name__ == "__main__":
    fileList = ["animale.txt", "film.txt", "sport.txt"]
    categoryList = ["1. Animale si pasari ", "2. Film", "3. Sport"]

    category = choose_category(categoryList)
    word = random_word(category, fileList)
    print_word(word)

