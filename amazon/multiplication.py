def multiple(num1, num2):
    fac = 1
    if num1 > 0 and num2 < 0 or (num1 < 0 and num2 > 0):
        fac =  -1
    
    res = helper(abs(num1), abs(num2))
    if fac < 0:
        return 0 - res
    else:
        return res

def helper(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    if num1 == 1 or num2 == 1:
        return num1 if num2 == 1 else num2
    if num2 % 2 == 0:
        return helper(num1, num2/2) + helper(num1, num2/2)
    else:
        return num1 + helper(num1, num2/2) + helper(num1, num2/2)

print multiple(452, 0)
print multiple(1, 4)
print multiple(-1, 3)
