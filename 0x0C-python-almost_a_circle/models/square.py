#!/usr/bin/python3
""" Square  """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ rectangle definition """

    def __init__(self, size, x=0, y=0, id=None):
        ''' calling super on Rectangle '''

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        ''' size '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        ''' str '''
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        ''' update args in the class '''

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        '''
        setting each arg to its appropriate item
        '''
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        except IndexError:
            pass

    def to_dictionary(self):
        ''' dictionary '''
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
