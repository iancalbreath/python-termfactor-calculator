# Ian Calbreath
# Mac Littlefield's Class
# Midterm Calculation Program

# a.k.a. TERMIAL and FACTORIAL Calculator

# Create getNum
#   - receives no input
#   - prompts user to enter integer
#   - uses a while loop to validate
#   - ensures number is not negative or zero
#   - returns the result

def getNum():
    userint = input("Enter an integer greater than 1: ")   
    while int(userint) <= 1:
        print("You must use a number that is greater than 1.")
        userint = input("Enter an integer: ")
    return int(userint)

# Create calcSum
# calculate what is essentially the termial of user's input with a loop

def calcSum(number):
    total = 0.0
    for num in range(1, number + 1):
        total += num
    return total



# Create calcProd
# calculate factorial of user's input with loop


def calcProd(number):
    total = 1
    for num in range(1, number + 1):
        total *= num
    return total

    

# Create main()
#   - prompt for S or P - sum or product
#   - if valid input, use getNum to prompt for number
#   - call calcSum or calcProd on the user's input and display the result

def main():
    print("Welcome to Ian's Accumulated Sum and Product Calculator.")
    try_again = 'y'
    while try_again == 'y':
        sp = input('If you want a sum, enter S.  If you want a product, enter P.: ')
        
        while sp != 's' and sp != 'S' and sp != 'p' and sp != 'P':
            sp = input("Only enter S or P: ")
        usrnum = getNum()
        if sp == 's' or sp == 'S':
            result = calcSum(int(usrnum))
            result = int(result)
            print(f"The accumulated sum of numbers 1 to {usrnum} is {result:,d}.")
        elif sp == 'p' or sp == 'P':
            result = calcProd(int(usrnum))
            result = int(result)
            print(f"The accumulated sum of numbers 1 to {usrnum} is {result:,d}.")
        else:
            sp = input('Only enter S or P: ')
        try_again = input('Do you want to try another number? (y/n): ')
        if try_again != 'y':
            print("Thanks for using my calculator. Bye.")
            break
main()
