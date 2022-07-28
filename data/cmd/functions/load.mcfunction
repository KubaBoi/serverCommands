
scoreboard objectives add tempPos dummy

scoreboard objectives add homeX dummy
scoreboard objectives add homeY dummy
scoreboard objectives add homeZ dummy

# Position
scoreboard objectives add posX dummy
scoreboard objectives add posY dummy
scoreboard objectives add posZ dummy

scoreboard objectives remove Position
scoreboard objectives add Position dummy
scoreboard objectives setdisplay sidebar Position 

scoreboard objectives add health health
scoreboard objectives setdisplay belowName health

scoreboard objectives add death deathCount
scoreboard objectives setdisplay list death

#gamerule sendCommandFeedback false

tellraw @a {"text": "==========="}
tellraw @a {"text": "ServerCommands datapack loaded", "color": "#00FF00"}
tellraw @a {"text": ""}
tellraw @a {"text": "For usage type:"}
tellraw @a {"text": "/function cmd:help", "color": "#fcba03"}
tellraw @a {"text": ""}
tellraw @a {"text": "==========="}
