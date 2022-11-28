def choose_category(categoryList):
    print("\nCategoriile de cuvinte sunt:")
    for i in categoryList:
        print(i)
    category = input("\nScrie numarul categoriei dorite ")
    while 1:
        if category == '1' or category == '2' or category == '3':
            return int(category)
        else:
            print("Caracterul introdus nu face parte din lista")
            category = input("Scrie numarul categoriei dorite ")


def rendom_word(category, fileList):
    try:
        f = io.open(fileList[category - 1], "r", encoding='utf-8')
        words = []
        for line in f:
            words.append(line.strip())
        f.close()
        return words[random.randint(0, len(words))]
    except:
        print("Unable to open file ", fileList[category])


if __name__ == "__main__":
    fileList = ["animale.txt", "film.txt", "sport.txt"]
    categoryList = ["1. Animale si pasari ", "2. Film", "3. Sport"]

    category = choose_category(categoryList)
    word = rendom_word(category, fileList)
