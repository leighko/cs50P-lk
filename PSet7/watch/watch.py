"""
implement a function called parse that expects a str of HTML as input, 
extracts any YouTube URL that’s the value of a src attribute of an 
iframe element therein, and returns its shorter, shareable youtu.be 
equivalent as a str. Expect that any such URL will be in one of the 
formats below. Assume that the value of src will be surrounded by double 
quotes. And assume that the input will contain no more than one such URL. 
If the input does not contain any such URL at all, return None.

    http://youtube.com/embed/xvFZjo5PgG0
    https://youtube.com/embed/xvFZjo5PgG0
    https://www.youtube.com/embed/xvFZjo5PgG0

Structure watch.py as follows, wherein you’re welcome to modify main and/or 
implement other functions as you see fit, but you may not import any other 
libraries. You’re welcome, but not required, to use re and/or sys.
"""

import re

csdhtml = '<iframe width="560" height="315" src="https://www.youtube.com/embed/Gnwr8x-W_fY?si=cexPExL6TLGNbOAJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'

def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str:
    if matches := re.search(r'.+(https?://(www\.)?youtube\.com/embed/\w.+?)"', s, re.IGNORECASE):
        g1 = matches.group(1)
        new_g1 = g1.replace("youtube.com/embed", "youtu.be")
        return new_g1

if __name__ == "__main__":
    main()