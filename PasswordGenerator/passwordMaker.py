import string
import random

def main():
    a = select()
    b = select()
    c = select()
    d = select()
    print("Your words are: " + a + " " + b + " " + c + " " + d)
    print("Password: " + a + b + c + d)

def select():
    s = random.choice(tuple(randomwords()))
    if s.isalpha() is False:
        select()
    if "'" in s:
        select()
    return s

def randomwords():  # put words in set
    s = set()
    with open('words.txt', 'r') as f:
        for line in f:
            for word in line.split():
                s.add(word)
    return s  # returns set of words


if __name__ == "__main__":
    main()
