# Lilah, string s of lowercase letters repeated infinitely many times
# Given int n find and print # of letter a's in the first n letters of lilahs infinite string

# EX: s='abcac' n=10, we consider the substring  'abcacabcac, the first 10 chars
# There are 4 occurences of a in the sub string above

def repeatedString(s, n):
    return(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

# return (the number of a's in the original string s) * (number of chars // length of s) +
# slice of s where only the first n % len(s) characters

# this solution seems trivial but is very hard to comprehend, i don't know how anybody came up with this

