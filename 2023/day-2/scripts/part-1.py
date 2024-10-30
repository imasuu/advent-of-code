import re;

puzzleInput = open("advent-of-code/2023/day-2/puzzle-input", "r");
#puzzleInput = open("advent-of-code/2023/day-2/test-input", "r");

def solution():
    global line;
    line = puzzleInput.readline();

    GetAndCheck();
    if GetAndCheck() == True:
        a = GetID();
    else:
        a = 0;
    return a;

def Convert(string):
    li = list(string.split(" "));
    return li;

def GetAndCheck():
    values = ("".join(re.findall(" [0-9]+", line[line.index(":"):])));
    values = Convert(values[1:]);
    colours = ("".join(re.findall(" red| green| blue", line[line.index(":"):])));
    colours = Convert(colours[1:]);
    result = [];
    for i in range(0, len(values)):
        result.append(values[i] + colours[i]);
    
    matched_indexes = [];
    i = 0;
    length = len(result);
    while i < length:
        if re.match("[0-9]+red", result[i]):
            matched_indexes.append(i);
        i += 1;
    red = [];
    for j in range(0, len(matched_indexes)):
        red.append(result[matched_indexes[j]]);
    
    matched_indexes = [];
    i = 0;
    length = len(result);
    while i < length:
        if re.match("[0-9]+blue", result[i]):
            matched_indexes.append(i);
        i += 1;
    blue = [];
    for j in range(0, len(matched_indexes)):
        blue.append(result[matched_indexes[j]]);
    
    matched_indexes = [];
    i = 0;
    length = len(result);
    while i < length:
        if re.match("[0-9]+green", result[i]):
            matched_indexes.append(i);
        i += 1;
    green = [];
    for j in range(0, len(matched_indexes)):
        green.append(result[matched_indexes[j]]);
    
    valid = True;

    for i in range(0, len(red)):
        if not(int(red[i][:str(red[i]).index("r")]) <= 12):
            valid = False;

    for i in range(0, len(blue)):
        if not(int(blue[i][:str(blue[i]).index("b")]) <= 14):
            valid = False;

    for i in range(0, len(green)):
        if not(int(green[i][:str(green[i]).index("g")]) <= 13):
            valid = False;

    return valid;

def GetID():
    return int(line[5:line.index(":")]);

ans = 0;
for i in range(0, 100):
    ans += solution();
    print(ans);