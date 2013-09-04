__all__ = []

class _MetaIter:

    '''
    def next(self):
        for elem in self._iterdata: # Requires self._iterdata to exist
            try:
                yield elem
            except StopIteration:
                break
    '''

    def __iter__(self):
        return self._iterdata().__iter__()
