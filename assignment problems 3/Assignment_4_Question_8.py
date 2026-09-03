# concept: abstract and class attributes
class Player:
    player_count = 0
    def __init__(self,name,level):
        self.name = name
        self.level = level
        Player.player_count += 1

    @classmethod
    def get_player_count(cls):
        print(f"Total player is: {cls.player_count}")

p1 = Player("vishnu",1)
p2 = Player("urvashi",2)
Player.get_player_count()