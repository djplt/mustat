import click
import api
from api import searchArtistID, APIFormatError, APINearlyFound, APINotFound

@click.command()
@click.option('--name', prompt='Artist name',
              help='The Artist name to perform statistics on.')
def main(name):
  '''
  Mustat - Music Statistics.
  Program to generate statistics about music artists.
  '''
  click.echo("You typed in the name %s" % name)
  try:
    api.searchArtistID(name)
  except APINearlyFound as e:
    click.echo("Did you mean %s" % e.args)
  except APINotFound:
    click.echo("Could not find any entries under the artist name %s" % name)
  except APIFormatError:
    click.echo("Unexpected API error")
  except Exception as e:
    click.echo("Unexpected error occured")
    raise e

