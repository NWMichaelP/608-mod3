import statistics

print("Do you want the boring version, yes (y) or no (b)?")

answer = input()

if answer == 'y':
    #Defining Data, I couldn't get >>if answer == 'Y' or 'y':<< to work
    data = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

    print(round(statistics.pvariance(data),2))
    print(round(statistics.pstdev(data),2))
elif answer == 'n':
# n1,n2,n3,n4,n5,n6,n7,n8,n9,n10 = input("Enter 10 numbers, seperated by a space: ").split()
#I tried REALLY hard to get this to work, but ultimately, I gave up. I'm going to take a nap now.     

    n1  = int(input("Number 01:"))
    n2  = int(input("Number 02:"))
    n3  = int(input("Number 03:"))
    n4  = int(input("Number 04:"))
    n5  = int(input("Number 05:"))
    n6  = int(input("Number 06:"))
    n7  = int(input("Number 07:"))
    n8  = int(input("Number 08:"))
    n9  = int(input("Number 09:"))
    n10 = int(input("Number 10:"))

    data = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
    
    print(round(statistics.pvariance(data),2))
    print(round(statistics.pstdev(data),2))

print('\nCode by Michael "I have been defeated" Pogue')