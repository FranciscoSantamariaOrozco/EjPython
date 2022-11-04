#Exercises - Day 10
print()

# 3- Escribe un bucle que haga 7 llamadas a print(), para que en el output aparezca el siguiente triángulo:
"""
    #
    ##
    ###
    ####
    #####
    ######
    #######
"""
Tree = ("#")
AddBranch = ("#")
for i in range(7):
    print(Tree)
    Tree = Tree + AddBranch
print()