#!/usr/bin/env python3
#!
# birthday_paradox.py
#
# Refer: https://en.wikipedia.org/wiki/Birthday_problem
# Use random.randint() to model the birthday problem.
# 
# Ian Stewart - 27 Jan 2020 - © CC0
#
import itertools
import time
import random
import sys

iterations = 100
list_length = 23
days_in_year = 365

help = """
birthday_paradox.py [iterations] [list length - people]

Refer: https://en.wikipedia.org/wiki/Birthday_problem

In probability theory, the birthday problem or birthday paradox concerns the 
probability that, in a set of n randomly chosen people, some pair of them 
will have the same birthday.

It can be shown that the number of people required to reach the 50% threshold 
is 23 or fewer. With 70 people there is a 99.9% threshold.

Probabilities:
1   0.0%
5   2.7%
10  11.7%
20  41.1%
23  50.7%
30  70.6%
40  89.1%
50  97.0%
60  99.4%
70  99.9%
75  99.97%
100 99.99997% 
"""

def get_dupes(c):
        '''
        From a list create a list of the duplicates.
        Code from: 
        https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them/9835819'''
        a, b = itertools.tee(sorted(c))
        next(b, None)
        r = None
        for k, g in zip(a, b):
            if k != g: 
                continue
            if k != r:
                yield k
                r = k

def main(iterations, list_length):
    """
    Repeatedly generate a fixed length list of random integer values in the 
    range 1 to 365. Each integer represents a day of the year that someone is
    born on.
    
    Check each list for duplicates. i.e. Keep a count for if two birthdays 
    occur on the same date.
    """
    start_time = time.time()
    no_dup = 0
    dup = 0
    extra_dup = 0

    for i in range(iterations):
        random_list = []
        for j in range(list_length):
            random_list.append(random.randint(0,days_in_year))
        #print(random_list)
        #print(list(get_dupes(random_list)))
        dup_list = list(get_dupes(random_list))

        if dup_list:
            dup += 1
            if len(dup_list) > 1:
                extra_dup += 1
        else:
            no_dup += 1

    percent = dup * 100 / iterations

    print("Total iterations: {}\n"
          "Total items in a list: {}\n"
          "Total list without duplicates: {}\n"
          "Total lists with duplicates: {}\n"
          "More than one duplicate {}\n"
          "Duplicate percentage: {:.1f}%\n"
          .format(iterations, list_length, no_dup, dup, extra_dup, percent)) 
          
    print("Duration: {:.1f}".format( time.time() - start_time))

    #print(list(get_dupes([1,1,1,2,3,4,5,6])))
    #[1]


if __name__ == "__main__":

    # Number of iterations or help
    if len(sys.argv) > 1:
        if sys.argv[1].isnumeric():
            iterations = int(sys.argv[1])
        else:
            print(help)
            sys.exit()

    # length of a list. i.e. Number of people in the room.
    if len(sys.argv) > 2:
        if sys.argv[2].isnumeric():
            list_length = int(sys.argv[2])

    main(iterations, list_length)

"""
Example:

$ python3 birthday_paradox.py 1000000 23
Total iterations: 1000000
Total items in a list: 23
Total list without duplicates: 494676
Total lists with duplicates: 505324
More than one duplicate 135313
Duplicate percentage: 50.5%

Duration: 74.6

===

$ python3 birthday_paradox.py 1000 70
Total iterations: 1000
Total items in a list: 70
Total list without duplicates: 1
Total lists with duplicates: 999
More than one duplicate 993
Duplicate percentage: 99.9%

Duration: 0.2

"""
