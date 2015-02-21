'''Name that rabbit
================

"You forgot to give Professor Boolean's favorite rabbit specimen a name? You know how picky the professor is! Only particular names will do! Fix this immediately, before you're... eliminated!"

Luckily, your minion friend has already come up with a list of possible names, and we all know that the professor has always had a thing for names with lots of letters near the 'tail end' of the alphabet, so to speak. You realize that if you assign the value 1 to the letter A, 2 to B, and so on up to 26 for Z, and add up the values for all of the letters, the names with the highest total values will be the professor's favorites. For example, the name Annie has value 1 + 14 + 14 + 9 + 5 = 43, while the name Earz, though shorter, has value 5 + 1 + 18 + 26 = 50. 

If two names have the same value, Professor Boolean prefers the lexicographically larger name. For example, if the names were AL (value 13) and CJ (value 13), he prefers CJ.

Write a function answer(names) which takes a list of names and returns the list sorted in descending order of how much the professor likes them. 

There will be at least 1 and no more than 1000 names. 
Each name will consist only of lower case letters. The length of each name will be at least 1 and no more than 8.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string list) names = ["annie", "bonnie", "liz"]
Output:
    (string list) ["bonnie", "liz", "annie"]

Inputs:
    (string list) names = ["abcdefg", "vi"]
Output:
    (string list) ["vi", "abcdefg"]
'''

def answer(names):
    
    dict = { 'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    new_dict = {}
    list = []
    new_list = []
    
    for name in names:
        sum = 0.00
        
        for letter in name:
            sum += dict[letter]

        str_sum = str(dict[name[0]]) #+ str(dict[name[1]]) #+ str(dict[name[2]])  
        new_dict[sum + (int(str_sum)/1000.0)] = name
        list.append(sum + (int(str_sum)/(1000.0)))

        
    list = sorted(list)
    for items in xrange(len(list)-1, -1, -1):
        new_list.append(list[items])
    print new_list
    
    for x in xrange(len(new_list)):
        new_list[x] = new_dict[new_list[x]]
        
    return new_list
