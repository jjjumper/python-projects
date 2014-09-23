
class Ship():
    size = None

class Carrier(Ship):
    size = 5
    
class BattleShip(Ship):
    size = 4
    
class PatrolBoat(Ship):
    size = 2
    
class Destroyer(Ship):
    size = 3

class Submarine(Ship):
    size = 3
player_carrier = Carrier()
enemy_carrier = Carrier ()

print(player_carrier.size)
print(enemy_carrier.size)
