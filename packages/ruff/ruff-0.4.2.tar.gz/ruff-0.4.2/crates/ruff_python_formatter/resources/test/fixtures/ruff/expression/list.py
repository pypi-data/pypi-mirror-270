# Dangling comment placement in empty lists
# Regression test for https://github.com/python/cpython/blob/03160630319ca26dcbbad65225da4248e54c45ec/Tools/c-analyzer/c_analyzer/datafiles.py#L14-L16
a1 = [  # a
]
a2 = [  # a
    # b
]
a3 = [
    # b
]

# Add magic trailing comma only if there is more than one entry, but respect it if it's
# already there
b1 = [
    aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlahflashdfljahlfksajlhfajfjfsaahflakjslhdfkjalhdskjfa
]
b2 = [
    aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlahflashdfljahlfksajlhfajfjfsaahflakjslhdfkjalhdskjfa,
]
b3 = [
    aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlahflashdfljahlfksajlhfajfjfsaahflakjslhdfkjalhdskjfa,
    aksjdhflsakhdflkjsadlfajkslhfdkjsaldajlahflashdfljahlfksajlhfajfjfsaahflakjslhdfkjalhdskjfa
]

# Comment placement in non-empty lists
c1 = [ # trailing open bracket
    # leading item
    1,

    # between

    2, # trailing item
    # leading close bracket
] # trailing close bracket


[  # end-of-line comment
]

[  # end-of-line comment
    # own-line comment
]

[  # end-of-line comment
    1
]

[  # inner comment
    first,
    second,
    third
]  # outer comment

[  # inner comment
    # own-line comment
    (  # end-of-line comment
        # own-line comment
        first,
    ),
]  # outer comment
