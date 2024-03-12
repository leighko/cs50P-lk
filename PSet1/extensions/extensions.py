"""
implement a program that prompts the user for the name of 
a file and then outputs that file’s media type if the file’s 
name ends, case-insensitively, in any of these suffixes:

    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip

If the file’s name ends with some other suffix or has no 
suffix at all, output application/octet-stream instead, which 
is a common default.
"""


def main():
    file_name = input("File name: ").strip().lower()
    ext_finder(file_name)


def ext_finder(n):
    if ".gif" in n:
        print("image/gif")
    elif ".jpg" in n or ".jpeg" in n:
        print("image/jpg")
    elif ".png" in n:
        print()
    elif ".pdf" in n:
        print("application/pdf")
    elif ".txt" in n:
        print("application/txt")
    elif ".zip" in n:
        print("file/zip")
    else:
        print("application/octet-stream")


main()