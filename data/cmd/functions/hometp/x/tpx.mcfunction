tp @s 0 ~ ~
execute as @s[scores={homeX=..-1}] at @s run function cmd:hometp/x/tpx_neg
execute as @s[scores={homeX=1..}] at @s run function cmd:hometp/x/tpx_pos