'''
Find minimum number of coins that make a given value
Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = {C1, C2, .. , Cm}
valued coins, what is the minimum number of coins to make the change?

'''
'''
--> Corner case
1) coins == None len(coins) == 0
2) val <= 0
3) cannot find the change: assume return -1
'''

def change(coins, val):
    if not coins or len(coins) == 0 or val < 0:
        return -1
    if val == 0:
        return 0
    coins.sort()
    coins.reverse()
    res =  helper(coins, val, None)
    if res == float('inf'): 
        return -1
    return res

def helper(coins, val, last):
    if val == 0:
        return 0

    mini = float('inf')
    for coin in coins:
        if coin <= val:
            prev = helper(coins, val-coin)
            mini = min(mini, prev)

conis = [15, 49]
print change(conis, 123)
