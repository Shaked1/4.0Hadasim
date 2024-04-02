##import math

def twitter_towers():

    while True:

        user_choice = int(input("Hello,\n For a rectangular tower press 1 \n for a triangular tower press 2 \n To exit press 3: "))

        if user_choice == 3:
            print("Goodbye.")
            break



        ## rectangular tower
        if user_choice == 1:
            width = int(input("Please insert a width: "))
            height = int(input("Please enter a height greater than or equal to 2: "))
            if width == height or abs((height - width))> 5:
                print("The area of a rectangular tower is: ", width * height) ## Area calculation
            else:
                print("The perimeter of the rectangular tower is: ", (width + height) * 2) ##Scope calculation


        ## triangular tower
        elif user_choice == 2:
            width = int(input("Please insert a width: "))
            height = int(input("Please enter a height greater than or equal to 2: "))
            user_choice2 = int(input("Calculate the perimeter of the triangle press 1 \nFor the triangle print press 2:"))
            if user_choice2 == 1:
                print("Triangular tower perimeter: ",height * 2 + width) ##perimeter of the triangle
            elif user_choice2 == 2:
                if width % 2 == 0 or width > height * 2:
                    print("The triangle cannot be printed.")
                else:
                    print_triangle(width, height)

        else: ## Other option
            print("Invalid choice, Please press again.\n")

def print_triangle(width, height):
    odd_numbers = []

    for num in range(2, width):
        if num % 2 != 0:
            odd_numbers.append((num, 0))

    if odd_numbers:
        middle_rows_number = (height-2) // len(odd_numbers)
        for i in range(len(odd_numbers)):
            odd_numbers[i] = (odd_numbers[i][0], middle_rows_number)

        if (height-2) % len(odd_numbers) != 0:
            odd_numbers[0] = (odd_numbers[0][1], middle_rows_number + 1)
    else:
        odd_numbers.append((1, height-2))

    print(" " * (width // 2 - 1), "*")

    for odd_number in odd_numbers:
        for i in range(odd_number[1]):
            print(" " * ((width-odd_number[0])//2 - 1), "*" * odd_number[0])

    print("*" * width)

if __name__ == '__main__':
    twitter_towers()
