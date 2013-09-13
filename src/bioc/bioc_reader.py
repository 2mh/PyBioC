__all__ = ['BioCReader']

from bioc_collection import BioCCollection
from bioc_document import BioCDocument
from bioc_passage import BioCPassage
from bioc_sentence import BioCSentence

class BioCReader:

    def __init__(self, file_object=None, file_name=None)
        self.collection = None
        self.document = None
        self.passage = None
        self.sentence = None
        self.xml_object = None
        int state = 0
        is_sentence_level = False
        is_document_level = False
        is_passage_level = False

   # XXX: TBD
   def close():
       pass 
