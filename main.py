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


if __name__ == "__main__":
    fileList = ["animale.txt", "film.txt", "sport.txt"]
    categoryList = ["1. Animale si pasari ", "2. Film", "3. Sport"]

    category = choose_category(categoryList)
