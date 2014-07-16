# config file
import os

root_path = os.path.dirname(os.path.realpath(__file__))
last_root_path = os.path.split(root_path)[0]
join = os.path.join



# site config
BOOK_TITLE = "MkBook"
HOST_URL = "http://127.0.0.1:5000/"


# theme config
THEME_NAME = "readthedocs"
THEME_PATH = join(root_path, "theme", THEME_NAME)

# content folder
CONTENT_PATH = join(last_root_path, "contnet")

# output
OUTPUT_PATH = join(last_root_path, "output")


##########################################
########## PARSER CONFIG STUFF ###########
##########################################

''' choose from `FLAT`, `STATIC`
    `FLAT`: show content like flatdoc, which save Internet flow,
            with one html and several .md files. 
            Each time you change the content, readers can see it immediately except
            you create a new file. In that case, you need to compile again.

    `STATIC`: show content in serveral .html files.
              You need to compile the files every time you change the content

'''
DISPLAY = "FLAT" 



##########################################
########## BOOK CONFIG STUFF ###########
##########################################

BOOK_NAME = "mkbook"










