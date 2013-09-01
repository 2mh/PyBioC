__all__ = ['BioCNode']

class BioCNode:

    def __init__(self, node=None):
        self.refid = ''
        self.role = ''

        if node is not None:
            self.refid = node.refid
            self.role = node.role

    def __str__(self):
         s = 'refid: ' + self.refid + '\n'
         s += 'role: ' + self.role + '\n'

         return s
