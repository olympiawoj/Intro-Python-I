

def mult_2(n):
    n *= 2
    return n


x = 5
print(mult_2(x))  # prints 10

print(x)   # prints 5


l = [1, 2, 3, 4]


def append_5(l):
    l.append(5)
    return l


print(append_5(l))  # return [1, 2, 3, 4, 5]
print(l)  # l is list [1, 2, 3, 4, 5]


# s is passed by value, does not get modified
# lists, dicts and sets will,  but strings dont, floats dont, integers dont and so on
# how do you know? know your language
# in JS evertyhing is a value and its stored as a string which leads to interesting behavior like when sroting a list of #s in JS, 123 is sorted before 567.

s = "abc"


def make_capital(s):
    s = s.capitalize()
    return s


print(make_capital(s))
print(s)
