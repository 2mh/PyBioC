#!/usr/bin/env python

from bioc import BioCReader
from bioc import BioCWriter

test_file_1 = '../test_input/everything.xml'

def main():
    bioc_reader = BioCReader(test_file_1)
    bioc_reader.read()

    bioc_writer = BioCWriter()
    bioc_writer.collection = bioc_reader.collection
    print(bioc_writer)

    '''
    print('collection/source: ' + bioc_reader.collection.source)
    print('collection/date: ' + bioc_reader.collection.date)
    print('collection/key: ' + bioc_reader.collection.key)
    print('collection/infon: ' + str(bioc_reader.collection.infons))
    
    print('Number of documents: ' 
            + str(len(bioc_reader.collection.documents)))
            
    print('document info, infon position: '
            + str(bioc_reader.collection.documents[0].infons))
            
    
    document = bioc_reader.collection.documents[0]
    print document.passages[0].relations
    '''

if  __name__ =='__main__':
    main()
