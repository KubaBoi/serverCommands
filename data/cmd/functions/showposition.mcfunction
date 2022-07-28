execute store result score @s posX run data get entity @s Pos[0]
execute store result score @s posY run data get entity @s Pos[1]
execute store result score @s posZ run data get entity @s Pos[2]

scoreboard players operation X Position = @s posX
scoreboard players operation Y Position = @s posY
scoreboard players operation Z Position = @s posZ