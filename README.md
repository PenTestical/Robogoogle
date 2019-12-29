# Robogoogle
Python script to open several Google results. Save your time by automating your Google search!

## Requirements

You need [pip](https://pypi.org/project/pip-download/) to download the required modules. 

**Install requirements on Linux (Python3)**

If you have Python 3, use the command line: </br>
`git clone https://github.com/PenTestical/Robogoogle.git` </br>
`pip3 install -r requirements.txt`</br>
This will install the required modules bs4, webbrowser, requests (most important) and few other.

**Install requirements on Linux (Python2)**

If you are using Python 2, try instead:</br>
`git clone https://github.com/PenTestical/Robogoogle.git` </br>
`pip install -r requirements.txt`</br>

**Install requirements on Windows**

Download the ZIP file, unzip it and then enter the command line to install the required modules:
`python -m pip install -r requirements.txt`

## Basic Usage

How to use the script? It's pretty simple. By just entering the searchword after the python script you can start. If you want to search for Ice cream, just enter:</br>
`python robogoogle.py ICE CREAM`</br>

On Python 3 (Linux), you need to use:</br>
`python3 robogoogle.py ICE CREAM`

## Advanced Usage

By default, your browser will open 5 results. To change this behavior, use the `-n` command. To open at example 10 results for Ice cream, enter:</br>
`python robogoogle.py ICE CREAM -n 10`

On Python 3, you need to use:</br>
`python3 robogoogle.py ICE CREAM -n 10`


## Help
To print the help message, enter:</br>
`python robogoogle.py -h`
or:</br>
`python robogoogle.py --help`

With Python 3 (Linux):</br>
`python3 robogoogle.py -h`

