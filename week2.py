#my week 2 assignment
# This file contains the code for the week 2 assignment
#create an empty list
my_list = []    

#append multiple elements to the list   
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


#insert an element in the list at the second position
my_list.insert(1, 15)

#extend the list with another list
my_list.extend([50, 60, 70])

#remove the last element from the list
my_list.pop()

#sorting the list
my_list.sort ()

#find and print index of the element 30
index_of_30 = my_list.index(30)
print(f"Index of 30:", index_of_30)

#print the final list 
print("my final list:", my_list)



