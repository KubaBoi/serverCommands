
import os

class TpBuilder:

    def __init__(self, pth):
        self.pth = pth

    def build(self, xData, yData, zData):
        """
        data - tuple
        (lowLimit, highLimit, scoreboard name, file name)
        """
        with open(os.path.join(self.pth, xData[2] + ".mcfunction"), "w") as f: f.write("")
        self.__buildOne(xData, 1)
        self.__buildOne(xData, 1, True)

        with open(os.path.join(self.pth, yData[2] + ".mcfunction"), "w") as f: f.write("")
        self.__buildOne(yData, 2)
        self.__buildOne(yData, 2, True)

        with open(os.path.join(self.pth, zData[2] + ".mcfunction"), "w") as f: f.write("")
        self.__buildOne(zData, 3)
        self.__buildOne(zData, 3, True)

    def __buildOne(self, data, pos, neg=False):
        cmds = ""
        if (neg):
            rng = range(0, data[1])
            name = "pos"
            r = "0.."
        else:
            rng = range(data[0], 1)
            name = "neg"
            r = "..-1"

        for i in rng:
            coords = self.nth_repl("~ ~ ~", "~", str(i), pos)
            cmds += "execute as @s[scores={tempPos=" + str(i) + "}] at @s run tp " + coords + "\n"

        with open(os.path.join(self.pth, f"{data[2]}_{name}.mcfunction"), "w") as f:
            f.write(cmds)

        with open(os.path.join(self.pth, f"{data[2]}.mcfunction"), "a") as f:
            f.write("execute as @s[scores={tempPos=" + r + "}] at @s run function cmd:tp/" + data[2] + "_" + name + "\n")

    def nth_repl(self, s, sub, repl, n):
        find = s.find(sub)
        # If find is not -1 we have found at least one match for the substring
        i = find != -1
        # loop util we find the nth or we find no match
        while find != -1 and i != n:
            # find + 1 means we start searching from after the last match
            find = s.find(sub, find + 1)
            i += 1
        # If i is equal to n we found nth match so replace
        if i == n:
            return s[:find] + repl + s[find+len(sub):]
        return s
