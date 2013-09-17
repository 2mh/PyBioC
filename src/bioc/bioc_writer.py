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
        nav = self.root_tree.find('document')
        for document in self.collection.documents:
            nav_doc = nav
            
            # id
            nav = nav.find('id')
            nav.text = document.id

            # infon*
            for infon_key, infon_val in document.infons.items():
                infon_elem = E('infon')
                infon_elem.attrib['key'] = infon_key
                infon_elem.text = infon_val
                nav.addnext(infon_elem)
                nav = nav.getnext() # Go to <infon>
            
            # passage+
            for passage in document.passages:
                nav = nav.getnext() # Go to <passage>
                nav_passage = nav
                
                # infon*
                for infon_key, infon_val in passage.infons.items():
                    infon_elem = E('infon')
                    infon_elem.attrib['key'] = infon_key
                    infon_elem.text = infon_val
                    nav.insert(0, infon_elem)
                    
                # offset
                nav = nav.find('offset')
                nav.text = passage.offset
                
                # sentence | text?, annotation*
                if passage.has_sentence():
                    # TBD
                    pass
                else:
                    # text?, annotation*
                    nav.addnext(E('text'))
                    nav = nav.getnext() # Go to <text>
                    nav.text = passage.text
                    nav.addnext(E('annotation'))
                    nav = nav.getnext() # Go to <annotation>
                    
                    for annotation in passage.annotations:
                        nav.attrib['id'] = annotation.id
                        
                        # infon*
                        for infon_key, infon_val \
                                        in annotation.infons.items():
                            infon_elem = E('infon')
                            infon_elem.attrib['key'] = infon_key
                            infon_elem.text = infon_val
                            nav.insert(0, infon_elem)
                        # location*
                        for location in annotation.locations:
                            location_elem = E('location')
                            location_elem.attrib['offset'] = \
                                                        location.offset
                            location_elem.attrib['length'] = \
                                                        location.length
                            nav.append(location_elem)
                        # text
                        text_elem = E('text')
                        text_elem.text = annotation.text
                        nav.append(text_elem)
                
                # relation*
                for relation in passage.relations:
                    nav_passage.append(E('relation'))
                    nav = nav_passage.getchildren()[-1]
                    nav.attrib['id'] = relation.id
                    
                    # infon*
                    for infon_key, infon_val in relation.infons.items():
                        infon_elem = E('infon')
                        infon_elem.attrib['key'] = infon_key
                        infon_elem.text = infon_val
                        nav.insert(0, infon_elem)
                        
                    # node*
                    for node in relation.nodes:
                        nav.append(E('node'))
                        nav = nav.getchildren()[-1]
                        nav.attrib['refid'] = node.refid
                        nav.attrib['role'] = node.role
                    
                    
            # relation*
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
