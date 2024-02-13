def distribute_shirts1(shirt,bags):
    baseShirt=shirt//bags
    shirtLeft=shirt%bags
    ListOfShirtInBags=[baseShirt]*bags

    for i in range(shirtLeft):
        ListOfShirtInBags[i]=ListOfShirtInBags[i]+1

    deviation=max(ListOfShirtInBags)-min(ListOfShirtInBags)
    print("list of bags:",ListOfShirtInBags,"deviation :",deviation)



def distribute_shirts(shirt,bags):
    baseShirtCase1 = shirt // (bags-1)
    shirtLeftOnLastBag = shirt % (bags-1)
    ListOfShirtInBags = []
    baseShirtCase2 = shirt // bags
    shirtLeft = shirt % bags

    if abs(baseShirtCase1-shirtLeftOnLastBag) < abs(baseShirtCase2-shirtLeft):
        ListOfShirtInBags = [baseShirtCase1] * (bags-1)
        ListOfShirtInBags.append(shirtLeftOnLastBag)
    else:
        ListOfShirtInBags = [baseShirtCase2] * bags
        ListOfShirtInBags[0]=ListOfShirtInBags[0]+shirtLeft
    deviation=max(ListOfShirtInBags)-min(ListOfShirtInBags)
    print("list of bags:",ListOfShirtInBags,"deviation :",deviation)








    pass


#Test cases
distribute_shirts(93, 10)
distribute_shirts(151, 13)
distribute_shirts(96, 5)
distribute_shirts(93, 7)
distribute_shirts(101, 7)
distribute_shirts(100, 10)
# distribute_shirts(8, 12)
# distribute_shirts(4, 8)