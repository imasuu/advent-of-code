import re;

puzzleInput = open("advent-of-code/2023/day-1/puzzle-input", "r");

def solution():
    n = ("".join(re.findall("[0-9]+", puzzleInput.readline())));
    return(int(n[0] + n[-1]));

n = 0;
for i in range(0, 1000):
    n += solution();
    print(n);