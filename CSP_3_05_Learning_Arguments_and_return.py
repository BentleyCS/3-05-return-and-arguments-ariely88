

#Below you will find several older homework questions done correctly using input
#and print statements. our task is to take each one and convert it to
# arguments and returns instead.


#modify the below function such that it asks the user for 2 numbers as input.
#Then have it print out the larger number
def larger(a, b):
    if a>b:
        return a
    else:
        return b

#Modify the below function such that it asks for the users score as an input.
#Then based on the score print out a letter grade.
# 90+ A
# 80+ B
# 70+ C
# 60+ D
# 59- F
def grade(score):

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

#Modify the below function such that it asks the user for a number then
#if the number is divisible by 3 print "fizz"
#if the number is divisible by 5 print "buzz"
#if both are the case then print "FizzBuzz" instead of the prior two
#if niether are the case print the number.
def fizzBuzz(n):
    if n%5==0 and n%3==0:
        return 'FizzBuzz'
    elif n%3==0:
        return 'fizz'
    elif n%5==0:
        return 'buzz'
    else:
        return n

#modify the below function such that it asks the user for an input number.
#if the number is even divide it by two.
#if the number is odd multiply it by 3 and add 1
#then print the new number.
def collatz(n):
    if n==1:
        return n
    if n%2==0:
        return n/2
    else:
        return 3*n+1





#Modify the below function such that it asks the user for a temperature.
#The format for temperature should end in F For Fahrenheit and C for Celcius
#Then given the temperature if it is in Fahrenheit convert it to Celsius on vice versa
#Example 32F -> 0C  20C -> 68F
def convertTemperature(temp):

    value = int(temp[:-1])
    unit = temp[-1].upper()
    if unit == 'C':
        out = value*(9/5)+32
        out = str(int(out))+ "F"
        return out
    elif unit == 'F':
        out = (value-32)*5/9
        out = str(int(out)) +"C"
        return out
    else:
        return "invalid"
if __name__ == "__main__":
    print ("Temperature conversion", convertTemperature("42C"))
    print ("larger of 6 and 7: ", larger(6, 7))
    print ("grade: ", grade(89))
    print ("fizzBuzz: ", fizzBuzz(89))
    print ("collatz: ", collatz(89))


