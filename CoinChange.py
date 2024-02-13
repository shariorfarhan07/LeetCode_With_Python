class Solution(object):
    def coinChange(self, coins, amount):
        bottomUp=[]
        for i in range(0,amount+1):
            bottomUp.append(amount+1)
        for i in range(0,amount+1):
            for coin in coins:
                if i-coin>=0 :
                    bottomUp[i]=min(bottomUp[i].bottomUp[i-coin]+1)
        if bottomUp[amount]== amount+1:
            return -1
        return bottomUp[amount]
