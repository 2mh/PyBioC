__all__ = ['BioCWriter']

from lxml.builder import E
from lxml.etree import tostring

class BioCWriter:
    
    def __init__(self, filename=None, collection=None):
        
        self.root_tree = E('collection', # 1
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
        self.annot_tree = E('annotation',
                            E('text') # 1
                        )
        self.sent_tree = E('sentence',
                            E('offset') # 1
                        )
                        
        self.collection = None
        self.doctype = '''<?xml version='1.0' encoding='UTF-8'?>'''
        self.doctype += '''<!DOCTYPE collection SYSTEM "BioC.dtd">'''
        
        if collection is not None:
            self.collection = collection
        
        if filename is not None:
            self.filename = filename
        
    def __str__(self):
        
        self.build()
        s = tostring(self.root_tree, 
                    pretty_print=True, 
                    doctype=self.doctype)
                    
        return s
        
    def build(self):
        self._build_collection()
        #self._build_collection_infon(self.root_tree)
        #self._build_collection_document()
        
    def _build_collection(self):
        
        # source, date, key
        nav = self.root_tree.find('source')
        nav.text = self.collection.source
        nav = self.root_tree.find('date')
        nav.text = self.collection.date
        nav = self.root_tree.find('key')
        nav.text = self.collection.key
        
        # infon*
        for infon_key, infon_val in self.collection.infons.items():
            infon_elem = E('infon')
            infon_elem.attrib['key'] = infon_key
            infon_elem.text = infon_val
            self.root_tree.insert(self.root_tree.index(nav) + 1, 
                                infon_elem)
                                
        # document+
        pass
        
   
    '''
    def _build_collection_infon(self, tree):
        pass
                
    def _build_collection_document(self):
        pass
        
    def _build_infon(self):
        pass
        
    def _build_document(self):
        pass
        
    def _build_passage(self):
        pass
    
    def _build_relation(self):
        pass
        
    def _build_offset(self):
        pass
        
    def _build_relation(self):
        pass
        
    def _build_text(self):
        pass
        
    def _build_sentence(self):
        pass
    
    def _build_id(self):
        pass
        
    def _build_annotation(self):
        pass
        
    def _build_annotation(self):
        pass
        
    def _build_node(self):
        pass
    
    def write(self):
        #f = open(self.filename, 'w')
        pass
    '''
