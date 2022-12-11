with open("02/inputs.txt", "r") as f:
    input= f.read().split("\n")

result_dic = {
    "A X":  0,
    "A Y":  1,
    "A Z":  -1,
    "B X":  -1,
    "B Y":  0,
    "B Z":  1,
    "C X":  1,
    "C Y":  -1,
    "C Z":  0,
}

point__result_dic = {
    1:6,
    0:3,
    -1:0
}
point_shape_dic = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def part1():
    score = 0
    for x in input:
        score += point__result_dic[result_dic[x]] + point_shape_dic[x.split(" ")[1]]
    
    print(score)


def part2():
    matchbook_dic = {
        "X": -1,
        "Y": 0,
        "Z": 1,
    }
     
    shape_dic = {
       "A":{
            0:  "X",
            1:  "Y",
            -1: "Z",
        },
       "B":{ 
            -1: "X",
            0:  "Y",
            1:  "Z",
        },
        "C":{
            1:  "X",
            -1: "Y",
            0:  "Z",
        }
    }
    
    score = 0
        
    for x in input:
        shape = shape_dic[x.split(" ")[0]][matchbook_dic[x.split(" ")[1]]]

        played = x.split(" ")[0] + " " + shape
        score += point__result_dic[result_dic[played]] + point_shape_dic[shape]
    
    print(score)    
    
    
    
        
part1()
part2()