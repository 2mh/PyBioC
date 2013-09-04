__all__ = []

class _MetaIter:
    def __iter__(self):
        self.next()
