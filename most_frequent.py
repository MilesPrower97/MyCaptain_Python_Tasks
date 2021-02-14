import collections

string = input("Please enter a string: ")

def most_frequent():
    x = collections.Counter(string)
    print(str(x))
most_frequent()