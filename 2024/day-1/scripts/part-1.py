#take number from line before the 3 spaces and append to lists
#next line and repreat until done
#make seoncd list doing the same thing but with the numbers after the 3 spaces
#sort lists
#find the difference between each element pair
#sum all differences

puzzleInput = open("../puzzle-input", "r");

list1 = [];
list2 = [];

for i in range(len(puzzleInput.readlines())):
    line = puzzleInput.readline(i);
    list1.append(line.strip().split()[0]);
    list2.append(line.strip().split()[1]);

print(list1);
print(list2);
