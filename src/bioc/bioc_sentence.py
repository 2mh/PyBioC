__all__ = ['BioCSentence']


from bioc_meta import MetaAnnotations, MetaInfons, MetaOffset, \
                      MetaRelations, MetaText
                      

class BioCSentence(MetaAnnotations, MetaInfons, MetaOffset, 
                   MetaRelations, MetaText):
    
    def __init__(self, sentence=None):

        if sentence is not None:
            self.offset = sentence.offset
            self.text = sentence.text
            self.infons = sentence.infons
            self.annotations = sentence.annotations
            self.relations = sentence.relations

    def __str__(self):
        s = 'offset: ' + str(self.offset) + '\n'
        s += 'infons: ' + str(self.infons) + '\n' # TBD
        s += 'text: ' + str(self.text) + '\n' # TBD
        s += str(self.annotations) + '\n' # TBD
        s += str(self.relations) + '\n' # TBD

        return s
