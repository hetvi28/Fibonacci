lowNum=-50
highNum=60
mainlist=[]
listPos=[]

#Making the main list with integers starting from lowNum and upto HighNum
for item in range(lowNum, highNum+1):
   mainlist.append(item)

print("In the given range from ", lowNum, " to", highNum, " :")
print("\nThe Main List :")
print(mainlist)

#dividing the main list into negatives and positives 
for item in mainlist:
   if (item > 0): 
      listPos.append(item)
            
print("\nThe Negative Elements in the Range :")
print(listPos)