
import os

pth = os.path.abspath(os.path.join(__file__, "..", "data", "cmd", "functions"))

loadData = """
scoreboard objectives add tpConst dummy
scoreboard objectives add tpVar dummy

scoreboard objectives add homeX dummy
scoreboard objectives add homeY dummy
scoreboard objectives add homeZ dummy

tellraw @a {"text": "ServerCommands datapack loaded", "color": "#00FF00"}
tellraw @a {"text": ""}
tellraw @a {"text": "Usage:"}
tellraw @a {"text": "/function cmd:<command name> <value>", "color": "#fcba03"}
tellraw @a {"text": ""}
tellraw @a {"text": "Example:"}
tellraw @a {"text": "/function cmd:home", "color": "#fcba03"}
tellraw @a {"text": ""}
tellraw @a {"text": "====COMMANDS===="}
"""

for root, dirs, files in os.walk(pth):
    for file in files:
        with open(os.path.join(pth, file), "r") as f:
            lines = f.readlines()

        if (lines[0] != "# COMM"): continue

        loadData += 'tellraw @a {"text": "' + file.replace(".mcfunction", "") + '", "color": "#fcba03"}\n'
        for line in lines:
            line = line.strip()
            if (line == "# COMMEND"): break
            loadData += 'tellraw @a {"text": "    -' + line.replace("#", "") + '"}\n'

with open(os.path.join(pth, "load.mcfunction"), "w") as f:
    f.write(loadData)
