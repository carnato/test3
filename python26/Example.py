import sys 
# import array as arr

# For getting input from input.txt file 
sys.stdin = open('input.txt', 'r')  
  
# Printing the Output to output.txt file 
sys.stdout = open('output.txt', 'w') 
# def main():
#     marks = [12,34.2,67.45,65.89,"Khushi","Uttam"]
#     marks[4]="Vishal"
#     print(marks)
#     """List is mutable"""
#     # list method
# Array is collection of same data type that store the data in same contiguous memory location

def main():
    """creating array of integer"""
    # a=arr.array('i',[1,2,3])
    # print(a[0])
    # a.append(6)
    # print(a)
    # var1=45
    # # float function always take a integer value never take a float value
    # for i in range(2,45,2):
    #     print(i)
    # fruits=arr.array('i',[8,7,6,5,4,4,4,3,3])
    # for i in range(len(fruits)):
    #     print(fruits[i])
    # there are some function of array like insert(),append,remove,pop,index
    # var2=arr.array('i',[6,5,4,3,2])
    # for j in range(0,5):
    #     print(var2[j],end="  ")
    # print("Array value before the insertion of new element",*var2)
    # var2.insert(2,12)
    # print("Modifieed array",*var2)
    # print(var2[3])
    # var3=arr.array('f',[1.2,2.1,3.9,9.1])
    # print(var3[3])
   
    # List of integer
    # a=[6,5,4,3,2,8]
    # b=["Vishal","Uttam","Sudeep","Veeresh"]
    # c=[5,3.56,"Vishal","Uttam","Sudeep","Veeresh",4.5,6,7]
    # print(a)
    # print(b)
    # print(c)
    # how to print single list in n times
    # d=[2]*4
    # g=["Vishal"]*5
    # print(d)
    # print(g)
    # insert(): This will be used to insert the number at particular index
    # append(): Add the element at the end of list.
    #  extend(): Add the mltiple element at the end of list
    # Example
    # creating the empty list
    # a=[]
    # a.append(2)
    # print(a[0])
    # a.insert(4,34)
    # print(a[1])
    # a.extend([23,45,67,32,24])
    # print(a)
    a=[21,12,93,63,35,36]
    var1=[b for a,b in enumerate(a) if a % 2 == 0 or b % 2 == 0]
    print(var1)
    # length of list
    # var=len(a)
    # print(var)
    # # find the max value in the given list
    # # print(max(a))
    # # Native approach find max withot using max function
    # max1=0
    # # In this for loop passing the array and i assign the array
    # for i in a:
        
    #     if i>max1:
    #         max1=i
    # print(max1) 
    # max1=0
    # #  in this situation size of length assign to the i 
    # for i in range(len(a)):
    #     if a[i]>max1:
    #         max1=a[i]
    # print(max1)            

# Yo are given a list with 10 random number using list comprension create a new list
#  using the old list and add only those number that are either even or at even indexes
    # a=[1,2,3,43,5,6]
    # add=0
    # for i in range(len(a)):
    #     if a[i]%2==0 or i%2==0:
    #         add=add+a[i]
    #     # if i%2==0:
    #     #     add=add+a[i]
    # print(add)     
    # Introduction to List Comprehension
    # names=['John','James','Emmy','Micheal','Jimmy']
    # You need to create a new list with starting 'J'
    # j_names=[]
    # for name in names:
    #     if 'J' in name:
    #         j_names.append(name)
    # print(j_names)   
    # Syntex of List Comprehension
    # list=[expression for item in iterable if condition ==True]
    # j_names=[name for name in names if 'J' in name]
    # print(j_names)
    # # Copy of the element of list into new list
    # list1=[99,88,77,66,55,44,33,22,11]
    # list2=[var for var in list1]
    # print(list2)
    animals=['Lion','tiger','monkey','elephant','frog']
    filter_animals=[]
    for animal in animals:
        filter_animals.append(animal.title( ))
                 

    























    


if __name__ == '__main__':
    main()