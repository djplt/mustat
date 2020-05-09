import unittest
import statistics
from statistics import StatisticsError

from artist import Artist
from api import APINotFound

class TestArtist(unittest.TestCase):

  def test_artist_init(self):
    '''
    Test case: Simple initialiation of TestArtist.
    '''
    a = Artist("Green Day", 5)
    self.assertTrue(a.name, "Green Day")
    self.assertTrue(a.wordLengths != [])
    for wordLength in a.wordLengths:
      self.assertTrue(wordLength > 0)

    # TODO test against a test vector - for now just check values are sane.
    self.assertTrue(a.averageWordLength > 1)
    self.assertTrue(a.stdevWordLength > 0)
    self.assertTrue(a.varianceWordLength > 0)


  def test_api_song_mismatch(self):
    '''
    Test case: Brainmusic API returns songs but the "lyrics" API returns 404 to "The Eagles".
    All artist song names return a 404 when searching under the lyrics API.
    The "Artist" module will simply throw a common APINotFound exception if something has not been found during the
    API download.
    '''
    exceptionRaised = False
    try:
      a = Artist("The Eagles", 5)
      self.assertTrue(a.name, "The Eagles")
      self.assertTrue(a.wordLengths == [])
    except APINotFound:
      exceptionRaised = True

    self.assertTrue(exceptionRaised)


if __name__ == "__main__":
  unittest.main()