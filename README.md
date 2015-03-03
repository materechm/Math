# Math
This repository hopefully will contain several math projects, although at the moment it only contains one (in progress) 
##Goldbach triplets 

A Goldbach partition is a division of an even number into two primes. I used a list of primes as an input (the first million primes here: https://primes.utm.edu/lists/small/millions/ 

I then, for all primes (p) in the list got 2p, and then looked for partitions in which both primes were equidistant from p. I generated the triplet (p_a, p, p_b) where p_a and p_b are the two primes in the partition (p_b is the largest). I then generated a dictionary and set p_a to be the key and p to be the value associated with the key (if there are several triplets that contain both p_a and p then there are several values associated to the key). I did the same with p as key and p_b as value and then generated a csv file with all the relationships (p_a : p, p : p_b), then generated two extra files: one that contains all relationships in which the key is congruent with 1 mod 6 and the other one in which the key is congruent with 5 mod 6. The reason I did this is because after graphing all the relationships I found that two clusters formed and the characteristics of this clusters were that one was congruent with 1 mod 6 and the other one with 5 mod 6.

Something else that is interesting to note from this is that most of the distances between p and p_a, p_b are 6 or a multiple of 6. 
