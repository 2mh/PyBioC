#!/usr/bin/env python

from bioc import BioCReader
from bioc import BioCWriter

test_file = '../test_input/PMID-8557975-simplified-sentences.xml'
dtd_file = '../test_input/BioC.dtd'

def main():
    bioc_reader = BioCReader(test_file, dtd_valid_file=dtd_file)
    bioc_reader.read()
    '''
    sentences = bioc_reader.collection.documents[0].passages[0].sentences
    for sentence in sentences:
        print sentence.offset
    '''

    bioc_writer = BioCWriter('output_bioc.xml')
    bioc_writer.collection = bioc_reader.collection
    bioc_writer.write()
    print(bioc_writer)

if  __name__ == '__main__':
    main()
