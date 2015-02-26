'''
Zombit antidote
===============

Forget flu season. Zombie rabbits have broken loose and are terrorizing Silicon Valley residents! Luckily, you've managed to steal a zombie antidote and set up a makeshift rabbit rescue station. Anyone who catches a zombie rabbit can schedule a meeting at your station to have it injected with the antidote, turning it back from a zombit to a fluffy bunny. Unfortunately, you have a limited amount of time each day, so you need to maximize these meetings. Every morning, you get a list of requested injection meetings, and you have to decide which to attend fully. If you go to an injection meeting, you will join it exactly at the start of the meeting, and only leave exactly at the end.

Can you optimize your meeting schedule? The world needs your help!

Write a method called answer(meetings) which, given a list of meeting requests, returns the maximum number of non-overlapping meetings that can be scheduled. If the start time of one meeting is the same as the end time of another, they are not considered overlapping.

meetings will be a list of lists. Each element of the meetings list will be a two element list denoting a meeting request. The first element of that list will be the start time and the second element will be the end time of that meeting request.

All the start and end times will be non-negative integers, no larger than 1000000. 
The start time of a meeting will always be less than the end time.

The number of meetings will be at least 1 and will be no larger than 100.
The list of meetings will not necessarily be ordered in any particular fashion.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

'''

#I wish this worked. This code failed 2 test cases.
'''
def are_overlapped(list1, list2):
    if min(list2[1], list1[1]) > max(list1[0], list2[0]):
        return True
  


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

def answer(meetings):
    different_meetings = condense(meetings)
    new_meetings = []
    for meeting in different_meetings:
        if meeting[0] != meeting[-1]:
            new_meetings.append(meeting)
    return len(new_meetings) 
'''

#This also failed two test cases
'''
def answer(intervals):
    new = []
    for meeting in intervals:
        for x in meeting:
            new.append(x)
    count = 1
    yes = True
    for meeting in intervals:
        for element in new:
            if meeting[0] < element < meeting[1]:
                yes = False
        if yes == True:
            count += 1
    return count
'''




#This worked fine

import operator

def answer(meetings):
    sorted_meetings = sorted(meetings, key=operator.itemgetter(1))
    final_meetings = []
    for meeting in sorted_meetings:
        overlapped = False
        for sample in final_meetings:
            if meeting[0] < sample[1] and meeting[1] > sample[0]:
                    overlapped = True
        if overlapped == False:
            final_meetings.append(meeting)
    return len(final_meetings)



