from collections import Counter
COUNT = 30


def dictionary():
    for r in range(COUNT):
        diction = dict.fromkeys(range(r))
        print('Length:', len(diction))
        print('Size:', diction.__sizeof__())
        print('---------------------------------')


def text():
    txt = input('Print text: ')
    split_text = txt.split()
    count_words = Counter(split_text)
    max_word = get_max_key(count_words)
    print('Max word', max_word)

    count_letters = Counter(txt)
    count_letters.pop(' ')
    max_letter = get_max_key(count_letters)
    print('Max letter', max_letter)

    for word in count_words.keys():
        len_wrd = len(word)
        print('Word:', word)

        for letter, count in Counter(word).items():
            average = count / len_wrd
            print('Letter:', letter, '; average:', average)


def palindrome():
    length = int(input('Enter length: '))
    abc = input('Enter alphabet: ')
    palindromes = []

    for symbol in abc:
        for symbol1 in abc:
            word = symbol + symbol1

            if word == ''.join(reversed(word)):
                palindromes.append(word)

            for symbol2 in abc:
                word = symbol + symbol1 + symbol2

                if word == ''.join(reversed(word)):
                    palindromes.append(word)

    for p in palindromes.copy():
        i = 2
        while len(p * i) <= length:
            palindromes.append(p * i)
            i += 1

    print(palindromes)


def get_max_key(d):
    max_val = 0
    max_key = ''
    for k, v in d.items():
        if v > max_val:
            max_key = k
            max_val = v

    return max_key


if __name__ == '__main__':
    print('Dictionary.')
    dictionary()
    print()
    print('Text.')
    text()
    print()
    print('Palindrome.')
    palindrome()
