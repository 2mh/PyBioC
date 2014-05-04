#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# h2m@access.uzh.ch

from os import curdir, sep
import sys

from nltk.tokenize import wordpunct_tokenize
from nltk import PorterStemmer

from bioc import BioCAnnotation
from bioc import BioCReader
from bioc import BioCWriter

BIOC_IN = '..' + sep + 'test_input' + sep + 'example_input.xml'
BIOC_OUT = 'example_input_stemmed.xml'
DTD_FILE = '..' + sep + 'BioC.dtd'

def main():
    # A BioCReader object is put in place to hold the example BioC XML
    # document
    bioc_reader = BioCReader(BIOC_IN, dtd_valid_file=DTD_FILE)
    
    # A BioCWRiter object is prepared to write out the annotated data
    bioc_writer = BioCWriter(BIOC_OUT)
    
    # The NLTK porter stemmer is used for stemming
    stemmer = PorterStemmer()
    
    # The example input file given above (by BIOC_IN) is fed into
    # a BioCReader object; validation is done by the BioC DTD
    bioc_reader.read()
    
    # Pass over basic data
    bioc_writer.collection = bioc_reader.collection
    
    # Get documents to manipulate
    documents = bioc_writer.collection.documents
    
    # Go through each document
    annotation_id = 0
    for document in documents:
        
        # Go through each passage of the document
        for passage in document:
            #  Stem all the tokens found
            stems = [stemmer.stem(token) for 
                     token in wordpunct_tokenize(passage.text)]
            # Add an anotation showing the stemmed version, in the
            # given order
            for stem in stems:
                annotation_id += 1
                
                # For each token an annotation is created, providing
                # the surface form of a 'stemmed token'.
                # (The annotations are collectively added following
                #  a document passage with a <text> tag.)
                bioc_annotation = BioCAnnotation()
                bioc_annotation.text = stem
                bioc_annotation.id = str(annotation_id)
                bioc_annotation.put_infon('surface form', 
                                          'stemmed token')
                passage.add_annotation(bioc_annotation)
    
    # Print file to screen w/o trailing newline
    # (Can be redirected into a file, e. g output_bioc.xml)
    sys.stdout.write(str(bioc_writer))
    
    # Write to disk
    bioc_writer.write()
    
if  __name__ == '__main__':
    main()
