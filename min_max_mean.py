list = []
num = int(input("How many numbers: "))
for n in range(num):
    numbers = int(input("Enter number "))
    list.append(numbers)
print("Maximum element in the list is :", max(list))
print("\n Minimum element in the list is :", min(list))
add=sum(list)
mean=add/len(list)
print("Mean is: ", mean)