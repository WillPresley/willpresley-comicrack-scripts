# WP-Rename-Files_comicrack.py
# Rename files based on properties
# Cryptecks
#
##########################################################################

import clr
clr.AddReferenceByPartialName("System.Windows.Forms")
from System.Windows.Forms import *

import sys
import datetime
import re

def log_error(error_message):
    """
    Logs error messages to a file in the specified directory.
    """
    # Get the current date and time
    current_datetime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    # Create the log file name based on a predefined name and current date-time
    log_file_name = 'C:\\tmp\\WP-Rename-Files_comicrack_' + current_datetime + '.log'

    # Write the error message to the log file
    with open(log_file_name, 'a') as log_file:  # 'a' means append mode
        log_file.write(error_message + '\n')

# Prepare a map for removing unwanted characters
remove_punctuation_map = dict((ord(char), None) for char in '\/*?:"<>|')

#
# Rename Book Files (serials)
#
#@Name WP - Rename Files (serials)
#@Hook Books
#@Description Script to rename the selected Books based on the meta data
def WPRenameBookFiles(books):
    """
    Renames the selected books based on their metadata.
    Specifically designed for serials.
    """
    for book in books:
        try:
            name = hasattr(book, 'ShadowSeries') and book.ShadowSeries or ""
            name = re.sub('[:]', ' -', name)
            name = name.translate(remove_punctuation_map)
            paddednumber = hasattr(book, 'ShadowNumber') and str(book.ShadowNumber).zfill(3) or ""

            # Construct name based on available attributes
            if name:
                name += " - #" + paddednumber if paddednumber else ""

            # Check for valid month and construct month name
            if hasattr(book, 'Month') and isinstance(book.Month, int) and 1 <= book.Month <= 12:
                monthname = datetime.date(1900, book.Month, 1).strftime('%B')
                if hasattr(book, 'ShadowYear') and book.ShadowYear != -1:
                    name += " (" + monthname + ", " + str(book.ShadowYear) + ")"
            else:
                log_error("Missing or invalid 'Month' attribute for book: " + str(book))

            # Rename the book file
            book.RenameFile(name)
        except Exception as e:
            log_error("Error while processing book " + str(book) + ": " + str(e))

#
# Rename Book Files (TPBs)
#
#@Name WP - Rename Files (TPBs)
#@Hook Books
#@Description Script to rename the selected Books based on the meta data
def WPRenameBookFilesTPBs(books):
    """
    Renames the selected books based on their metadata.
    Specifically designed for TPBs.
    """
    for book in books:
        try:
            name = hasattr(book, 'ShadowSeries') and book.ShadowSeries or ""
            name = re.sub('[:]', ' -', name)
            name = name.translate(remove_punctuation_map)
            volumetitle = hasattr(book, 'Title') and book.Title or ""
            paddednumber = hasattr(book, 'ShadowNumber') and str(book.ShadowNumber).zfill(2) or ""

            # Construct name based on available attributes
            if name:
                name += " - V" + paddednumber if paddednumber else ""
                name += " - " + volumetitle if volumetitle else ""

            # Check for valid month and construct month name
            if hasattr(book, 'Month') and isinstance(book.Month, int) and 1 <= book.Month <= 12:
                monthname = datetime.date(1900, book.Month, 1).strftime('%B')
                if hasattr(book, 'ShadowYear') and book.ShadowYear != -1:
                    name += " (" + monthname + ", " + str(book.ShadowYear) + ")"
            else:
                log_error("Missing or invalid 'Month' attribute for book: " + str(book))

            # Rename the book file
            book.RenameFile(name)
        except Exception as e:
            log_error("Error while processing book " + str(book) + ": " + str(e))
