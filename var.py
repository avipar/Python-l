"""#var="avinash"
#print(var)
var=22
print(var)
num=22
print(var,id(num))
g=9.8
print(type(g))
print(isinstance(g,float))
m1=man()
print(isinstance(m1,man))
a=b=c=d=30
print(a,b,c,d)
a,b,c,d=1,2,3,4
print(a,b,c,d)

a=2
if a==2:
    var="avinash"
    print("var=2")
    print(var)"""
#input two numbers and perform all arthematic operations

"""a = int(input("Enter the first number: "));
b = int(input("Enter the second number: "));

c = a+b;
d = (a-b)*(-1);
e = a/b;
f = a*b;
g = a%b;

print("Addition of the two numbers are: ", c);
print("Multiplication of the two numbers are: ", f);
print("Subtraction of the two numbers are: ", d);
print("Division of the two numbers are: ", e);
print("Modulus value of the two numbers are: ", g);"""

"""a=5;
b=15;
print("a=",a, "b=",b);
print("division of two numbers are",int(b/a));
print("multiplication of these two are",int(b*a));
print("addition of these two are",int(b+a));
print("subtraction of these two are",int(b-a));
print("modulus of these two are",int(a%b));"""

"""a=6;
b=9;
x=b/a;
y=b*a;
z=b+a;
h=b-a;
print("a=",a,"b=",b);
print("addition of these two numbers are",z);
print("division of these two numbers are",int(x));
print("multiplication of these two numbers are",y);
print("substraction of these two numbers are",h);"""

"""maths=77;
science=99;
sst=79;
it=99;
english=89;

total=maths+science+sst+it+english;
percentage=total/500*100;
avg=total/5;
print(int(total));
print(float(percentage));
print(int(avg));"""

"""x=5;
y=10;
a=x/100;
b=y/100;
c=x/1000;
d=y/1000;
print((x,y),"cm");
print("we have to change it in meter",a,"m",b,"m");
print('we have to change in km',c,"km",d,"km");

x=6;
y=68;
a=x/y;
b=x*y;
print("value of div is",int(a));
print("value of mul is",int(b));

a=110
b=55
if a==55:
    print("ok")
else:
    print("not ok")


def my_function():
    print("hell world")

my_function()


def my_class(section):
    print(section + "a")

my_class('601')

def university(firstname, lastname):
    print(firstname + lastname)

university("chandigarh", "university")


def universities(bestuniversity):
    print("one of the best universities is"+ bestuniversity)
universities("chandigarh university")


def name(gotra):
    print("my gotra is" + gotra)
name("parashar")


def arb_arg(statement1,statement2,statement3):
    print("let we see which no get executed"+ statement1)
arb_arg(statement1="my name is avinash", statement2="my friend name is harsh", statement3="my x name is vhvf")

def arb_arg(*statement):
    print("let we see which no get executed"+ statement[2])

arb_arg("my name is avinash","my friend name is harsh","my x name is thor")

n=44;
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if (temp==rev):
    print("the number is palindrome")
else:
    print("the number is not palindrome")

n = 370
s = 0
t = n
while t > 0:
   digit=t%10
   s += digit**3
   t= t//10
if n == s:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")



a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))


if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

print(largest, "is the largest of three numbers.")
 

myString = "i_am_String"
print(myString)
print(type(myString))

# ! swapcase()
print(myString.swapcase())
# ! isalnum()
print(myString.isalnum())
# ! lower()
print(myString.lower())      
# ! slicing
print(myString[2:5])
# ! reverse string
print(myString[::-1])





age=int(input('enter your age: '))
gender=str(input('enter your gender: '))
if (age<65 and gender=='male' ):
    print('you are eligible to pay the taxes')
elif (age>65 and gender=='female'):
    print('you are not able to pay the taxes/Wrong category')
elif (age<65 and gender=='female'):
    print('you are not able to pay the taxes/Wrong category')
elif (age>65 and gender=='male'):
    print('you are not able to pay the taxes/Wrong category')
else:
    print('you are able to pay the tax')


if (age<65 and gender=='male'):
    print("the income tax is as follows")
else:
    print('wrong category')
T=int(input('enter the amount: '))
if (T<160000):
    print('nill')
elif (T>160000 and T<=500000):
    tax=(T-160000)*10/100
    print("payable tax is",tax)
elif (T>500000 and T<=800000):
    tax=(T-500000) * 20/100 +34000
    print("payable tax is",tax)
else:
    tax=(T-800000)* 30/100 + 94000
    print("payable tax is",tax)




num = int(input('enter the number: '))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a composite number")
else:
    print(num, "is a prime number")


def palindrome(a):

  mid = (len(a)-1)//2    

  start = 0        

  last = len(a)-1

  flag = 0

  while(start <= mid):

    if (a[start]== a[last]):

       

      start += 1

      last -= 1

       

    else:

      flag = 1

      break;

  if flag == 0:

    print("The entered string is palindrome")

  else:

    print("The entered string is not palindrome")



def symmetry(a):

   

  n = len(a)

  flag = 0

   

  if n%2:

    mid = n//2 +1

  else:

    mid = n//2

     

  start1 = 0

  start2 = mid

   

  while(start1 < mid and start2 < n):

     

    if (a[start1]== a[start2]):

      start1 = start1 + 1

      start2 = start2 + 1

    else:

      flag = 1

      break

  if flag == 0:

    print("The entered string is symmetrical")

  else:

    print("The entered string is not symmetrical")

     

string = 'amaama'

palindrome(string)

symmetry(string)


def UncommonWords(A, B):

  count = {}

  for word in A.split():

    count[word] = count.get(word, 0) + 1

  for word in B.split():

    count[word] = count.get(word, 0) + 1

  return [word for word in count if count[word] == 1]

A = "Geeks for Geeks"

B = "UNCOMMON WORD"

print(UncommonWords(A, B))"""


def add_string(str1):

 length = len(str1)



 if length > 2:

  if str1[-3:] == 'ing':

   str1 += 'ly'

  else:

   str1 += 'ing'



 return str1

print(add_string('ab'))

print(add_string('abc'))

print(add_string('string'))


    










    
