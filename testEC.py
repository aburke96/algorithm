# Python function to find unique triplets in a hand
def uniqueTriplets(hand):
    if len(hand) < 3:
        return "Not enough to count"
    # Initializing total variable to store the triplets count
    total = 0

    # triplets is a dictionary containing unique triplets
    triplets = {}

    # looping over input hand
    for i in range(len(hand)):
        # Forming a string of face and suit values of cards
        temp = f'{hand[i]["face"]}{hand[i]["suit"]}'
        # Updating their count in triplets dictionary
        if temp in triplets:
            triplets[temp] += 1
        else:
            triplets[temp] = 1

    # looping over triplets dict to find unique triplets
    for key in triplets:
        if triplets[key] >= 3:
            total += 1
    print(triplets)
    # Check if total count is greater than 0
    if total > 0:
        return total
    else:
        return "No triplets found"

# list of cards with attributes face and suit
hand = [
    {
        "face": 2,
        "suit": "diamonds"
    },
    {
        "face": 8,
        "suit": "hearts"
    },
    {
        "face": 14,
        "suit": "clubs"
    },
    {
        "face": 11,
        "suit": "spades"
    },
    {
        "face": 2,
        "suit": "diamonds"
    },
    {
        "face": 8,
        "suit": "hearts"
    },
    {
        "face": 14,
        "suit": "clubs"
    },
    {
        "face": 11,
        "suit": "spades"
    },
    {
        "face": 11,
        "suit": "spades"
    },
    {
        "face": 5,
        "suit": "diamonds"
    },
    {
        "face": 14,
        "suit": "clubs"
    }
]

# Calling the function
print(uniqueTriplets(hand))