#from bdb import Breakpoint

count=0
sum=0
#number = int(input("Enter numbers to calculate their sum and average. Enter 0 to exit: "))

#while number!=0:
 #       sum +=number
  #      count+=1
   #     average=sum//count
    #print("Sum = ",sum ,"Average = ",average)

while True:
    number = int(input("Enter numbers to calculate their sum and average. Enter 0 to exit: "))
    if number==0:
        print("Bye")
        break
    else :
        sum += number
        count+=1
        average=sum//count
        print("Sum = ",sum ,"Average = ",average)
