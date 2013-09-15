__all__ = ['BioCWriter']

from lxml.builder import E
from lxml.etree import tostring

class BioCWriter:
    
    def __init__(self, filename, collection=None):
        
        self.root = E('collection', # 1
                        E('source'), # 1
                        E('date'), # 1
                        E('key'), # 1
                        E('document', # >= 1
                            E('id'), # 1
                            E('passage', # >= 1
                                E('offset') # 1
                            )
                        )
                    )
        self.annotation = E('annotation', id='',
                            E('text') # 1
                        )
        self.sentence = E('sentence',
                            E('offset') # 1
                        )
        self.filename = filename
        self.collection = None
        self.doctype = '''<?xml version='1.0' encoding='UTF-8'?>'''
        self.doctype += '''<!DOCTYPE collection SYSTEM "BioC.dtd">'''
        
        if collection is not None:
            self.collection = collection
        
    def __str__(self):
        s = tostring(self.root, pretty_print=True, doctype=self.doctype)
        return s
        
    def build(self):
        pass
        
    def write(self):
        #f = open(self.filename, 'w')
        pass
