# birthday-paradox

The birthday paradox is described at: https://en.wikipedia.org/wiki/Birthday_problem

The program birthday_paradox.py may be used to model this paradox.

In probability theory, the birthday problem or birthday paradox concerns the 
probability that, in a set of n randomly chosen people, some pair of them 
will have the same birthday.

It can be shown that the number of people required to reach the 50% threshold 
is 23 or fewer. With 70 people there is a 99.9% threshold.

## Probabilities:
* 1   0.0%
* 5   2.7%
* 10  11.7%
* 20  41.1%
* 23  50.7%
* 30  70.6%
* 40  89.1%
* 50  97.0%
* 60  99.4%
* 70  99.9%
* 75  99.97%
* 100 99.99997% 

## Examples:

Two command line arguments may be passed to the program. The first is the number of iterations
and second is what is effectively the number of random people in the room. 
The default values are 100 and 23.

$ python3 birthday_paradox.py 1000000 23
Total iterations: 1000000
Total items in a list: 23
Total list without duplicates: 494676
Total lists with duplicates: 505324
More than one duplicate 135313
Duplicate percentage: 50.5%

Duration: 74.6

$ python3 birthday_paradox.py 1000 70
Total iterations: 1000
Total items in a list: 70
Total list without duplicates: 1
Total lists with duplicates: 999
More than one duplicate 993
Duplicate percentage: 99.9%

Duration: 0.2
