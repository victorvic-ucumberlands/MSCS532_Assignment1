#This script sorts data in decreasing order, based on the insertion sort algorithm
data_input = [1,2,3,900,5,6,7,8,9,10,300,11,12,13,14,15,16,0,17,18,19,20]
print("Data input: ", data_input)
for i in range(1, len(data_input)):
    key = data_input[i]
    j = i - 1
    while j >= 0 and data_input[j] < key  :
        data_input[j + 1] = data_input[j]
        j -= 1
    data_input[j + 1] = key
print ("Sorted data in decreasing order: ", data_input)
