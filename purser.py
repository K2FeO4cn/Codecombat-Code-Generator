import src.hero
hero = src.hero.hero_model()
# Purser Testing & No-Warning Utils



def purseCom(command):
    if "d" in command:
        if command['d'] == 0:
            hero.moveUp(command['s'])
        if command['d'] == 1:
            hero.moveRight(command['s'])
        if command['d'] == 2:
            hero.moveDown(command['s'])
        if command['d'] == 3:
            hero.moveLeft(command['s'])
    elif "s" in command:
        hero.say(command["s"])
    elif "a" in command:
        if command["a"] == "":
            if hero.findNearestEnemy():
                hero.attack(hero.findNearestEnemy())
        else:
            hero.attack(command["a"])

runmap = [{"s":"Run stepgen to generete stepcode in coms.json.Copy it here."}]
runnow = 0
while True:
    if hero.findNearestEnemy():
        hero.attack(hero.findNearestEnemy())
        hero.say("soldier")
    else:
        purseCom(runmap[runnow])
        runnow += 1