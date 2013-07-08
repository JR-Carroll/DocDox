#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""
This short script is designed to concat multiple Doxygen files
into one large file.  The purpose for this is that Doxygen provides
a low-level documentation standard-of-sorts using Markdown, Doxygen-
specific syntax, and HTML.  By drafting documentation in Doxygen, a
author can create several media outputs (PDF; RTF; Web; LaTeX) at the
same time!  

To draft documentation a user should first structure the document into
separate 'chapters' or pages.  Each chapter/page should be isolated 
by content and design - of course, as a user, you can design it however
you want.  

For instance, the file-structure for a sample project might look like:

Main Page
    Introduction
    About
    More Information

How to Use Doxygen
    Invoking Doxygen via CMD-Line
    Invoking Doxygen via a GUI
    Changing options

Various Doxygen-outputs
    PDF
    RTF
    LaTeX
    
...And so on...

"Main Page", "How to Use Doxygen", and "Various Doxygen-outputs" would be
their own separate files in the main directory.  Each with their own 
`\section` and `\subsections`.  

The purpose for this design is to keep the maintainable sections compartmentalized
so it can be easily updated in CVS, and allows a user to built their own flavor of
documentation locally.  

<<IMPORTANT>>

For this script to work, you must use a separate table of contents (TOC) file named 
`toc.txt`.  This TOC file is just a JSON payload that helps to give order to the
document; by not providing a TOC file, Doxygen will just generate a random collection
of documents into a single document (it has the apperance of being alphabetical, but 
Doxygen really just does whatever the hell it wants...).  

The JSON payload should be in the form of:

    {
    "Title": "DoxygenTOCS",
    "LocationOfContents": "/home/username/workspace/myDoxygenDocumentation/",
    "FileExtensions": ["md"],
    "OrderOfContents": [
        "mainpage",
        "introductions",
        "specifications",
        [...etc...],
        ]
    }

TODO:  Add support for various other 'extension' types.

After you have constructed this TOC file, place it in the same directory
as this script and run!  You should see output generated for `documentation.md`
with all the contents of your various separate pages correctly concatenated.

Next, you'll want to run Doxygen on your `documentation.md` file; to learn more 
about how to run Doxygen, visit their website at http://www.stack.nl/~dimitri/doxygen/.

If you are interested in generating various additional formats from Doxygen pages, make
sure to generate your Doxyfile (or use a GUI to edit Doxyfile on-the-fly) and enable
or disable the various output formats you need.
"""

import os

try: 
    import simplejson as json
except ImportError:
    import json
    
## Sets the current working directory.  You SHOULD put this in the same
## directory as all your source files for Doxygen!
__CWDList__ = [x for x in os.getcwd().split("/") if x != ""]

## String containing the table of contents file.  Contents should be a 
## JSON-valid payload. 
__TOCLOCATION__ = "./toc.txt"

## Context-manager for opening/closing the json-TOC file.
with open(__TOCLOCATION__, 'rb') as jsonImport:
    __loadedTOC__ = json.load(jsonImport)

__extensions__ = __loadedTOC__.get("FileExtensions")
__fileLocation__ = __loadedTOC__.get("LocationOfContents")
__files__ = __loadedTOC__.get("OrderOfContents")

## Context-manager for making an entire dumpfile for all the separate 
## doxygen files.
with open('./documentation.md', 'wb+') as outFile:
    ## iterate through all the files, in order.
    ## kickPageDown is a small state-machine to start adding "\page" to the appended documents.
    _kickPageDown_ = False
    for doxyfile in __files__: 
        _tempFile_ = open(__fileLocation__ + "/" + doxyfile + "." + __extensions__[0]).read()
        _tempFileSplit_ = _tempFile_.split("\n")

        if _kickPageDown_:
            outFile.write("\n\n\page \"" + _tempFileSplit_[0].split("{")[0] + "\"\n" + "\n".join(_tempFileSplit_[2:]))
            pass
        else:
            outFile.write(_tempFile_)
        _kickPageDown_ = True

## TODO:  Need to eat the first two lines of each MD file to elimate the header and '===='.
##        In its place, I need to add \page 'ORIGINAL_HEADER'

print "all is quiet on the Western front..."