# // Some code
# //Currency Exchange
# //calculate the max exchange rate with at most k steps (1,n-1) from c1 to currency c2
# //max exchange rate for k+1 steps from c1 to c2 = Max(rate(c, c2)* max 
# exchangerate from c1 to c in at most k steps, k steps c1 to c2) (c2 will be 
# unused currency in previous k steps)
# //rate1*rate2> originalRate

# //memo[k, current] max exchenge rate from original currency to current currency with k steps
# // = memo[k-1, whatever currency that not used]*rate(current/whatever currency), 
# memo[k-1, current]

currencies = ["USD","CAD","EUR","CNY"]
table = [[1,1,1,0.00001],[0.72,1,0.9,5.5],[1.1,1.1,1,7.3],[0.18,0.2,0.136,1]]

# public static int targetCurr;
currencyAtHand = "USD"
target = "CNY"

targetCurr = 0
names = {}
memo = [[-1 for i in range(len(currencies))] for j in range(len(currencies))]
loggedtable = [[0 *len(table)] *len(table)]
# names[usd] = 0
for i in range(len(currencies)):
    names[currencies[i]] = i
# current = 0, 1, 2, 3
current = names[currencyAtHand]
targetCurr = names[target]

def dfs(target, current, visited, step):
    if target == targetCurr:
        return 
    
    for i in range(len(table)):
        pass
    

def maxTransactionRate(currencies, table,  target,  currencyAtHand):
    names = {}
    memo = [[0 for i in range(len(currencies))] for j in range(len(currencies))]
    loggedtable = [[0 *len(table)] *len(table)]
    # names[usd] = 0
    for i in range(len(currencies)):
        names[currencies[i]] = i
    # current = 0, 1, 2, 3
    current = names[currencyAtHand]
    
    for i in range(len(currencies)):
        memo[1][i] = table[current][i]
    exchanged = set()
    # target = 0, 1, 2, 3
    targetCurr = names[target]

    exchanged.add(current)

    
    for j in range(len(table)):
        for i in range(len(table)):
            if i not in exchanged:
                exchanged.add(i)
                memo[j][i] = max(memo[j-1][i], memo[j-1][current]*table[current][i])
                exchanged.remove(i)

    return memo[len(table)-1][targetCurr]
    # //whether to add currency in exchange line: log(rate(c/c1))+log(rate(c2/c))-log(rate(c2/c1))>0

print(maxTransactionRate(currencies, table, "CNY","USD"))

