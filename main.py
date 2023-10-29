# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def LeapYear():
    # Use a breakpoint in the code line below to debug your script.
    a = int(input("Enter the Year"))
    if a%4==0:
        if a%100==0:
            if a%400==0:
                print("The Year is a Leap Year ")
            else:
                print("The year is not a leap Year")
        else:
            print("The Year is a Leap Year")
    else:
        print("The Year is not a leap Year")


def oddNum(n):
    i = 1
    print(n)
    while(i<=n):
        print(i)
        i+=2




def factorial(n):
    i = 2
    f = 1
    while(i<=n):
        f *=i
        i+=1
    print(f)




def oddNUM():
    x = int(input("Enter N: "))
    a = 1
    for i in range(1,x+1):
        print(a)
        a+=2





def sumDigts():
    n = int(input("Enter n: "))
    sum = 0
    while n!=0:
        sum+=n%10
        n//=10

    print(sum)



def reverse2():
    n = int(input("Enter n: "))
    number = n
    reversed_number = 0
    while n > 0:
        remainder = n % 10
        reversed_number = (reversed_number * 10) + remainder
        n = n // 10

    print(reversed_number)

def pallindrome():
    n = int(input("Enter any number: "))
    number = n
    reversed_number = 0
    while n > 0:
        remainder = n % 10
        reversed_number = (reversed_number * 10) + remainder
        n = n // 10
    if(number==reversed_number):
        print("Number is a pallindrome")
    else:
        print("Number is not a pallidrome")


pallindrome()



def reverse1():
    n = int(input("Enter n: "))
    x = 0
    y = " ";
    while n<=0:
        y = n%10
        x+=y

    print(x)







# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
