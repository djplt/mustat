import musicbrainzngs as mus

MinSearchScoreAccept = 99

class APIFormatError(Exception):
  pass

class APINotFound(Exception):
  pass

class APINearlyFound(Exception):
  pass

def init():
  mus.set_useragent("Music Statistics App", "0.1", "dominic.j.platt@hotmail.com")

def getArtistSongURLs(name: str):
  '''
  Interacts with "musicbrains" API to get all the song URLs of a given artist needed to pass into 
  the "lyricssovh" API.
  '''
  URLBase = "https://api.lyrics.ovh/v1/{}/{}"
  id = searchArtistID(name)
  songs = getArtistSongs(id)
  songURLs = [URLBase.format(name, song) for song in songs]
  return songURLs


def searchArtistID(name: str):
  '''
  Search artist id by name.
  '''
  try:
    artists = mus.search_artists(name)
    # Assume this is ordered in descending format.
    topScore = artists['artist-list'][0]['ext:score']
    if int(topScore) < MinSearchScoreAccept:
      raise APINearlyFound('Did you mean %s' % artists['artist-list'][0]['ext:score'])

    return artists['artist-list'][0]['id']

  except IndexError:
    raise APINotFound
  except KeyError:
    raise APIFormatError

def getArtistSongs(id: str):
  '''
  Get all of an artists works.
  '''
  # TODO consider query with type only being song, although this is unlikely to be program bottle neck.
  offset = 0
  limit = 100
  maxSongs = 500
  songs = []
  while offset < maxSongs: 
    works = mus.browse_works(id, [], offset=offset, limit=limit)
    maxSongs = works['work-count']
    songs.extend([work['title'] for work in works['work-list'] if 'type' in work and work['type'] == 'Song'])
    offset += len(works['work-list'])

  return songs

