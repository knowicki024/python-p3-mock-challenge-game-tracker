import ipdb 

class Game:
    def __init__(self, title):
        self.title = title
        self.results_list = []
        self.players_list = []

    @property
    def title(self):
        return self.title
        
    @title.setter
    def title(self, title):
        if (not hasattr(self, 'title')) and type(title) == str and len(title) >0:
            self._title = title 
        else:
            print("Error: Unable to set title.")

    def results(self):
        return self.results_list

    def players(self):
        return self.players_list

    def average_score(self, player):
        score_list = [result.score for result in self.results_list if result.player is player]
        return sum(score_list) / len(score_list)



class Player:
    def __init__(self, username):
        self.username = username
        self.results_list = []
        self.games_list = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return self.results_list

    def games_played(self):
        return self.games_list

    def played_game(self, game):
        if game in self.games_list:
            return True
        else:
            return False

    def num_times_played(self, game):
        result_list = [result for result in self.results_list if result.game is game]
        return len(result_list)

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        self.player.results_list.append(self)

        if not (game in self.player.games_list):
            self.player.games_list.append(game)

        self.game.results_list.append(self)

        if not(player in self.game.players_list):
            self.game.players_list.append(player)

        Result.all.append(self)


    @property 
    def score(self):
        return self._score 
    
    @score.setter
    def score(self, score):
        if (not hasattr(self, "score")) and type(score) == int and 1 <= score <= 5000:
            self._score  = score 

    @property 
    def player(self):
        return self._player 
    
    @player.setter 
    def player(self, player):
        if type(player) == Player:
            self._player = player 

    @property 
    def game(self):
        return self._game 
    
    @game.setter 
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

ipdb.set_trace()