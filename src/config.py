# iota_arena configuration file

#####################################
# import the player strategies needed
#####################################
from src.player_inventory.OneCardPlayer import OneCardPlayer

#####################################
# identify the players and strategies
#####################################
Player1 = OneCardPlayer()
Player2 = OneCardPlayer()
#Player3 =
#Player4 =

#############################
# identify the players in [,]
#############################
players = [Player1, Player2]
