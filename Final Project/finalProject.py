# Stable matching algorithm
# N viewers and N ads
# Each viewer has ranked all N ads by preference
# Each ad has ranked all N viewers by preference
#
# Algorithm's goal: assign viewers to ads such that
# there are no pairs of (viewer, ad) who would both
# prefer each other over their current match
# If there are no such pairs, the matching is "stable"

# A "matching" is where we assign each viewer to an ad
# (and each ad to a viewer)


# Input to the algorithm:
viewers = [1, 2, 3, 4]
ads = [1, 2, 3, 4]
viewer_preferences = [
    queue([3, 2, 4, 1]),
    queue([2, 3, 4, 1]),
    queue([1, 3, 2, 4]),
    queue([4, 3, 2, 1])
]
ad_preferences = [
    queue([1, 2, 3, 4]),
    queue([4, 3, 2, 1]),
    queue([2, 3, 4, 1]),
    queue([1, 4, 2, 3])
]