"""
Project Name: Book Recommendations
Author: Zhihui Chen
Due Date: 05/18/2022
Course: CS1410-X01
"""


def main():
    """
    Getting necessary data
    name: string
    people: dict
    """
    name = input("Enter a reader's name: \u001b[1m").lower()  # albus dumbledore
    people = get_data()
    if name not in people:
        return print(f"\u001b[0mNo such reader {name}")
    friends_lst = friends(name, people)
    recommend(people[name], [people[friends_lst[0]], people[friends_lst[1]]])


def friends(name, people):
    """
    name: string, which user entered
    people: dict

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
    val = [i for i in affinity_score.keys()][0: 2]
    val.sort()
    print(f"\u001b[0mRecommendations for {name} from {val[0]} and {val[1]}:")
    return val


def recommend(target_person, people):
    """
    target_person: list, the scores for comparing
    people: list in list, the scores for comparing to target_person

    recommend_book_lst uses to avoid print the same book title
    """
    recommend_book_lst = []
    with open("booklist.txt", "r") as booklist_file:
        booklist_file_lines = booklist_file.read().splitlines()
        for person in people:
            for index, data in enumerate(person):
                if data >= 3 and target_person[index] == 0 and booklist_file_lines[index] not in recommend_book_lst:
                    recommend_book_lst.append(booklist_file_lines[index])
                    # TODO sort by first name, last name, then title
                    lst = booklist_file_lines[index].split(",")
                    print(f"      {lst[0]},\t{lst[1]}")


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
