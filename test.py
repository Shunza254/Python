# # Write a program that accepts user input to create a list of integers. 
# # Then, compute the sum of all the integers in the list.

# numbers = input("Input numbers separated by spaces: ")
# # Convert input from string to int
# numbers_list = [int(num) for num in numbers.split()]
# # Total all numbers inputted
# total_sum = sum(numbers_list)
# # Print total
# print("Total sum is: ", total_sum)

# # Create a tuple containing the names of five of your favorite books. 
# # Then, use a for loop to print each book name on a separate line.
# favorite_books = ("River & the Source", "Rich Dad Poor Dad")
# # for loop to print the names on a separate line
# for fav in favorite_books:
#     print(fav)

# print(type(favorite_books))

    # Write a program that uses a dictionary to store information about a person,such as their name, age, 
    # and favorite color. Ask the user for input and store the information in the dictionary. 
    # Then, print the dictionary to the console.


# Declare an empty dictionary
info = {}

# Create a keys dictionary with the keys needed
keys = {"Name", "Age", "Favorite color"}

for key in keys:
    value = input(f"{key}: ")
    info[key] = value

print("Here is your information: ", info)
