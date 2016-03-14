def change(n, coins):
    if n <= 0:
        return -1
    total = []
    coins.sort()
    coins.reverse()
    helper(total, coins, 0, [], n)
    return total

def helper(total, coins, index, sub, n):
    if len(total) > 0:
        return 
    if n == 0:  
        total.append(sub[:])
    for i in range(index, len(coins)):
        coin = coins[i]
        if coin <= n:
            sub.append(coin)
            helper(total, coins, i, sub, n-coin)
            sub.pop()

coins = [1, 5, 10, 25]
print change(154, coins)
