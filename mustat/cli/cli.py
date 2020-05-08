import click
import api
from api import searchArtistID, APIFormatError, APINearlyFound, APINotFound
from artist import Artist

@click.command()
@click.option('--name', prompt='Artist name',
              help='The Artist name to perform statistics on.')
@click.option('--songs', default=20, help='Number of song lyrics to download')
def main(name, songs):
  '''
  Mustat - Music Statistics.
  Program to generate statistics about music artists.
  '''
  try:
    art = Artist(name, songs)
    click.echo("Artist data downloaded!")
    click.echo("\n**** Summary Artist Data ****")
    click.echo("Artist name: %s" %art.name)
    click.echo("Attempted song downloads %d" %songs)
    click.echo("Successful song downloads %d" %len(art.songs))
    click.echo("Average word length = %.2f" %art.averageWordLength)
    click.echo("Standard deviation of word length = %.2f" %art.stdevWordLength)
    click.echo("Variance of word length = %.2f" %art.varianceWordLength)
  except APINearlyFound as e:
    click.echo("Did you mean %s?" % e.args)
  except APINotFound:
    click.echo("Could not find any entries under the artist name %s" % name)
  except APIFormatError:
    click.echo("Unexpected API error")
  except Exception as e:
    click.echo("**** An unexpected error occured ****")
    raise e

