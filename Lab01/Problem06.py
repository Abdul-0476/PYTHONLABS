number=int(input("Enter number:"))
if number > 1:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    for i in range(2, (number // 2) + 1):


        if (number % i) == 0:
            print(number, "is not a prime number")
            break


    else:
        print(number, "is a prime number")
        print("Its factorial :",factorial)
else:
    print(number, "is not a prime number")