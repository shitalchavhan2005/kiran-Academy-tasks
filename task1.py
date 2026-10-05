# print("Hello World")
# cost_price = float(input("Enter the cost price: "))
# selliing_price = float(input("Enter the selling price: "))
# profit=selliing_price-cost_price
# print(profit)
# loss=cost_price-selliing_price
# print(loss)


# num=eval(input("Enter a number : "))
# if num %2==0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# age=eval(input("Enter Your age:"))

# if age>=18:
#     print("You are eligible for vote")
# else:
#     print("You are not eligible for vote")

str1=input("Enter a string: ")
str2=input("Enter another string: ")
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()
if sorted(str1) == sorted(str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")