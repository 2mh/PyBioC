#!/usr/bin/env python

from bioc import BioCReader
from bioc import BioCWriter

test_file_1 = '../test_input/everything-sentence.xml'

def main():

    bioc_reader = BioCReader(test_file_1)
    bioc_reader.read()

    bioc_writer = BioCWriter()
    bioc_writer.collection = bioc_reader.collection
    print(bioc_writer)

if  __name__ =='__main__':
    main()
