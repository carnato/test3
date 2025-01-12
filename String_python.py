
import sys 
# import array as arr

# For getting input from input.txt file 
sys.stdin = open('input.txt', 'r')  
  
# Printing the Output to output.txt file 
sys.stdout = open('output.txt', 'w') 
# A string is a seqence of characters
# Can be enclosed in a single or double quotes
# this multiline string
# statements ="""Hello World
# HE is a MAN"""
# print(statements)
# Accessing indivisal character in a string 
# statement1='HELLO'
# print(statement1[-1])
# Slicing in the string 
# print(statement1[0:3])
# String Operator
# String Concatenare Operater
# statement2='a'+'b'+'c'+'d'+'e'
# print(statement2)
# X='I '
# Y='am '
# Z='Vishal Yadav'
# print(X+Y+Z)
# print(2*"Vishal")
# String Comparison Operator
# Compare twostring at a time.
# ASCII value of A=65,a=97
# Return input from user as a string.
number=int(input("Enter the number if element:" ))
number1=[]
for i in range(number):
    x=int(input())
    number1.append(x)

print(number1)    

