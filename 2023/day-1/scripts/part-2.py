import re;

puzzleInput = open("advent-of-code/2023/day-1/puzzle-input", "r");
#puzzleInput = open("advent-of-code/2023/day-1/test-input", "r");

def solution():
    n = puzzleInput.readline();
    n = n.replace("one", "o1ne");
    n = n.replace("two", "tw2o");
    n = n.replace("three", "thr3ee");
    n = n.replace("four", "fo4ur");
    n = n.replace("five", "fi5ve");
    n = n.replace("six", "si6x");
    n = n.replace("seven", "sev7en");
    n = n.replace("eight", "ei8ght");
    n = n.replace("nine", "ni9ne");
    b = ("".join(re.findall("[0-9]+", n)));
    a = "";
    a += b[0];
    a += b[-1];
    return(int(a));

n = 0;
for i in range(0, 1000):
    n += solution();
    print(n);