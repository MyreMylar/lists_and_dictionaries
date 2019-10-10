# ---------------------------------------------------------------
# Lists - part 1
# ------
# A python list is used to store several bits of data
# in one place under a single variable name.
# It is a very useful think to have when you have hundreds, thousands
# or millions of bits of data. Imagine writing a million different
# variable names!
#
# Keeping all that data in one structure make it very easy to loop
# though it performing the same operations on each piece of data in
# the list.
#
# ---------------------------------------------
# Lets have a look at how we can create a list.
# ---------------------------------------------------------------
print("Lists: Part 1\n-------\n")
# here is a list of numbers, created with a bunch of different numbers in it at the start
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# here is a list created with nothing in it, which we then add, or append, some decimals to.
my_empty_list = []
my_empty_list.append(3.14)
my_empty_list.append(3.14)
my_empty_list.append(4.13)  # the function is called append because it always adds the new data at the end of the list.

# here is a list containing some strings
my_names = ["Dan", "Steve", "Ronin", "Ahab", "Jesus", "Mohammad"]

# if you can make a regular variable of a piece of data, then you can also put it in a list
my_boolean_logic_variable_1 = True
my_boolean_logic_variable_2 = False
my_logical_list = [my_boolean_logic_variable_1, my_boolean_logic_variable_2]

# you can also print lists to the console as I do here
print(my_list)
print(my_empty_list)
print(my_names)
print(my_logical_list)

# -----------------------------------------------------------------------------
# Part 2: What can we do with lists?
# --------------------------
# One of the most common uses for a list is because we have lot of pieces of data
# and we want to do the same things to each one in our code.
# A for loop takes care of this.
#
# Another common use case is because we want to sort the pieces of data into
# an order. Python's sort() and sorted() functions can take care of that for us.
#
# Lets look at some examples!
# -----------------------------------------------------------------------------
print("\nLists: Part 2\n-------\n")
number_total = 0
for number in my_list:      # We use the 'in' keyword with for to loop through each item in the list,
    number_total += number  # 'number' is used here as a temporary variable name for each item.
print("Number total: " + str(number_total))


my_names.sort()  # the sort function does an 'in place' sort working directly on the list
print(my_names)

# you can also refer to individual items in a list using 'index notation'
print(my_names[0])  # using '0' as an index refers to the first item in the list
my_names[2] = "Bob"  # '2' refers to the 3rd item in the list, here I've used = to change the name in the list
print(my_names)

# -------------------------------------------------------------------
# Challenge 1
# ------------
#
#  a) Create a list of all the vowels in the alphabet.
#  b) Loop through the list printing each vowel to the console.
#  c) Sort your list, then print only the 5th value to the console
#
# -------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# Dictionaries
# ------------
#
# A dictionary is another container for multiple pieces of data - like a list, but
# instead of just using numbers as indexes, each piece of data also has a 'key' that
# you can use to index the data.
#
# Lets look at some examples!
# ---------------------------------------------------------------------------------------
print("\nDictionaries\n------------\n")
my_age_dictionary = {"dan": 35, "sid": 42, "mary": 15, "gary": 18}
print(my_age_dictionary)
print(my_age_dictionary["mary"])  # here we are using the 'key' as an index to find the associated 'value'

print("\nKeys:")
# By default a for loop on a dictionary will loop through all the keys in the dictionary
for key in my_age_dictionary:
    print(key)

print("\nValues:")
# we can use indexing to access the values in our loop
for key in my_age_dictionary:
    print(my_age_dictionary[key])

print("\nValues again:")
# we could also use the values function to loop through the values directly:
for value in my_age_dictionary.values():
    print(value)

# ----------------------------------------------------------------------
# Challenge 2
# ------------
#
# a) create a dictionary to hold 3 answers to the multiple choice question
#    below. Use 'a', 'b' and 'c' as the keys and your answers as the values.
#
# b) print your whole list to the console and then just the 'b' answer on
#    it's own.
# ----------------------------------------------------------------------

question = "What is the best video game of all time?"
