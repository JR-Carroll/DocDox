DocDox
======

A helper script to merge individual Doxygen-specific files into a single document for easier consumption by the Doxygen processor.

History/Why?
-------------

A request was made to me to create documentation in several different formats - RTF, WORD, PDF, and HTML.  One end user needed HTML, another user needed a .doc format, and yet another was requesting LaTeX.  Now, rather than draft the contents in these various flavors, it was determined that Doxygen could be used (by way of Markdown, HTML, and Doxygen-specific syntax) to create rich content from a single source); certainly, Doxygen wasn't designed for this purpose, but it does the trick!

The problem being that our in-house team was requesting (and it makes sense... to a degree) to have maintaible Doxygen/Document source-like-material that is versioned controled.  Again, Doxygen seemed to match this perfectly because it would be written in all flat-file formats that SVN could easily understand and diff against.  

In our specific project, we manually typed and formatted each individual page and customized it for Web consumption first and foremost (as this was our _majority use-case scenario_.  However, when we went back to generate the government-required documentation in PDF/Word, we saw the limitations of our decisions; Doxygen doesn't have a notion of a customizable _Table of Contents_ as far as we were able to find... i.e. you couldn't tell Doxygen to generate a PDF with `JSONSpecification.md` as the last page of the document... Doxygen has it's own internal notion (typically alphabetical order) for which it structures the documents.  This means that we needed a way to combine the separate files into one structured ordered document.

What Does This Script Do?
--------------------------

This script does exactly that!  You provide a Table of Contents JSON payload in a separate `toc.txt` file and the script reads it in that order - properly concatenating and adding Doxygen-specific syntax with `\page` syntax where needed.  


How To Use It
--------------

Pull-down the two files.  Edit the toc.txt file to reflect the order of the pages you want to merge.  Run the script, and __BAM!__.  You should have a `documentation.md` file in your directory.  Now, run Doxygen on that file to generate the various flavors of output desired.  

