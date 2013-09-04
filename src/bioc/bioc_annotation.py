__all__ = ['BioCAnnotation']

from meta import _MetaId, _MetaInfons, _MetaText

class BioCAnnotation(_MetaId, _MetaInfons, _MetaText):

    def __init__(self, annotation=None):
        self.locations = list()

        if annotation is not None:
            self.id = annotation.id
            self.infons = annotation.infons
            self.locations = annotation.locations
            self.text = self.text

    def __str__():
        s = 'id: ' + self.id + '\n'
        s += str(self.infons) + '\n'
        s += 'locations: ' + str(self.locations) + '\n'
        s += 'text: ' + self.text + '\n'

        return s

    def clear_locations():
        self.locations = list()

    def add_location(location):
        self.locations.append(location)
