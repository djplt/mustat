from statistics import mean, stdev, variance
import timeit

from api import api, APINotFound, getSongLyrics, getArtistSongs

class Artist(object):

  def __init__(self, name: str, maxSongs: int = 500):
    '''
    Downloads an sets up an artist data structure.
    '''
    self.name, self.id = api.searchArtistID(name)
    self.songs = getArtistSongs(self.id, maxSongs)
    self.words = getSongLyrics(self.name, self.songs)
    if self.words == []:
      raise api.APINotFound
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


