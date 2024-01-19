# import ipdb
from statistics import mean 

class Game:
    all = []

    def __init__(self, title):
        self._title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title
 
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        return mean([result.score for result in player.results() if result.game is self])

class Player:
    all = []

    def __init__(self, username):
        self._username = username
        Player.all.append(self)

    @property 
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played() 

    def num_times_played(self, game):
        games_played = [result.game for result in self.results()]
        return games_played.count(game) 

class Result:
    all = []

    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score 
    
    @score.setter 
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, 'score'):
            self._score = score 

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player 

    @property 
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game 




# ipdb.set_trace()