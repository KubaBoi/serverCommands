
scoreboard objectives add homeX dummy
scoreboard objectives add homeY dummy
scoreboard objectives add homeZ dummy

tellraw @a {"text": "ServerCommands datapack loaded", "color": "#00FF00"}
tellraw @a {"text": ""}
tellraw @a {"text": "Usage:"}
tellraw @a {"text": "/function cmd:<command name> <value>", "color": "#fcba03"}
tellraw @a {"text": ""}
tellraw @a {"text": "Example:"}
tellraw @a {"text": "/function cmd:home", "color": "#fcba03"}
tellraw @a {"text": ""}
tellraw @a {"text": "====COMMANDS===="}
tellraw @a {"text": "home", "color": "#fcba03"}
tellraw @a {"text": "    - teleports player to his bed"}
tellraw @a {"text": "sethome", "color": "#fcba03"}
tellraw @a {"text": "    - sets players home"}
