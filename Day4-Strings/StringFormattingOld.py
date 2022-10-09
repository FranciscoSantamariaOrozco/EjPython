"""
    %s - String
    %d - integers
    %f - floating
    "%.numbordigitsf" - Floating point numbers with fixed precision
"""
print()

# Strings only
FirstName = "Francisco"
LastName = "Orozco"
Language = "Python"
FormatedString =  "I am %s %s. I teach %s" %(FirstName, LastName, Language)
print(FormatedString)
print()

# String and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
FormatedStringStringsandnumbers = "The area of a circle with a radius %d is %2.f." %(radius,area)
print(FormatedStringStringsandnumbers)
print()

# More strings
PythonLibraries = ["Django", "Flask", "NumPy", "Matplotlib", "Pandas"]
FormatedStringMoreStrings = "The following are python libraries:%s" %(PythonLibraries)
print(FormatedStringMoreStrings)
print()