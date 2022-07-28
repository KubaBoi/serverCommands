execute store result score @p posX run data get entity @p Pos[0]
execute store result score @p posY run data get entity @p Pos[1]
execute store result score @p posZ run data get entity @p Pos[2]

scoreboard players operation X Position = @p posX
scoreboard players operation Y Position = @p posY
scoreboard players operation Z Position = @p posZ