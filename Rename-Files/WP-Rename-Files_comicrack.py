# WP-Rename-Files_comicrack.py
#
##########################################################################

import clr
clr.AddReferenceByPartialName("System.Windows.Forms")
from System.Windows.Forms import *

import sys
import datetime
import re
sys.setdefaultencoding("utf8")

remove_punctuation_map = dict((ord(char), None) for char in '\/*?:"<>|')

#
# Rename Book Files (serials)
#
#@Name WP - Rename Files (serials)
#@Hook Books
#@Description Script to rename the selected Books based on the meta data
def WPRenameBookFiles(books):
    for book in books:
        name = book.ShadowSeries
        name = re.sub('[:]', ' -', name)
        name = name.translate(remove_punctuation_map)
        paddednumber = str(book.ShadowNumber).zfill(3)
        monthname = datetime.date(1900, book.Month, 1).strftime('%B')
        if name != "":
            if book.ShadowNumber != "":
                name = name + " - #" + paddednumber
            if book.ShadowYear != -1:
                name = name + " (" + monthname + ", " + str(book.ShadowYear) + ")"
            book.RenameFile (name)

#
# Rename Book Files (TPBs)
#
#@Name WP - Rename Files (TPBs)
#@Hook Books
#@Description Script to rename the selected Books based on the meta data
def WPRenameBookFilesTPBs(books):
    for book in books:
        name = book.ShadowSeries
        name = re.sub('[:]', ' -', name)
        name = name.translate(remove_punctuation_map)
        volumetitle = book.Title
        paddednumber = str(book.ShadowNumber).zfill(2)
        monthname = datetime.date(1900, book.Month, 1).strftime('%B')
        if name != "":
            if book.ShadowNumber != "":
                name = name + " - V" + paddednumber
            name = name + " - " + volumetitle
            if book.ShadowYear != -1:
                name = name + " (" + monthname + ", " + str(book.ShadowYear) + ")"
            book.RenameFile (name)
