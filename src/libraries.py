COUNT = 30


def dictionary():
    for r in range(COUNT):
        diction = dict.fromkeys(range(r))
        print('Length:', len(diction))
        print('Size:', diction.__sizeof__())
        print('---------------------------------')


if __name__ == '__main__':
    print('Dictionary.')
    dictionary()
