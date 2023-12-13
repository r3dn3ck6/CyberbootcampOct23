# I used an online kindlebook to learn: Python 2nd Edition: Learn Python in one day and learn it well. Python for beginners with hands-on project. (https://read.amazon.com/?asin=B071Z2Q6TQ&ref_=dbs_t_r_kcr)
# Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.
# the ''' ''' writes a mult-line comment to show it , use print
#Python, the triple single quotes (''') or triple double quotes (""") are used to create multiline strings, also known as docstrings. Docstrings are often used to provide documentation for functions, classes, or modules. They can span multiple lines and are enclosed by either triple single or triple double quotes.
'''
My name is Josh Hughes.
My favorite food is potato soup.
My dream job is a welder.
'''

print ("My Name is Josh Hughes\n My Favorite food are plantains\n My dream job is to be retired and working only on my ranch")

# assign 5 different data types to 5 different variables. At least one datatype must be a string.
# Integer
userage = 57
print(userage)

#Float
userHeight = 68.7
print(userHeight)

#String
userName = "R3dn3ck6\nColombia\nT3XAN"
print(userName)
print(len(userName))

#List
grandkidsAge = [22, 17, 16, 14, 10, 8, 4, 1]
print (grandkidsAge)

userage = [33, 34, 35, 36, 37]
print(userage)

#Dictionary
grandkidsNameAndAge = {"Alexis":22, "Eric":17, "Ariana":17, "Isaiah":16, "Ethan":14, "Arielle":14, "Kalob":8, "Celine":4, "Jabob":1}
print (grandkidsNameAndAge)

grandkidsNameAndAge = dict(Alexis = 22, Eric = 17, Ariana = 17, Isaiah = 16, Ethan = 14, Arielle = 14, Kalob = 8, Celine = 4, Jabob = 1)
print (grandkidsNameAndAge)

# print the length of your string.
string = "Love the LORD your GOD with all your heart, with all your soul, and with all your mind"
print (string)
print(len(string))

# create a new variable called savvy, and assign it the string with this phrase "Learning Python is Awesome!"
savvy = "Learning Python is Awesome!"
print(savvy)

# Replace "Awesome" with "great" in the string
new_savvy=savvy.replace("Awsome, Great")
print(new_savvy)


# Create and assign 3 more variables called name, age and length using the multi-variable naming method.
#Used the Snake Case all lower case 

name, age, length = "Josh", 57, 68

name = "Josh"
age = 57
length = 68
print("name\nage\n\length")

# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today.")
name = "Josh"
tall = "5'8\""
so = 57

miniBio = f"Hi my name is {name}, I am {tall}, and {so} old today."
print (miniBio)

    ###The miniBio string is created using an f-string (formatted string literal) where variables are placed within curly braces {}.
    ###The variables are substituted with their respective values when the string is evaluated.
    ### https://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf

# Create a list of at least 5 elements of mixed data types
mixed_list = [57, "Josh", 68, {"Alexis":22, "Eric":17, "Ariana":17, "Isaiah":16, "Ethan":14, "Arielle":14, "Kalob":8, "Celine":4, "Jabob":1}, ("R3dn3ck6 " + "Colombia " + "T3XAN")]
    #interger, variable, variable, dictionary, string
print (mixed_list)

# replace a part of it with something else
mixed_list1 = [57, "Josh", 68, ("Learning Python is GREAT!"), ("R3dn3ck6 " + "Colombia " + "T3XAN")]
print (mixed_list1)

# append or insert several more items to the list
mixed_list1.[2] = 70
print (mixed_list1)

# find and print the length of the list
print(len(mixed_list))
print(len(mixed_list1))

# slice a sub-section of the 1st list, and save it to a different 2nd list
userage2 = userage[1:3]

# print the 2nd list
print(userage2)

# extend your original list with the 2nd list sliced above
userage.append(38)
print(userage)

# Create a new list called "simList" containing at least 5 elements of the same data type, either string, integer, float, or Boolean.
simList=[50,45,48,47,46, 49]
print(simList)

# sort "simList", and print the list
simList.sort()
print(simList)

# copy the "simList" list to another 3rd list
simList=[50,45,48,47,46, 49]
thirdList = simList.copy()
print(thirdList)

# add the 2nd and 3rd lists together into a 4th list
mixed_list = [57, "Josh", 68, {"Alexis":22, "Eric":17, "Ariana":17, "Isaiah":16, "Ethan":14, "Arielle":14, "Kalob":8, "Celine":4, "Jabob":1}, ("R3dn3ck6 " + "Colombia " + "T3XAN")]
userage2 = userage[1:3]
thirdList = simList.copy()

combined_list = mixed_list + userage2 + thirdList
print (combined_list)
