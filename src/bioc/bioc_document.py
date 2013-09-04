__all__ = ['BioCDocument']

from bioc_meta import MetaId, MetaInfons, MetaRelations

class BioCDocument(MetaId, MetaInfons, MetaRelations):

    def __init__(self, document=None):

        self.passages = list()

        if document is not None:
            self.id = document.id
            self.infons = document.infons
            self.relations = document.relations
            self.passages = document.passages

    def __str__(self):
        s = 'id: ' + self.id + '\n'
        s += 'infon: ' + self.infons + '\n'
        s += str(self.passages) + '\n'
        s += str(self.relations) + '\n'

        return s

    def get_size(self):
        return self.passages.size() # As in Java BioC

    def clear_passages(self):
        self.passages = list()

    def add_passage(self, passage):
        self.annotations.append(passage)

    def remove_passage(self, passage):
        if type(passage) is int:
            self.passages.remove(self.passages[passage])
        else:
            self.passages.remove(passage) # TBC

    def iterator(self):
        pass # TBD: To iterate over passages
