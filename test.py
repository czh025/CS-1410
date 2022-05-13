def main():
    my_str = "hello"
    vowels = ["a", "e", "i", "o", "u"]
    print("".join(["*" if x in vowels else x for x in my_str]))
    # new_str = my_str.replace(i for i in my_str if i in vowels, "*")
    # print(t(2, lst))
    # print((lambda x: x if x in my_str else "")(i for i in ["a", "e", "i", "o", "u"]))
    print

def most_frequent(word):
  dic = {}
  for char in word:
    if char not in dic:
      dic[char] = 1
    else:
      dic[char] += 1
  print(dic)
if __name__ == '__main__':
    most_frequent("hello")
    # main()