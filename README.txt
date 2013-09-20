The PyBioC is a native python library to deal with BioCreative XML data,
i. e. to read from and to write to it.

Usage:
------
Two example programs, test_read+write.py and stemming are shipped in the
src/ folder.

test_read+write.py shows the very basic reading and writing capability of the 
library.

stemming.py uses the Python Natural Toolkit (NLTK) library to manipulate a
BioC XML file read in; it then tokenizes the corresponding text, does stemming 
on the tokens and transforms the new PyBioC objects to valid BioC XML format.
