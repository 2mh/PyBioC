#!/usr/bin/env python

from bioc import BioCReader
from bioc import BioCWriter

test_file_1 = '../test_input/PMID-8557975-simplified-sentences.xml'

def main():


    bioc_reader = BioCReader(test_file_1)
    bioc_reader.read()
    '''
    sentences = bioc_reader.collection.documents[0].passages[0].sentences
    for sentence in sentences:
        print sentence.offset
    '''

    bioc_writer = BioCWriter()
    bioc_writer.collection = bioc_reader.collection
    print(bioc_writer)

if  __name__ == '__main__':
    main()
