__all__ = ['BioCReader']

from bioc_collection import BioCCollection
from bioc_document import BioCDocument
from bioc_passage import BioCPassage
from bioc_sentence import BioCSentence

class BioCReader:
    def __init__(self):
        self.collection = None
        self.document = None
        self.passage = None
        self.sentence = None
        self.fh = None # File Handler
        int state = -1
        is_sentence_level = False
        is_document_level = False
        is_passage_level = False
