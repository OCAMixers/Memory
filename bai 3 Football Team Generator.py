class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_endurance(self):
        return self.__endurance

    def set_endurance(self, endurance):
        self.__endurance = endurance

    def get_sprint(self):
        return self.__sprint

    def set_sprint(self, sprint):
        self.__sprint = sprint

    def get_dribble(self):
        return self.__dribble

    def set_dribble(self, dribble):
        self.__dribble = dribble

    def get_passing(self):
        return self.__passing

    def set_passing(self, passing):
        self.__passing = passing

    def get_shooting(self):
        return self.__shooting

    def set_shooting(self, shooting):
        self.__shooting = shooting

    def __str__(self):
        return f"Player: {self.__name}, Endurance: {self.__endurance}, Sprint: {self.__sprint}, Dribble: {self.__dribble}, Passing: {self.__passing}, Shooting: {self.__shooting}"


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def get_players(self):
        return self.__players

    def add_player(self, player: Player):
        for p in self.__players:
            if p.get_name() == player.get_name():
                return f"Player {player.get_name()} has already joined"
        
        self.__players.append(player)
        return f"Player {player.get_name()} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for p in self.__players:
            if p.get_name() == player_name:
                self.__players.remove(p)
                return f"Player {player_name} removed"
        
        return f"Player {player_name} not found"

    def __str__(self):
        players_str = ', '.join([player.get_name() for player in self.__players])
        return f"Team: {self.__name}, Rating: {self.__rating}, Players: [{players_str}]"
