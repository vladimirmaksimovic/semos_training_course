import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("text-01.txt")
    
    # make a backup copy by appending "bak" to the name
    dst = src + ".bak"

    # copy over permissions, modification times, and other info
    shutil.copy(src, dst)
    shutil.copystat(src, dst)

    # rename original file
    os.rename("text-01.txt", "new-text-01.txt")

    # put things into a ZIP
    root_dir, tail = path.split(src)
    shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip","w") as newzip:
      newzip.write("newfile.txt")
      newzip.write("textfile.txt.bak")

if __name__ == "__main__":
  main()