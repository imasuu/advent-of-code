puzzleInput = open("../puzzle-input", "r");

list1 = [];
list2 = [];

for i in range(1000):
    line = puzzleInput.readline().strip().split();
    list1.append(int(line[0]));
    list2.append(int(line[1]));

list1.sort();
list2.sort();

total = 0;
for i in range(len(list1)):
    diff = list1[i]*list2.count(list1[i]);
    total += diff;

print(total);
