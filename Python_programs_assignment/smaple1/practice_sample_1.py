import random
#1.Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
def exchange_numbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

#2.Python Program to Check Whether a Number is Positive or Negative.
def isPositive (num):
	if(num>0):
		return True
	elif(num<0):
		return False
	else:
		return None
  
 # 3.Python Program to Print all Numbers in a Range Divisible by a Given Number. 
 # [ ifrange is from 1 to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ]
def checkDivisor(n,k):
  a=[]
  for i in range(1,n+1):
    if(i%k==0):
      a.append(i)
  return a

#4.Python Program to Read Two Numbers and Print Their Quotient and Remainder.
def Divide(a,b):
	q=a/b
	r=a%b
	return q,r

#5.Python Program to Print Odd Numbers Within a Given Range
def oddNumbers(n):
	a=[]
	for i in range(n+1):
		if(i%2!=0):
			a.append(i)
	
	return a

#6.Python Program to Find the Sum of Digits in a Number.
def sumOfDegits(n):
	sum=0
	while(int(n)>0):
		sum=sum+n%10
		n=int(n/10)
	return sum

#7.Python Program to Find the Smallest Divisor of an Integer.
def findSmallestDivisor(n):
	for i in range(2,n):
		if(n%i==0):
			return i
		
#8.Python Program to Read a number n and Compute n+nn+nnn.
def sumOfSeries(n,k):
	sum=0
	digit=n
	while(k>0):
		sum=sum+n
		n=n*10+digit
		k=k-1
	return sum

#9.Python Program to Reverse a Given Number.
def reverse(n):
	reverse=0
	while(int(n)>0):
		reverse=reverse*10+n%10
		n=int(n/10)
	return reverse

#10.Python Program to Calculate the Average of Numbers in a Given List.
def average(a):
	sum=0
	for i in range(len(a)):
		sum=sum+a[i]
		average=sum/len(a)
	return average

#11.Python Program to Count the Number of Digits in a Number.
def count(n):
	c=0
	while(int(n)>0):
		c=c+1
		#print(c)
		n=int(n/10)
	return c

#12.Python Program to Check if a Number is a Palindrome.
def palindrome(n):
	number=n
	reverse=0
	while(n>0):
		reverse=reverse*10+n%10
		n=int(n/10)
	return (reverse==number)

#13.Python Program to print the number of occurrence of a sub string in a given string.
def ifSubStringFound(a,b):
	c=0
	for i in range(len(a)):
		if(a[i:i+len(b)]==b):
			c=c+1
	return c

#14.Python program to print the lowest index in the string where substringsubis found within the string.
def indexSubStringFound(a,b):
	for i in range(len(a)-len(b)+1):
		if(a[i:i+len(b)]==b):
			break
	return i

#15.Python Program to return true if all characters in the string are alphabetic and there is at least one other character, False.
def checkForCharacters(a):
	for i in range(len(a)):
		f=0
		if(96<ord(a[i])<123 or 64<ord(a[i])<92):
			f=0
		else:
			f=1
			break
	if(f==1):
		return False
	else:
		return True
	
#16.Python Program to Replace all Occurrences of ‘a’ with $ in a String.
def replace(a):
	a_list=list(a)
	for i in range(len(a_list)):
		if(a_list[i]=='a'):
			a_list[i]='$'
	return ''.join(a_list)

#17.Python Program to Count the Number of Vowels in a String.
def countVowels(n):
	c=0
	for i in range(len(n)):
		if(n[i] in ['a','e','i','o','u','A','E','I','O','U']):
			c+=1
	return c

#18.Python Program to Take in a String and Replace Every Blank Space with Hyphen.
def replaceBlankSpace(a):
	a_list=list(a)
	for i in range(len(a_list)):
		if(a_list[i]==' '):
			a_list[i]='-'
	return ''.join(a_list)

#19.Python Program to find the length of string without using any built-in functions.
def findLength(a):
	if(a==''):
		return 0
	else:
		return 1+findLength(a[1:])
	
#20.Python Program to Take in Two Strings and Display the Larger Stringwithout Using Built-in Functions.
def findLargerString(a,b):
	n=findLength(a)
	m=findLength(b)
	if(n>m):
		return a
	elif(m>n):
		return b
	else:
		return "Equal"
	
#21.Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.
def countOfUpperLower(a):
	n=0
	l=0
	for i in range(len(a)):
		if(64<ord(a[i])<91):
			n+=1
		elif(96<ord(a[i])<123):
			l+=1
		else:
			"Nothing"
	return n,l

#22.Python Program to Calculate the Number of Digits and Letters in a String.
def checkDigitORLetter(b):
	if(64<ord(b)<91 or 96<ord(b)<123):
		return True
	else:
		return False
def countCharsDigits(a):
	c=0
	d=0
	for i in range(len(a)):
		if(checkDigitORLetter(a[i])):
			c+=1
		else:
			d+=1
	return c,d

#23.Python Program to check whether a full pattern (not sub string) is present in the given sentence.
def fullPattern(a,b):
	if(b in a):
		return True
	else:
		return False
	
#24.Cumulative sum of a list [1, 2, 4, ...] is defined as[1, 3, 7, . . .]
# Write a functioncumulative_sum() to compute cumulative sum of a list
def cumulative_Sum(a):
	b=[]
	sum=0
	for i in range(len(a)):
		sum=sum+a[i]
		b.append(sum)
	return b

#25.Write a program to generate 10 random integers.
def tenRandomNumbers():
	a=[]
	for i in range(10):
		a.append(random.random())
	return a

#26.Write a program to generate 10 random integers between 1 to 20 (both inclusive).
def tenRandomNumbersRange():
	a=[]
	for i in range(10):
		a.append(random.randint(1,20))
	return a

#27.Write a program to generate 5 random integers between 1 to 20 such that numbers should be unique.
def uniqueRandomNumbers():
	a=set()
	for i in range(6):
		a.add(random.randint(1,20))
	return a

#28.Write a program to generate 10 random numbers between 1 to 100 
# such that there should one number between 1 to 10 one number between 11 to 20 etc.
a=[]
def randomNumbers():
	n=1
	while(n<101):
		a.append(random.randint(n,n+10))
		n=n+10
	return a




