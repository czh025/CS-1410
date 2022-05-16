
def main():
    cache = {}
    cache[(1, 1)] = 0
    cache[(2, 1)] = 100
    print(cache.get((1, 1)))


if __name__ == '__main__':
    main()