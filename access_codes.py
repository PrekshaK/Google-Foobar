def answer(x):
    list = []
    for codes in x:
        list.append(''.join(sorted(codes)))
    print set(list)
    return len(set(list))
x = ["cba", "abc", "abc", "bhy", "yhb", "bhy", "bac", "haha", "", "000000", "00000"]
print answer(x)

def are_reversed(string1, string2):
    if string1[::-1] == string2 or string2[::-1} == string1:
        return True

def answer(x):
    list = []
    for codes in x:
        



