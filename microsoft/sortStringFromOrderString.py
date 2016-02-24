'''
sort a string according to the order from another string:
eg. order = dfbcae
    input = abcdeeabc
    output = dbbccaaee

'''

def sort(order, input):
    map = {}
    for i in range(len(order)):
        here = order[i]
        if here not in map:
            map[here] = len(map.keys())
    temp = []
    for i in range(len(input)):
        char = input[i]
        temp.append((map[char], char))
    temp.sort()
    res = []
    for item in temp:
        res.append(item[1])
    return res

order = 'dfbcae'
input = 'abcdeeabc'
print sort(order, input)
