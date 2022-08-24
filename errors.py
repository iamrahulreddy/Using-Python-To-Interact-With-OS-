myList=['sunny',"rahul","sam","alex"]
def OrganizeList(myList):
    for item in myList:
        assert type(item) == str,"Items In List Should Be Only Strings"
    myList.sort()
    return myList

print(OrganizeList(myList))