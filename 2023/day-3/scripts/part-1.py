import re;

puzzleInput = open("advent-of-code/2023/day-3/puzzle-input", "r");
#puzzleInput = open("advent-of-code/2023/day-3/test-input", "r");

#distance in characters until under or above current character (from the right of it): 142

def Check():
    global line;
    line = puzzleInput.readline();
    return("".join(re.findall(re.compile(r"\*\+#/@-\$=%&"), line)));

for i in range(0, 140):
    print(Check());