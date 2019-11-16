class Musician:

    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def get_name(self):
        return(self.name)

    def get_instrument(self):
        return(self.instrument)

    def play_song(self, song_title):
        return("I'm playing " + song_title)
