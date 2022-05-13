"""
Project Name: Book Recommendations
Author: Zhihui Chen
Due Date: 05/18/2022
Course: CS1410-X01
"""


def main():
    """
    Program starts here.
    """
    # name = input("Enter a reader's name: ")
    name = "albus dumbledore"
    people = {}
    books = {}
    rate = {}
    with open("booklist.txt", "r") as booklist_file, open("ratings.txt", "r") as rating_file:
        rating_file_lines = rating_file.read().splitlines()
        booklist_file_lines = booklist_file.read().splitlines()
        for index, line in enumerate(rating_file_lines):
            if index % 2 == 0:
                people[line.lower()] = rating_file_lines[index + 1]

        # for line in booklist_file_lines:
        #     print(line)
    # print(people)
    if name.lower() not in people:
        print(f"No such reader {name}")
        return
    for data in people:
        if data != name:
            # compare
            print(data)
    # for data in people[name]:
    #     print(data)

    # for person in people:
    #     print(people[person])


def friends(name):
    """
    TODO
    """


def recommend(name):
    """
    TODO
    """


if __name__ == "__main__":
    main()
