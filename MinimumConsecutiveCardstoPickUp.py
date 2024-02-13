class Solution:
    def minimumCardPickup(self, cards):
        consecutiveCardsWithpair=float('inf')
        d={}
        for i in range(len(cards)):
            if cards[i] not in d:
                d[cards[i]]=i
            else:
                consecutiveCardsWithpair=min(consecutiveCardsWithpair,1+i-d[cards[i]])
                d[cards[i]] = i
        if float('inf')==consecutiveCardsWithpair:
            return -1
        return consecutiveCardsWithpair


print(Solution().minimumCardPickup([3,4,2,3,4,7]))
print(Solution().minimumCardPickup([1,0,5,3]))