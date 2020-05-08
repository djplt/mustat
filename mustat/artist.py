from statistics import mean, stdev, variance

from api import api

class Artist(object):

  def __init__(self, name: str, maxSongs: int = 500):
    '''
    Downloads an sets up an artist data structure.
    '''
    self.name, self.id = api.searchArtistID(name)
    self.songs = api.getArtistSongs(self.id, maxSongs)
    self.words = []
    [self.words.extend(api.getSongLyrics(self.name, song)) for song in self.songs]
    self.wordLengths = [len(word) for word in self.words]

  @property
  def averageWordLength(self):
    return mean(self.wordLengths)

  @property
  def stdevWordLength(self):
    return stdev(self.wordLengths)

  @property
  def varianceWordLength(self):
    return variance(self.wordLengths)


