# My code for the problem:
def distribute_shirts(shirt,bags):
    baseShirt=shirt//bags
    shirtLeft=shirt%bags
    ListOfShirtInBags=[baseShirt]*bags
    for i in range(shirtLeft):
        ListOfShirtInBags[i]=ListOfShirtInBags[i]+1
        deviation=max(ListOfShirtInBags)-min(ListOfShirtInBags)
    print(shirt,"list of bags:",ListOfShirtInBags,"deviation :",deviation)


#Test cases
distribute_shirts(93, 10)
distribute_shirts(151, 13)
distribute_shirts(96, 5)
distribute_shirts(93, 7)
distribute_shirts(101, 7)
distribute_shirts(8, 12)
distribute_shirts(4, 8)

# print( "new test")
# def distribute_shirts(shirt,bags):
#     shirtList=[]
#     if shirt%(bags-1)<shirt%bags:
#         baseShirt=shirt//(bags-1)
#         shirtList=[baseShirt]*(bags-1)
#         shirtList.append(shirt%(bags-1))
#     else:
#         baseShirt = shirt // (bags)
#         shirtList = [baseShirt] * (bags)
#         shirtList[0]=shirtList[0]+(shirt%bags)
#     deviation=max(shirtList)-min(shirtList)
#     print(shirt,"list of bags:",shirtList,"deviation :",deviation)
#
# #Test cases
# distribute_shirts(93, 10)
# distribute_shirts(151, 13)
# distribute_shirts(96, 5)
# distribute_shirts(93, 7)
# distribute_shirts(101, 7)
# distribute_shirts(8, 12)
# distribute_shirts(4, 8)
