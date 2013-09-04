__all__ = ['BioCLocation']

from bioc_meta import MetaOffset

class BioCLocation(MetaOffset):

    def __init__(self, location=None):
        self.length = 0

        if location is not None:
             self.offset = location.offset
             self.length = location.length 

    def __str__(self):
        s = str(self.offset) + ':' + str(self.length)

        return s
