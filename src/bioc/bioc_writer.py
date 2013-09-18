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
        self._build_infons(nav, self.collection.infons, pos='next')
                                
        # document+
        nav = self.root_tree.find('document')
        for document in self.collection.documents:
            nav_doc = nav
            
            # id
            nav = nav.find('id')
            nav.text = document.id

            # infon*
            self._build_infons(nav, document.infons)
            
            # passage+
            for passage in document.passages:
                nav = nav.getnext() # Go to <passage>
                nav_passage = nav
                
                # infon*
                self._build_infons(nav, passage.infons)
                
                # offset
                nav = nav.find('offset')
                nav.text = passage.offset
                
                # sentence | text?, annotation*
                if passage.has_sentence():
                    # sentence
                    for sentence in passage.sentences:
                        nav.addnext(E('sentence'))
                        nav = nav.getnext() # Go to <sentence>
                        nav_sentence = nav
                        
                        # infon*
                        self._build_infons(nav, sentence.infons)

                        # offset
                        nav.append(E('offset'))
                        nav = nav.find('offset')
                        nav.text = sentence.text
                        # text?
                        if len(sentence.text) > 0:
                            nav.addnext(E('text'))
                            nav = nav.getnext()
                            nav.text = sentence.text
                        # annotation*
                        for annotation in sentence.annotations:
                            nav.addnext(E('annotation'))
                            nav = nav.getnext()
                            # infon*
                            
                            self._build_infons(nav, annotation.infons)

                            # location
                            self._build_locations(nav, 
                                            annotation.locations)
                            
                            # text
                            nav.append(E('text'))
                            nav = nav.find('text')
                            nav.text = annotation.text
                        # relation*
                        for relation in sentence.relations:
                            nav_sentence.append(E('relation'))
                            nav = nav_sentence.getchildren()[-1]
                            nav.attrib['id'] = relation.id
                    
                            # infon*
                            self._build_infons(nav, relation.infons)
                        
                            # node*
                            self._build_nodes(nav, relation.nodes)
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
                        self._build_infons(nav, annotation.infons)

                        # location*
                        self._build_locations(nav, 
                                            annotation.locations)
                            
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
                    self._build_infons(nav, relation.infons)
                        
                    # node*
                    self._build_nodes(nav, relation.nodes)
                    
                    
            # relation*
            nav = nav_doc
            print len(document.relations)
            for relation in document.relations:
                print relation
   
   
    def _build_infons(self, nav, infons, pos=None):
        
        for infon_key, infon_val in infons.items():
            infon_elem = E('infon')
            infon_elem.attrib['key'] = infon_key
            infon_elem.text = infon_val

            if pos == 'next':
                nav.addnext(infon_elem)
            else:
                nav.append(infon_elem)
   
            
    def _build_nodes(self, nav, nodes):
        
        for node in nodes:
            nav.append(E('node'))
            nav = nav.getchildren()[-1]
            nav.attrib['refid'] = node.refid
            nav.attrib['role'] = node.role
        
            
    def _build_locations(self, nav, locations):
        
        for location in locations:
            location_elem = E('location')
            location_elem.attrib['offset'] = location.offset
            location_elem.attrib['length'] = location.length
            nav.append(location_elem)
