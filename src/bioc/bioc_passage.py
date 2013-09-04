__all__ = ['BioCPassage']

from bioc_meta import MetaAnnotations, MetaInfons, MetaOffset, \
                      MetaRelations, MetaText

class BioCPassage:

    def __init__(self, passage=None):
        self.sentences = list()

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
