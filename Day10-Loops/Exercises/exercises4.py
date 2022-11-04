#Exercises - Day 10
print()

# 4- Usa bucles anidados para crear lo siguiente:
"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
string = "# "
for i in range(8):
    for ico in range(8):
        string = string + "# "
    print(string)
    string = "# "
print()