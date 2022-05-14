"""
Project Name: Book Recommendations
Author: Zhihui Chen
Due Date: 05/18/2022
Course: CS1410-X01

This project can suggest book that users might like based on the books they like

Before running this project make sure you have the 'booklist.txt' and 'ratings.txt' files.
"""


def main():
    """
    Getting necessary data
    name: string
    people: dict
    """
    # \u001b[1m add bold text style
    name = input("Enter a reader's name: \u001b[1m").lower()  # albus dumbledore
    # \u001b[0m restore to default style
    print('\u001b[0m', end='')
    people = get_data()
    if name not in people:
        return print(f"No such reader {name}")
    friends_lst = friends(name, people)
    print(f"Recommendations for {name} from {friends_lst[0]} and {friends_lst[1]}:")
    rec_book_lst = recommend(people[name], [people[friends_lst[0]], people[friends_lst[1]]])
    for i in rec_book_lst:
        print("     ", "\t".join(i))


def friends(name, people):
    """
    name: string, which user entered
    people: dict, data from booklist.txt

    find the two people with the highest affinity scores

    return a list with two names
    """
    affinity_score = {}
    for person in people:
        # filter the name which user entered
        if person != name:
            for index, rate in enumerate(people[person]):
                if person not in affinity_score:
                    affinity_score[person] = 0
                affinity_score[person] += rate * people[name][index]
    affinity_score = dict(sorted(affinity_score.items(), key=lambda item: -item[1]))
    val = sorted([*affinity_score][0: 2])
    return val


def recommend(target_person, people):
    """
    target_person: list, the scores for comparing
    people: list in list, the scores for comparing to target_person

    rec_book_lst uses to avoid print the same book title

    return a list with recommend book data
    """
    rec_book_lst = []
    with open("booklist.txt", "r") as booklist_file:
        book_lines = booklist_file.read().splitlines()
        for person in people:
            for index, data in enumerate(person):
                if data >= 3 and target_person[index] == 0 and book_lines[index].split(",") not in rec_book_lst:
                    rec_book_lst.append(book_lines[index].split(","))
    rec_book_lst = sorted(rec_book_lst, key=lambda x: (x[0].split()[-1], x[0].split()[0], x[-1]))
    return rec_book_lst


def get_data():
    """
    Get necessary data from 'ratings.txt' file
    return a dict
    """
    people = {}
    with open("ratings.txt", "r") as rating_file:
        rating_file_lines = rating_file.read().splitlines()
        for index, line in enumerate(rating_file_lines):
            if index % 2 == 0:
                people[line.lower()] = list(map(int, rating_file_lines[index + 1].split()))
    return people


if __name__ == "__main__":
    main()
