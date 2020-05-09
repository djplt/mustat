import click
import api
from api import searchArtistID, APIFormatError, APINearlyFound, APINotFound
from artist import Artist
from plot import histogram, wordBarPlot, show

@click.command()
@click.option('--name', prompt='Artist name',
              help='The Artist name to perform statistics on.')
@click.option('--songs', default=500, help='Number of song lyrics to download')
@click.option('--graph/--no-graph', default=False, help='Display a graphical output')
def main(name, songs, graph):
  '''
  Mustat - Music Statistics.
  CLI to program to generate statistics about music artists.
  '''
  try:
    art = Artist(name, songs)
    click.echo("Artist data downloaded!\n")
    click.echo("**** Summary Artist Data ****")
    click.echo("Artist name: %s" %art.name)
    click.echo("Attempted song downloads %d" %songs)
    click.echo("Successful song downloads %d" %len(art.songs))
    click.echo("Average word length = %.2f" %art.averageWordLength)
    click.echo("Standard deviation of word length = %.2f" %art.stdevWordLength)
    click.echo("Variance of word length = %.2f" %art.varianceWordLength)
    click.echo("Most common word: '%s'" %art.mostCommonword)

    if graph:
      histogram(art.wordLengths, x_label="Word Lengths", y_label="Frequency",
                title="{} Word Lengths".format(art.name))

      wordBarPlot(art.words, x_label="Words", y_label="Frequency",
                title="{}'s Top 10 Words".format(art.name))
      show()
  except APINearlyFound as e:
    click.echo("Did you mean %s?" % e.args)
  except APINotFound:
    click.echo("Could not find any artists or songs under the artist name '%s'" % name)
  except APIFormatError:
    click.echo("Unexpected API error")
  except Exception as e:
    click.echo("**** An unexpected error occurred ****")
    raise e
