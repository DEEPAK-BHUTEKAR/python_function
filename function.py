

"""
#1. Write a Python function to find the Max of three numbers.
def max_no(a,b,c):
    if a>b and a>c:
        big=a
    elif b>a and b>c:
        big=b
    else:
        big=c

    return big

a,b,c=[int(i) for i in input("Enter the 3 Nos:").split(",") ]
big=max_no(a,b,c)
print("big no among {}, {}, {} is {} ".format(a,b,c,big))

"""

"""
#2. Write a Python function to to perform  sum and mul of all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
def mul_sum(lst):
    sum=0
    mul=1
    for x in lst:
        sum=sum+x
        mul=mul*x

    return sum,mul

lst=[8, 4, -6, 1, 7]
(sum,mul)=mul_sum(lst)
print("sum of elements of the list: ",sum)
print("multiplication of elements of the list: ",mul)
"""
"""
#Write a Python program to reverse a string.
# Sample String :"1234abcd"   Expected Output : "dcba4321"
def rev_str(str):
    str_rev=str[::-1]

    print("reverse string of {} is \n {}".format(str,str_rev))

str="1234abcd"
rev_str(str)

"""
"""
#4. Write a Python function to calculate the factorial of a number (a non-negative integer).
#The function accepts the number as an argument.
def fact(N):
    if (N==0):
        return 1
    else:
        retuen N * fact(N-1)
    
N=int(input("enter the the no: "))
res=fact(N)
print("factorial of {} is {}".format (N,res))
#for i in range(10):
    #print("factorial of {} is {}".format (i,fact(i))


"""
"""
#Q5. Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def uniq_lst(lst):
    x=[]
    for i in lst:
        if i not in x:
            x.append(i)
    return x

lst=[1,2,3,3,3,3,4,5]
x=uniq_lst(lst)
print("unique list of {} is \n {}".format(lst,x))
"""
"""
#9. Write a Python function that takes a number as a parameter and check the number is prime or not
def prime(N):
    for i in range(2,N//2):
        if (N%i)==0:
            print(N,"is non prime no")
            break
    else:
        print(N,"is prime no")

N=int(input("enter the input no: "))
prime(N)
"""
"""
#Q.store the prime no series between 10 to 50 into a list and print that list?
def prime_series(lw,ul):
    s=[]
    for x in range(lw,ul):
        for y in range(2,x):
            if (x==y) or (x%y)==0:
                break
        else:
            s.append(x)
            #print(x,end=", ")
    return s

lw,ul=[int(i) for i in input("Enter the lower and upper limit Nos:").split(",") ]
s=prime_series(lw,ul)
print("prime no series between {} to {} is \n {}".format(lw,ul,s))

"""

"""
#Q.Write a function that calculate monthly TDS by taking annual salary of an employee:
def TDS(asal):
    if asal<=250000:
        atax=0
    elif (asal<1200000):
        atax=asal * 10/100
    elif  (asal<3000000):
        atax=asal * 20/100
    else:
        atax=asal * 30/100
        
    mtax=atax/12
    return atax,mtax
asal=int(input("enter the annual salary ammount="))
atax,mtax=TDS(asal)
print("your yearly TDS is {:.2f} %".format(atax))
print("your monthly TDS{:.2f}=".format(mtax))
"""
"""
#Q.write a function to calculate GCD and LCM of a input No
def find_gcd(a,b):
    if a<b:
        small=a
    else:
        small=b
    for i in range(2,small+1):
        if a%i==0 and b%i==0:
           gcd = i
    return gcd

# Reading numbers from user
N1 = int(input('Enter first number: '))
N2 = int(input('Enter second number: '))

# Function call & displaying output HCF (GCD)
print('HCF or GCD of {} and {} is {}' .format(N1,N2,find_gcd(N1,N2)))

#finding lcm of input nos using formulae: N1*N2=lcm*gcd
lcm=(N1 * N2)/find_gcd(N1,N2)
print ("LCM of {} and {} is {} ".format(N1,N2,lcm))
"""

"""
#Q.write a program for tower of hanoi
def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


# Driver code
n = 4
TowerOfHanoi(n, 'A', 'B', 'C')
# A, C, B are the name of rods
"""
"""
#Q. Python program to check if the number is an Armstrong number or not
#write function for power value of digit
def power(num):
    digit=0
    while(num>0):
        num //= 10
        digit+=1
    return digit
#write function for sum of digits power
def digit_sum(num):
    temp=num
    sum=0
    while(temp>0):
        digit=temp % 10
        sum+=digit ** power(num)
        temp//=10

    return sum
# take input from the user
num = int(input("Enter a number: "))
sum=digit_sum(num)

# display the result
if num ==sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

"""


