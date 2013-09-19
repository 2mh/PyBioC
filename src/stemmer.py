#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# h2m@access.uzh.ch

from os import curdir, sep

from nltk.tokenize import wordpunct_tokenize
from nltk import PorterStemmer

from bioc import BioCAnnotation
from bioc import BioCReader
from bioc import BioCWriter

BIOC_IN = '..' + sep + 'test_input' + sep + 'example_input.xml'
BIOC_OUT = 'example_input_stemmed.xml'
DTD_FILE = '..' + sep + 'BioC.dtd'

def main():
    bioc_reader = BioCReader(BIOC_IN, dtd_valid_file=DTD_FILE)
    bioc_writer = BioCWriter(BIOC_OUT)
    stemmer = PorterStemmer()
    
    # Effectively read in input data; w/ test against BioC DTD
    bioc_reader.read()
    
    # Pass over basic data
    bioc_writer.collection = bioc_reader.collection
    
    # Get documents to manipulate
    documents = bioc_writer.collection.documents
    
    # Get text (by passage), tokenize and stem it
    annotation_id = 0
    for document in documents:
        
        for passage in document:
            stems_set = set([stemmer.stem(token) for 
                     token in wordpunct_tokenize(passage.text)])
            
            for stem in stems_set:
                annotation_id += 1
                
                bioc_annotation = BioCAnnotation()
                bioc_annotation.text = stem
                bioc_annotation.id = str(annotation_id)
                bioc_annotation.put_infon('surface form', 
                                          'stemmed token')
                passage.add_annotation(bioc_annotation)
    
    # Print to screen
    print(bioc_writer)
    
    # Write to disk
    bioc_writer.write()
    
if  __name__ == '__main__':
    main()
    
