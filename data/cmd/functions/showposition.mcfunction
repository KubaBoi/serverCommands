execute store result score @p posX run data get entity @p Pos[0]
execute store result score @p posY run data get entity @p Pos[1]
execute store result score @p posZ run data get entity @p Pos[2]

scoreboard players operation X Position = @a posX
scoreboard players operation Y Position = @a posY
scoreboard players operation Z Position = @a posZ