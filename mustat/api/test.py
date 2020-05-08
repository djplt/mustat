import unittest

from api import APIFormatError, APINearlyFound, APINotFound, init, searchArtistID, getArtistSongs, getSongLyrics, \
                lyricFormat 
import re

class TestAPI(unittest.TestCase):
  def setUp(self):
    init()

  # def test_search_artist(self):
  #   '''
  #   Test case: Search for a valid artist and get the artist id.
  #   '''
  #   try:
  #     id = searchArtistID("Cat Stevens")
  #     self.assertIsNotNone(id)
  #   except:
  #     self.fail("Unexpected exception raised")

  # def test_search_invalid_artist(self):
  #   '''
  #   Test case: Search for a non-existant artist.
  #   '''
  #   self.assertRaises(APINotFound, searchArtistID, "fasdfasfdfasfasdfasd")

  # def test_search_nearly_equal_artist(self):
  #   '''
  #   Test case: Search for a nearly equal artist id.
  #   Does not appear to be possible to get an entry less than a score of 100% so the strings must be compared.
  #   '''
  #   # TODO
  #   pass

  # def test_get_artist_songs(self):
  #   '''
  #   Test case: Get all songs by an artist.
  #   '''
  #   _, id  = searchArtistID("Cat Stevens")
  #   songs = getArtistSongs(id)
  #   self.assertIsNotNone(songs)

  def test_get_artist_song_lyrics(self):
    '''
    Test case: Get all the songs by an artist and put them into a "GET" request format used for the "lyrics" API.
    '''
    name, id = searchArtistID("Cat Stevens")
    songs = getArtistSongs(id, 5)
    lyrics = [getSongLyrics(name, song) for song in songs]
    self.assertIsNotNone(lyrics)
    self.assertTrue(lyrics != [])
    for l in lyrics:
      for word in l:
        self.assertFalse(word == "")    # Should not contain empty words
        self.assertTrue(word.isalnum()) # Only contains alpha-numeric chars.
        # self.assertIsNotNone(regex.match(word))


  def test_lyric_split_by_whitespace(self):
    '''
    Test case: Test the util function to be able extract relevant words from the the lyrics string.
    '''
    output = lyricFormat("dupa kupa lupa")
    self.assertListEqual(output, ["dupa", "kupa", "lupa"])
    output = lyricFormat("dupa    kupa   lupa")
    self.assertListEqual(output, ["dupa", "kupa", "lupa"])
    output = lyricFormat("dupa\nkupa\t\n\r\t   lupa")

  def test_lyric_format_non_chars(self):
    '''
    Test case: Test the util function to be able extract relevant words from the the lyrics string.
    '''
    # Strange input but we should be able to handle it.
    output = lyricFormat("dupa-kupa -, lupa")
    self.assertListEqual(output, ["dupa", "kupa", "lupa"])
    output = lyricFormat("don't don`t don´t")
    self.assertListEqual(output, ["dont", "dont", "dont"])




if __name__ == "__main__":
  unittest.main()