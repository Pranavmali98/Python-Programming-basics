#Starting personal information manager
print("=" * 50)
print("Personal information manager interface")
print("=" * 50)

#variables declared statically inside the program and initialized
name = "Pranav Mali"
age = 20
city = "Yeola"
hobby = "Travelling"

#Taking input for favorite color from the user
fav_color = input("Enter your favorite color: ")
while fav_color == "":                  #validating that user must input a valid string
    print("-" * 50)
    print("Invalid input, please enter again: ")
    print("-" * 50)
    fav_color = input("Enter your favorite color: ")

#Taking input for favorite food from the user
fav_food = input("Enter your favorite food: ")
while fav_food == "":                   #validating that user must input a valid string
    print("-" * 50)
    print("Invalid input, please enter again: ")
    print("-" * 50)
    fav_food = input("Enter your favorite color: ")

#displaying the user data into a structured format using formating string
print("=" * 50)
print("Your information: ")
print("-" * 50)
print(f"Your name is {name} and age {age},\nyou live in {city}. you love {hobby}.\nYour favorite color is {fav_color},\nand you love to eat {fav_food}")
print("=" * 50)

#greeting and thanking the user for using the personal information manager
print("=" * 50)
print("Thank you for using personal information manager...")
print("=" * 50)