# Algorithm Design and Analysis Work (About Sorting Algorithms);

# Sorting Algorithms -> These are a set of instructions that take an array or list as input and arrange the items in a specific order;

# In this program we are using the sorting algorithm 'Selection-Sort';


amount = int(input('Enter how many indexes you want: '))
list = []

while len(list) < amount:
    add = int(input('Enter a number: '))
    list.append(add)
    
print(list)

# Note: row = i and column = j 

for i in range(len(list)):
    smaller = i

    for j in range(i + 1 ,len(list)):
        if list[j] <= list[smaller]:
                smaller = j

    if list[i] != list[smaller]:
            aux = list[i]
            list[i] = list[smaller]
            list[smaller] = aux

print(list)
    

