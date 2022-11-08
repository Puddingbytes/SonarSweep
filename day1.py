with open("day1.txt") as fin:
    data = [int(i) for i in fin.read().strip().split("\n")] #contantanating read,strip and splitting the data by line break

def first():
    result = [num1 < num2 for num1, num2 in zip(data, data[1:])]    #using the zip function and my condition returns the true values in sum result
   
    return sum(result)

def second():
    allSums = [sum(someTuple) for someTuple in zip(data, data[1:], data[2:])] #campares the tuple sums given by the zip function using my condition
    result = [num1 < num2 for num1, num2 in zip(allSums, allSums[1:])] #sums up the true values in my list
    return sum(result)

    
    
    
print("first answer: ", first())
print("second answer: ", second())
    
