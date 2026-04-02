# 16. Find second largest number
# numbers = [5, 8, 2, 9, 1, 7]
# first = 9
# second = 8

# for num in numbers:
#     if num > first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         second = num

# print(second)  



# 17. Merge two lists
# list1 = [1,2,3,4,5,6]
# list2 = [2,3,4,5,6,6]
# print(list1+list2)



# 18. Find common elements in two lists
# list1 = [12, 34, 35, 56, 67]
# list2 = [12, 22, 33, 67, 34]
# common = []
# for item in list1:
#     if item in list2:
#         common.append(item)

# print(common)



# 19. Sort a list without using sort()
# x = [11,23,45,6,8,0]
# x=["green", "red", "blue","green"]
# n = len(x) #value of n ===6
# for i in range(n-1):   #range start from 0 ..........so range goes to n-1
#     for j in range(n-i-1):
#         if x[j] > x[j+1]:
#             temp =x[j]
#             x[j]=x[j+1]
#             x[j+1]=temp

#         j+=1
#     i+=1
# print (x)




# 20. Move all zeros to end
# def move_zeros(arr):
#     j = 0  

#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[j], arr[i] = arr[i], arr[j]
#             j += 1

#     return arr

# print(move_zeros([0, 1, 0, 3, 12]))




#   Pattern Questions
# rows = int(input("Enter rows : "))
# for i in range(1,rows + 1):
#     for j in range(i):
#         print("*",end = "")
#     print()



# rows = 4 
# for i in range(4, 0, -1):
#     print(i * "*")
   


#Question pattern
#    *
#   ***
#  *****
# ******* 
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()



<<<<<<< HEAD

# 24. Count frequency of each character



text = (input("Enter text : "))
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)



# 25. Find first non-repeating character

=======
>>>>>>> d461ac5c225a74e61a5546fcb591b36c4fff5a84
# 26. Count words in a sentence
# sentence = "learning python & practicing python"
# words = sentence.split()
# wordcount = len(words)
# print(f"The sentence has {wordcount} words.")
