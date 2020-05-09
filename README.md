# Mustat

Music Statistics Application. A CLI to gather statistics about a given artist, such as average word length, standard deviation and displaying graphs.

## Prerequisites

* python 3.5 or higher

* pip (for python3)

* virtualenv (optional)

### Getting Started

Clone the repository

```
git clone https://github.com/djplt/mustat.git
```

Navigate into the root directory

```
cd mustat
```

Start & activate a virtual environment (optional)

```
python3 -m virtualenv venv

source venv/bin/activate
```

Install the python modules from the root directory

```
pip install -r requirements.txt
```

### Command Line Interface

Mustat - Music Statistics. CLI to program to generate statistics about music artists.

Options:

  --name TEXT           The Artist name to perform statistics on.

  --songs INTEGER       Number of song lyrics to download

  --graph / --no-graph  Display a graphical output

  --help                Show this message and exit.

#### Example Use Cases

Executable from the root project directory.

Typical use case:

```
python mustat
```

You will then be prompted for the name of the artist you want to download statistics on.

Alternatively you can supply the name of the artist in the command line.

```
python mustat --name "ed sheeran"
```

You can also enable a graphical output of the data.

```
python mustat --name "cat stevens" --graph
```

The default maximum songs attempted to be downloaded is 500 but this is configurable.

```
python mustat --name "leonard cohen" --songs=20
```

## Running the tests

From the root directory you can run all unit and integration tests

```
python -m unittest discover -v mustat
```

## Authors

* **Dominic Platt**
