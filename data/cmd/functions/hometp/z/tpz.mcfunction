tp @s ~ ~ 0
execute as @s[scores={homeZ=..-1}] at @s run function cmd:hometp/z/tpz_neg
execute as @s[scores={homeZ=1..}] at @s run function cmd:hometp/z/tpz_pos