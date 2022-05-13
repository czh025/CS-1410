"""
Project Name: Book Recommendations
Author: Zhihui Chen
Due Date: 05/18/2022
Course: CS1410-X01
"""


def main():
    """
    TODO
    """
    name = input("Enter a reader's name: ")
    people = get_data()
    if name.lower() not in people:
        print(f"No such reader {name}")
        return
    friends_lst = friends(name, people)
    print(f"Recommendations for {name} from {friends_lst[0]} and {friends_lst[1]}:")
    recommend(people[name], {friends_lst[0]: people[friends_lst[0]], friends_lst[1]: people[friends_lst[1]]})


def friends(name, people):
    """
    TODO
    """
    affinity_score = {}
    for person in people:
        if person != name:
            for index, rate in enumerate(people[person]):
                if person not in affinity_score:
                    affinity_score[person] = 0
                affinity_score[person] += rate * people[name][index]
    affinity_score = dict(sorted(affinity_score.items(), key=lambda item: -item[1]))
    val = [i for i in affinity_score.keys()][0: 2]
    val.sort()
    return val


def recommend(target_person, people):
    """
    TODO
    """
    recommend_book_lst = []
    with open("booklist.txt", "r") as booklist_file:
        booklist_file_lines = booklist_file.read().splitlines()
        for person in people:
            for index, data in enumerate(people[person]):
                if data >= 3 and target_person[index] == 0 and booklist_file_lines[index] not in recommend_book_lst:
                    recommend_book_lst.append(booklist_file_lines[index])
                    print("     ", booklist_file_lines[index])


def get_data():
    people = {}
    with open("ratings.txt", "r") as rating_file:
        rating_file_lines = rating_file.read().splitlines()
        for index, line in enumerate(rating_file_lines):
            if index % 2 == 0:
                people[line.lower()] = list(map(int, rating_file_lines[index + 1].split()))
    return people


if __name__ == "__main__":
    main()
