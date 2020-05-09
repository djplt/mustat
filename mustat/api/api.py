import musicbrainzngs as mus
import requests
import json
import re
import asyncio
import concurrent.futures
import requests

MinSearchScoreAccept = 99

class APIFormatError(Exception):
  pass

class APINotFound(Exception):
  pass

class APINearlyFound(Exception):
  pass

def init():
  mus.set_useragent("Music Statistics App", "0.1", "dominic.j.platt@hotmail.com")

def searchArtistID(name: str):
  '''
  Search artist id by name.
  '''
  try:
    artists = mus.search_artists(name, limit=1)
    # List is ordered in descending format.
    topScore = artists['artist-list'][0]['ext:score']
    artistMatchedName = artists['artist-list'][0]['name']
    artistMatchedID = artists['artist-list'][0]['id']
    if int(topScore) < MinSearchScoreAccept or (name.lower() != artistMatchedName.lower()):
      raise APINearlyFound(artistMatchedName)

    return artistMatchedName, artistMatchedID

  except IndexError:
    raise APINotFound
  except KeyError:
    raise APIFormatError

def getArtistSongs(id: str, maxSongs: int = 500):
  '''
  Get all of an artists works.
  '''
  # TODO consider query with type only being song, although this is unlikely to be program bottle neck.
  offset = 0
  limit = 100
  songs = []
  while offset < maxSongs: 
    limit = min(maxSongs-offset, limit)
    works = mus.browse_works(id, [], offset=offset, limit=limit)
    maxSongs = min(works['work-count'], maxSongs)
    songs.extend([work['title'] for work in works['work-list'] if 'type' in work and work['type'] == 'Song'])
    offset += len(works['work-list'])

  return songs

async def _getSongLyrics_async(URLs: str):
  '''
  Asynchronous internal function for performing a Get request on a list on URLs.
  '''
  with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:

      loop = asyncio.get_event_loop()
      futures = [
          loop.run_in_executor(
              executor, 
              requests.get, 
              URL
          )
          for URL in URLs ]
      lyrics = []
      for res in await asyncio.gather(*futures):
          if res.ok and 'lyrics' in res.json():  # If the response is strange then just ignore this set of lyrics.
            lyrics.extend(lyricFormat(res.json()['lyrics']))
  return lyrics



def getSongLyrics(artist: str, songs: str):
  '''
  Retrieves song lyrics based on artist name and song.
  Returns an empty array if response was unsuccessful.
  This is done asynchronously as tests reveal this to function to be the bottleneck.
  E.g. Searching for the artist and getting the artist songs took ~2 seconds.
  '''
  lyrics = []
  URLBase = "https://api.lyrics.ovh/v1/{}/{}"
  URLs = [ 
    URLBase.format(artist, song)
    for song in songs
  ]
  loop = asyncio.get_event_loop()
  lyrics = loop.run_until_complete(_getSongLyrics_async(URLs))
  
  return lyrics

def lyricFormat(lyrics: str):
  '''
  Formats a lyrics string into an array of words, by removing all non-word chars splitting by whitespace.
  Note: Apostrophe's are simply removed from the count but not used as a deliminator e.g. "can't not" will become 
        ["cant", "not"]

  TODO Consider removing all non char words - although may be a bit too brutal.
  TODO Consider cases like "it's or Tom's"
  '''

  lyrics = lyrics.lower()
  # See note above.
  lyrics = re.sub(r"['|`|´]", '', lyrics)
  # Replace unwanted chars with whitespace and split by whitespace. E.g. one-two-three becomes ["one", "two", "three"]
  return re.sub(r'[-|.|,|?|!|"|(|)|{|}:|;]', ' ', lyrics).split()

