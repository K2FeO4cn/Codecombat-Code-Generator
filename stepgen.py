import json
commands = input()
com_con = {
        "w":{"d": 0, "s": 1},
        "a":{"d": 3, "s": 1},
        "s":{"d": 2, "s": 1},
        "d":{"d": 1, "s": 1},
        "z":{"s":"archer"},
        "x":{"a":""},
        "c":{"s":"soldier"}
    }
coms = []
for com in commands:
    coms.append(com_con[com])
json.dump(coms,open("./coms.json","r+"))