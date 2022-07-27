# COMM
# teleports player to his home
# COMMEND
execute as @s run scoreboard players operation @s tempPos = @s homeX
execute as @s at @s run function cmd:tp/tpx
execute as @s run scoreboard players operation @s tempPos = @s homeY
execute as @s at @s run function cmd:tp/tpy
execute as @s run scoreboard players operation @s tempPos = @s homeZ
execute as @s at @s run function cmd:tp/tpz

tellraw @s {"text": "Welcome home :)", "color": "#00FF00"}