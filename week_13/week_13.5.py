FibSequence = [1, 1] #start of the fib seqnce; input numer 
number = int(input("input a number: "))
i = 0

while i != number: # gowing threu the array and adding numbers to the fib sequence
    FibSequence.append(FibSequence[i] + FibSequence[i+1])
    i += 1

print(FibSequence) # prining the fib sequense