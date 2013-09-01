__all__ = [
    'MetaAnnotations', 'MetaId', 'MetaInfons', 'MetaOffset', 'MetaRelations',
    'MetaText'
    ]

class MetaAnnotations:
    annotations = list()

    def annotation_iterator(self):
        return self.annotations.iterator() # TBD

    def clear_annotations(self):
        self.annotations = list()

    def add_annotation(self, annotation):
	self.annotations.append(annotation)

    def remove_annotation(self, annotation): # Can be int or obj
        if type(annotation) is int:
            self.annotations.remove(self.annotations[annotation])
        else:
            self.annotations.remove(annotation) # TBC

class MetaInfons:
    infons = dict()

    def put_infon(self, key, val):
        infons[key] = val 

    def remove_infon(self, key):
        del(infons[key]) 

    def clear_infons(self):
        self.infons = dict()

class MetaOffset:
    offset = -1

class MetaRelations:
    relations = list()

    def relation_iterator(self):
        return self.relations.iterator() # TBD

    def clear_relations(self):
        self.relations = list()

    def add_relation(self, relation):
        self.relations.append(relation)

    def remove_relation(self, relation): # Can be int or obj
        if type(relation) is int:
            self.relations.remove(self.relations[relation])
        else:
            self.relations.remove(relation) # TBC

class MetaText:
    text = ''

class MetaId:
    id = ''
