# version1 = input("enter the version")
# version2 = input("enter the version")
# print(version1)
# print(version2)
# if version1 < version2:
#     print("It is Upgarded")
# elif version1 == version2:
#     print("It is equal") 
# else:
#     print("It is Downgraded")


# def has_same_digits(n1, n2):
#     return sorted(str(n1)) == sorted(str(n2))

# def find_smallest_integer():
#     x = 1
#     while True:
#         if all(has_same_digits(x, x * i) for i in range(2, 8)):
#             return x
#         x += 1

# if __name__ == "__main__":
#     smallest_integer = find_smallest_integer()
#     print("The smallest positive integer x is:", smallest_integer)
#     print("i.e.,", smallest_integer, "*", "2 =", smallest_integer * 2)
#     print(smallest_integer, "*", "3 =", smallest_integer * 3)
#     print(smallest_integer, "*", "4 =", smallest_integer * 4)
#     print(smallest_integer, "*", "5 =", smallest_integer * 5)
#     print(smallest_integer, "*", "6 =", smallest_integer * 6)


# def calculate_flames(name1, name2):
#     # Convert names to lowercase and remove spaces
#     name1 = name1.lower().replace(" ", "")
#     name2 = name2.lower().replace(" ", "")

#     # Count the number of unique characters in both names
#     unique_chars_name1 = set(name1)
#     unique_chars_name2 = set(name2)

#     # Calculate the total count of unique characters
#     total_unique_chars = len(unique_chars_name1.union(unique_chars_name2))

#     # Calculate the count of common characters
#     common_chars = len(unique_chars_name1.intersection(unique_chars_name2))

#     # Calculate the flames count
#     flames_count = total_unique_chars - common_chars

#     # Define FLAMES dictionary
#     flames_dict = {
#         0: "Friendship",
#         1: "Love",
#         2: "Affection",
#         3: "Marriage",
#         4: "Enemy",
#         5: "Sibling"
#     }

#     # Find the result
#     result = flames_dict[flames_count % 6]

#     return result

# if __name__ == "__main__":
#     name1 = input("Enter the first name: ")
#     name2 = input("Enter the second name: ")
#     result = calculate_flames(name1, name2)
#     print("Result of FLAMES game between", name1, "and", name2, "is:", result)




