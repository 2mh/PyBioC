__all__ = ['BioCReader']

from lxml import etree

from bioc_annotation import BioCAnnotation
from bioc_collection import BioCCollection
from bioc_document import BioCDocument
from bioc_location import BioCLocation
from bioc_passage import BioCPassage
from bioc_sentence import BioCSentence
from bioc_node import BioCNode
from bioc_relation import BioCRelation

class BioCReader:

    def __init__(self, source): # Source can be different stuff
        
        self.collection = None
        self.document = None
        self.passage = None
        self.annotation = None
        self.sentence = None
        self.relation = None
        self.xml_iter = etree.parse(source).getiterator()

   # XXX: TBC
    def close():
        pass

    def read(self):
        elem = next(self.xml_iter)

        if elem.tag == 'collection':
            self.collection = BioCCollection()
            self._read_collection_meta()

    def _read_collection_meta(self):

        for elem in self.xml_iter:
            if elem.tag == 'source':
                self.collection.source = elem.text 
            elif elem.tag == 'date':
                self.collection.date = elem.text
            elif elem.tag == 'key':
                self.collection.key = elem.text
            # 0 or more <infon> are possible.
            elif elem.tag == 'infon':
                infon_key = self._get_infon_key(elem)
                self.collection.put_infon(infon_key, elem.text)
            elif elem.tag == 'document':
                self._read_document()
            else:
                break # Should never be reached.

    def _read_document(self):
        self.document = BioCDocument()
        self.document.id = next(self.xml_iter).text # Expect <id>

        for elem in self.xml_iter:
            if elem.tag == 'infon':
                infon_key = self._get_infon_key(elem)
                self.document.put_infon(infon_key, elem.text)
            elif elem.tag == 'passage':
                self._read_passage()
            elif elem.tag == 'relation':
                self.relation = BioCRelation()
                self.relation.id = self._get_id(elem)
                self._read_relation()
                self.document.add_relation(self.relation)
            else:
                break # Go to possible next <document>.

        self.collection.add_document(self.document)

    def _read_passage(self):
        self.passage = BioCPassage()

        for elem in self.xml_iter:
            
            print elem.tag

            # 0 or more <infon> possible
            if elem.tag == 'infon':
                infon_key = self._get_infon_key(elem)
                self.passage.put_infon(infon_key, elem.text)
            elif elem.tag == 'offset':
                self.passage.offset = elem.text
            # Expect either <sentence> or
            # <text> and/or <annotation>
            elif elem.tag == 'sentence':
                self.sentence = BioCSentence()
                self._read_sentence() 
                self.passage.add_sentence(self.sentence) # XXX: TBD
            elif elem.tag == 'text':
                self.passage.text = elem.text
            elif elem.tag == 'annotation':
                self.annotation = BioCAnnotation() 
                self.annotation.id = self._get_id(elem)
                self._read_annotation()
                self.passage.add_annotation(self.annotation)
            elif elem.tag == 'relation' \
                            and elem.getparent().tag == 'passage':
                self.relation = BioCRelation()
                self.relation.id = self._get_id(elem)
                self._read_relation()
                self.passage.add_relation(self.relation)
            else:
                break

        self.document.add_passage(self.passage)

    def _read_sentence(self):
        '''
        <!elemENT   sentence ( infon*, offset, text?, 
                    annotation*, relation* ) >
        '''
        for elem in self.xml_iter:
            if elem.tag == 'infon': 
                infon_key = self._get_infon_key(elem)
                self.sentence.put_infon(infon_key, elem.text)
            elif elem.tag == 'offset':
                self.sentence.offset = elem.text
            elif elem.tag == 'text':
                self.sentence.text = elem.text
            elif elem.tag == 'annotation':
                self.annotation = BioCAnnotation()
                self.annotation.id = self._get_id(elem)
                self._read_annotation()
                self.sentence.add_annotation(self.annotation)
            elif elem.tag == 'relation':
                self.relation = BioCRelation()
                self.relation.id = self._get_id(elem)
                self._read_relation()
                self.sentence.add_relation(self.relation)
            else:
                break

    def _read_relation(self):
        
        for elem in self.xml_iter:
            if elem.tag == 'infon':
                infon_key = self._get_infon_key(elem)
                self.relation.put_infon(infon_key, elem.text)
            elif elem.tag == 'node':
                node = BioCNode()
                node.refid = elem.attrib['refid'] 
                node.role = elem.attrib['role']
                self.relation.add_node(node)
            else:
                break

    def _read_annotation(self):
        
        for elem in self.xml_iter:
            if elem.tag == 'infon':
                infon_key = self._get_infon_key(elem)
                self.annotation.put_infon(infon_key, elem.text)
            elif elem.tag == 'location':
                location = BioCLocation()
                location.offset = elem.attrib['offset']
                location.length = elem.attrib['length']
                self.annotation.add_location(location)
            elif elem.tag == 'text':
                self.annotation.text = elem.text
                break
                
    def _get_infon_key(self, elem):
        return elem.attrib['key']

    def _get_id(self, elem):
        return elem.attrib['id']
