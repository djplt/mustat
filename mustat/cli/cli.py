import click

@click.command()
@click.option('--name', prompt='Artist name',
              help='The Artist name to perform statistics on')
def main(name):
  '''
  Mustat - Music Statistics.
  Program to generate statistics about a music artists.
  '''
  click.echo("You typed in the name %s" %name)
