'''
Step 1
Imagine an Airbnb-like vacation rental service, where users in different cities can exchange their apartment 
with another user for a week.
Each user compiles a wishlist of the apartments they like. These wishlists are ordered, 
so the top apartment on a wishlist is that user's first choice for where they would like to spend a vacation.
You will be asked to write part of the code that will help an algorithm find pairs of users who would like 
to swap with each other.

Given a set of users, each with an *ordered* wishlist of other users' apartments:
a's wishlist: c d
b's wishlist: d a c
c's wishlist: a b
d's wishlist: c a b

The first user in each wishlist is the user's first-choice for whose apartment they would like to swap into.
Write a function called has_mutual_first_choice() which takes a username and returns true if that user and 
another user are each other's first choice, and otherwise returns false.

has_mutual_first_choice('a') # true (a and c)
has_mutual_first_choice('b') # false (b's first choice does not *mutually* consider b as their first choice)

Then expand the base case beyond just "first" choices, to include all "mutually ranked choices".
Write another function which takes a username and an option called "rank" to indicate the wishlist rank to query on.
If given a rank of 0, you should check for a first choice pair, as before. If given 1, you should check for a pair 
of users who are each others' second-choice.
Call your new function has_mutual_pair_for_rank() and when done, refactor has_mutual_first_choice() to depend on 
your new function.

has_mutual_pair_for_rank('a', 0) # true (a and c)
has_mutual_pair_for_rank('a', 1) # true (a and d are mutually each others' second-choice)
'''

'''
Step 2
Every wishlist entry in the network is either "mutually ranked" or "not mutually ranked" depending on the 
rank the other user gives that user's apartment in return.

The most common operation in the network is incrementing the rank of a single wishlist entry on a single user.
This swaps the entry with the entry above it in that user's list. Imagine that, when this occurs, the system 
must recompute the "mutually-ranked-ness" of any pairings that may have changed.

Write a function that takes a username and a rank representing the entry whose rank is being bumped up.
Return an array of the users whose pairings with the given user *would* gain or lose mutually-ranked status 
as a result of the change, if it were to take place.
Call your function changed_pairings().

if d's second choice becomes their first choice, a and d will no longer be a mutually ranked pair
changed_pairings('d', 1) # returns ['a']

if b's third choice becomes their second choice, c and b will become a mutually ranked pair (mutual second-choices)
changed_pairings('b', 2) # returns ['c']

if b's second choice becomes their first choice, no mutually-ranked pairings are affected
changed_pairings('b', 1) # returns []
'''

'''
Step 3
A user's last choice is the last entry on their wishlist. Their second-to-last choice is second to last on their wishlist.
This can be continued to define third-to-last choice, and so on, always counting from the end of the user's list of apartments.

A mutually-ranked-anti-pairing is one where both parties rank each other's apartments identically near to (or far from) the *end* of each of their wishlists.

Implement changed_antipairings(username, rank) to return an array of the users whose pairings with the given user either gain or lose mutually-ranked-anti-pairing status as a result of the change.
Note that, as before, the username and rank passed in identify the entry whose rank is being bumped up, so (a, 1) would refer to a's second-choice.

if b's third choice becomes their second choice, b and c will no longer be a mutually-ranked anti-pairing
changed_antipairings('b', 2) # returns ['c']

if a's second choice becomes their first choice, a and c will be no longer be a mutually ranked anti-pairing
in addition, a and d will become a mutually ranked anti-pairing (the second-to-last choice of each other)
changed_antipairings('a', 1) # returns ['c', 'd']


'''