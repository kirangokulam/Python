print()
list_of_numbers = []
limit = int(input("Enter the number of elements to be added: "))
for i in range(0, limit):
    list_of_numbers.append(int(input("Enter the value {}: ".format(str(i+1)))))
for i in range(0, limit):
    for j in range(i + 1, limit):
        if(list_of_numbers[i]>list_of_numbers[j]):
            list_of_numbers[i],list_of_numbers[j] = list_of_numbers[j],list_of_numbers[i]
print("The sorted list is")
print(list_of_numbers)
