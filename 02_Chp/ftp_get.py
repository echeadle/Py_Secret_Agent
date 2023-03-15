"""
Python for Secret Agents
Using FTP to download files
"""
import sys
import ftplib

host = "ftp.ibiblio.org"
root = "/pub/docs/books/gutenberg/"

"""
Get function to download files
Page 50
"""
def get( fullname, output=sys.stdout):
    download = 0
    expected = 0
    dots = 0
    def line_save( aLine ):
        nonlocal download, expected, dots
        print( aLine, file=output)
        if output != sys.stdout:
            download += len(aLine)
            show= (20*download)//expected
            if show > dots:
                print("-", end="", file=sys.stdout )
                sys.stdout.flush()
                dots= show
    with ftplib.FTP( host, user="anonymous") as connection:
        print("Welcome", connection.getwelcome())
        expected= connection.size( fullname )
        connection.retrlines("RETR {0}".format(fullname), line_save)
    if output != sys.stdout:
        print() #End of dots


"""
Show the README from Gutenberg press on stdout
"""

get(f"{root}README")

"""
Get GUTINDEX.ALL and save to file
"""

with open("GUTINDEX.ALL", "w", encoding="UTF-8") as output:
    get(f"{root}GUTINDEX.ALL", output)
