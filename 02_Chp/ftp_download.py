import ftplib

host = "ftp.ibiblio.org"
root = "/pub/docs/books/gutenberg/"

def directory_list( path ):
    with ftplib.FTP(host, user="anonymous") as connection:
        print(f"Welcome {connection.getwelcome()}")
        for name, details in connection.mlsd(path):
            print(f"{name} {details['type']} {details.get('size')}")

directory_list(root)
