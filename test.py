
def main():
    # lst = ["asdf fda"]
    # print(lst[0].split()[0].split("s"))
    # return
    lst = [
        "Douglas Adams,The Hitchhiker's Guide To The Galaxy",
        "Dan Brown,The Da Vinci Code",
        "F. Scott Fitzgerald,The Great Gatsby",
        "Cornelia Funke,Inkheart",
        "William Goldman,The Princess Bride",
        "C S Lewis,The Lion the Witch and the Wardrobe",
        "Gary Paulsen,Hatchet",
        "Jodi Picoult,My Sister's Keeper",
        "Philip Pullman,The Golden Compass",
        "Louis Sachar,Holes",
        "J R R Tolkien,The Lord of the Rings",
        "J R R Tolkien,The Hobbit",
        "Eric Walters,Shattered",
        "H G Wells,The War Of The Worlds",
        "John Wyndham,The Chrysalids"
    ]
    l = lst.split(",")
    print(l)
    return
    my_lst = []
    for i in lst:
        author, title = i.split(",")
        info = author.split()
        info = [info[0], info[-1]]
        info.append(title)
        my_lst.extend([[info[0], info[-2], info[-1]]])
    print(sorted(my_lst, key = lambda x: (x[1], x[0], x[-1])))


if __name__ == '__main__':
    main()