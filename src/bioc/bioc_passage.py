__all__ = ['BioCPassage']

from meta import _MetaAnnotations, _MetaInfons, _MetaOffset, \
                 _MetaRelations, _MetaText

class BioCPassage(_MetaAnnotations, _MetaOffset, _MetaText,
                  _MetaRelations, _MetaInfons):

    def __init__(self, passage=None):
        
        self.offset = -1
        self.text = ''
        self.infons = dict()
        self.sentences = list()
        self.annotations = list()
        self.relations = list()

        if passage is not None:
            self.offset = passage.offset
            self.text = passage.text
            self.infons = passage.infons
            self.sentences = passage.sentences
            self.annotations = passage.annotations
            self.relations = passage.relations

    def size(self):
        return len(self.sentences)

    # TBD: Sentence parts missing
