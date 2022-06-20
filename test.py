"""
metro_lat_long.py

Demonstration of nested tuple unpacking::

    >>> main()
                    |  latitude | longitude
    Mexico City     |   19.4333 |  -99.1333
    New York-Newark |   40.8086 |  -74.0204
    São Paulo       |  -23.5478 |  -46.6358

"""

# tag::MAIN[]
phone = ["3852075000", "15980101010"]

def main():
    for record in phone:
        match tuple(record):  # <1>
            case ["1", *rest]:  # <2>
                print("China", rest)
            case ["3", *rest]:
                print("America", rest)
# end::MAIN[]

if __name__ == '__main__':
    main()