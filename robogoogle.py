#!/usr/bin/env python3
#robogoogle.py
#Little Python script to automate your Google search results!
'''
Author: PenTestical
Twitter: https://twitter.com/PTestical
Github: https://github.com/pentestical
E-Mail: pentestical@protonmail.com

If you have improvement suggestions or something goes wrong, feel free to contact me! Made with love. <3
'''

import webbrowser, requests, bs4, sys, argparse, os, random, time

#CLI COMMANDS
#custom usage message
def msg(name=None):
    return '''\t\t\t\tpython robogoogle.py SEARCHWORD
example search for C++: \tpython robogoogle.py C++'''

#argparse to get a help menu
my_parser = argparse.ArgumentParser(epilog="-------------------------Enjoy your PenTestical search!-----------------------", description="--------------------------Google search engine 2.0----------------------------\n", usage=msg())
my_parser.add_argument('Search', metavar='searchword', nargs="+", type=str, help='specify what you want to search')
my_parser.add_argument('-n', '--number', nargs='?', default=5, type=int , help='specify the number of results. By default -n 5.')
args = my_parser.parse_args()
input_Search = args.Search

#top results from a google search
print("Let's google like a boss...")
response = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'lxml')
linkElements = soup.select('div#main > div > div > div > a')
number_of_links = min(int(args.number), len(linkElements))
delays = [0.1, 0.8, 0.3, 0.4, 0.6]
delay = random.choice(delays)
for i in range(number_of_links):
    webbrowser.open('http://google.com' + linkElements[i].get("href"))
    time.sleep(delay)
