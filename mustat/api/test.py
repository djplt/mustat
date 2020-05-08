import unittest

from api import APIFormatError, APINearlyFound, APINotFound, init, searchArtistID, getArtistSongs, getArtistSongURLs

class TestAPI(unittest.TestCase):
  def setUp(self):
    init()

  def test_search_artist(self):
    '''
    Test case: Search for a valid artist and get the artist id.
    '''
    try:
      id = searchArtistID("Cat Stevens")
      self.assertIsNotNone(id)
    except:
      self.fail("Unexpected exception raised")

  def test_search_invalid_artist(self):
    '''
    Test case: Search for a non-existant artist.
    '''
    self.assertRaises(APINotFound, searchArtistID, "fasdfasfdfasfasdfasd")

  def test_search_nearly_equal_artist(self):
    '''
    Test case: Search for a nearly equal artist id.
    Does not appear to be possible to get an entry less than a score of 100% so the strings must be compared.
    '''
    # TODO
    pass

  def test_get_artist_songs(self):
    '''
    Test case: Get all songs by an artist.
    '''
    id = searchArtistID("Cat Stevens")
    songs = getArtistSongs(id)
    self.assertIsNotNone(songs)

  def test_get_artist_song_urls(self):
    '''
    Test case: Get all the songs by an artist and put them into a "GET" request format used for the "lyrics" API.
    '''
    songURLs = getArtistSongURLs("Cat Stevens")
    self.assertIsNotNone(songURLs)




if __name__ == "__main__":
  unittest.main()