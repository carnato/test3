# Below is Python code for input/output 
  
import sys 
# For getting input from input.txt file 
sys.stdin = open('input.txt', 'r')  
  
# Printing the Output to output.txt file 
sys.stdout = open('output.txt', 'w') 


s=["Vishal","Ashok","Manju"]
for i in s:
    print(i)
##########################################
s1="Vishal"
for i in s1:
    print(i)
    
    ###############################################
    #Using range in for loop
    for i in range(0,5,1):
        for j in range(0,i,1):
            print("*"),
        print("\n")    
