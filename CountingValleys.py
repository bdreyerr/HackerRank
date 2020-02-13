# Ben Dreyer
# Hacker Rank Interview Prep Warm up Challenges
# Sock Merchant
# 2.11.2020

# Gary hikes, during his last hike he took n steps.
# U for uphill, D for downhill for every step.
# Gary's hike start and end at sea level, each step up or down represents Delta 1 in altitude
# A mountain is a sequence of consecutive steps above sea level, MUST start with step up from sea level(0),
#   ends with a step down to sea level(0)
# A valley is a sequence of steps below sea level, starting with a step down from sea level,
#   ends with a step up to sea level


# Entities: Steps(Uphill or Downhill), Mountain(sequence of steps), Valley(Sequence of steps)

# Given Gary's sequence of up and down steps during his latest hike:
#   Find and Print the number of VALLEYS he walked through, DISREGARD MOUNTAINS
# EX: path = [DDUUUUDD]
#   Our output would be 1 because Gary walked through one valley

# Input: n -> number of steps
#        s[i] -> a single string of n characters of U or D (-1 or 1)

# Constraints: 2 <= n <10^6, There must be at least 2 steps in Gary's hike, so 0 or 1 valleys miniumum
#              s[i] contain {UD}

word = 'DDDDUUUU'
# Slice the string into an array of chars

s = ([word[i:i+1] for i in range(0,len(word), 1)])
print s

def counting_valleys(n, s):
    sea_level = 0
    count = 0
    # Slice the string into a list where characters are seperated
    ar = [s[i:i+1] for i in range(0, len(s), 1)]
    ar.append('!')
    # ar = ['D', 'U', 'D'....] vs s = "DDDUUUDD"
    # We are looking for the number of valleys, which means the number of times the hike goes below the sea level or 0
    # We are not interested in where the hike ends, but rather the path that leads to the end
    for x in range(len(ar)):
        if ar[x] == 'D':
            seaLevel = sea_level - 1
        if ar[x] == 'U':
            seaLevel = sea_level + 1
        if sea_level == 0 and ar[x] == 'U':
            count = count + 1
    # Now we need to determine every time the sealevel transitionfs from -1 to 0
    return count
num_valleys = counting_valleys(len(word), word)
print num_valleys