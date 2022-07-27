
import os

from buildTp import TpBuilder

pth = os.path.abspath(os.path.join(__file__, "..", "data", "cmd", "functions"))

helpData = """
tellraw @a {"text": ""}
tellraw @a {"text": "====HELP====", "color": "#ff0000"}
tellraw @a {"text": "Usage:"}
tellraw @a {"text": "/function cmd:<command name> <value>", "color": "#00FF00"}
tellraw @a {"text": ""}
tellraw @a {"text": "Example:"}
tellraw @a {"text": "/function cmd:home", "color": "#00FF00"}
tellraw @a {"text": ""}
tellraw @a {"text": "====COMMANDS====", "color": "#ff0000"}
tellraw @a {"text": "help", "color": "#fcba03"}
tellraw @a {"text": "    - shows help"}
"""

cmdData = ""
for root, dirs, files in os.walk(pth):
    for file in files:
        if (not root.endswith("functions")): continue

        with open(os.path.join(pth, file), "r") as f:
            lines = f.readlines()

        if (len(lines) == 0): continue
        if (lines[0].strip() != "# COMM"): continue

        cmdData += 'tellraw @a {"text": "' + file.replace(".mcfunction", "") + '", "color": "#fcba03"}\n'
        for line in lines[1:]:
            line = line.strip()
            if (line == "# COMMEND"): break
            cmdData += 'tellraw @a {"text": "    -' + line.replace("#", "") + '"}\n'

with open(os.path.join(pth, "help.mcfunction"), "w") as f:
    f.write(helpData + cmdData + 'tellraw @a {"text": ""}')

tpBuild = TpBuilder(os.path.join(pth, "tp"))
tpBuild.build(
        (-10000, 10000, "tpx"),
        (-64, 320, "tpy"),
        (-10000, 10000, "tpz")
    )