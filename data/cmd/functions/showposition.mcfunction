#execute store result score @s posX run data get entity @s Pos[0]
#execute store result score @s posY run data get entity @s Pos[1]
#execute store result score @s posZ run data get entity @s Pos[2]

#scoreboard players operation X Position = @s posX
#scoreboard players operation Y Position = @s posY
#scoreboard players operation Z Position = @s posZ

execute store result score Svagrid posX run data get entity Svagrid Pos[0]
execute store result score Svagrid posY run data get entity Svagrid Pos[1]
execute store result score Svagrid posZ run data get entity Svagrid Pos[2]

scoreboard players operation X Position = Svagrid posX
scoreboard players operation Y Position = Svagrid posY
scoreboard players operation Z Position = Svagrid posZ

execute store result score JoVitaa posX run data get entity JoVitaa Pos[0]
execute store result score JoVitaa posY run data get entity JoVitaa Pos[1]
execute store result score JoVitaa posZ run data get entity JoVitaa Pos[2]

scoreboard players operation X Position = JoVitaa posX
scoreboard players operation Y Position = JoVitaa posY
scoreboard players operation Z Position = JoVitaa posZ