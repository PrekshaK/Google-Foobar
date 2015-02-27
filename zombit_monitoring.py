'''
Zombit monitoring
=================
The first successfully created zombit specimen, Dolly the Zombit, needs constant monitoring, and Professor Boolean has tasked the minions with it. Any minion who monitors the zombit records the start and end times of their shifts. However, those minions, they are a bit disorganized: there may be times when multiple minions are monitoring the zombit, and times when there are none!
That's fine, Professor Boolean thinks, one can always hire more minions... Besides, Professor Boolean can at least figure out the total amount of time that Dolly the Zombit was monitored. He has entrusted you, another one of his trusty minions, to do just that. Are you up to the task?
Write a function answer(intervals) that takes a list of pairs [start, end] and returns the total amount of time that Dolly the Zombit was monitored by at least one minion. Each [start, end] pair represents the times when a minion started and finished monitoring the zombit. All values will be positive integers no greater than 2^30 - 1. You will always have end > start for each interval.
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (int) intervals = [[1, 3], [3, 6]]
Output:
    (int) 5
Inputs:
    (int) intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
Output:
    (int) 16
'''
def are_overlapped(list1, list2):
    if list1[1] > list2[0]:
        return True
    return list


def merge(list1, list2):
    list = []
    if are_overlapped(list1, list2):
        list = [min(list2[0],list1[0]), max(list2[1], list1[1])]
    return list


def condense(list):
    list = sorted(list)
    x = 0
    y = 0
    final_list = [list[0]]
    while y < len(list)-1:
        if are_overlapped(final_list[x], list[y+1]) == True:
            final_list[x] = merge(final_list[x], list[y+1])
        else:
            x += 1
            final_list.append(list[y+1])
        y += 1
    return final_list 
    
def answer(interval):
    list = condense(interval)
    total_time = 0
    for x in list:
        time = x[1] - x[0]
        total_time += time
    return total_time

print answer(interval)
