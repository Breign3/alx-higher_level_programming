#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base

class Rectangle(Base):
    """
        class Rectangle implements Base.
        Methods: __init__()
    """

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """initialization of Rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        Return the formation or format of the string
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """
        Get function for __width
        Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set function for width.
        Args:(int) value: value to be set.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        get function for height
        Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter function for height
        Args:(int)Value: value to be set.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        get function for x.
        Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        set function for x.
        Args:value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value
    
    @property
    def y(self):
        """
        get function for y
        Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter function for y
        Args: value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        '''
        Return area of this rectangle.
        '''
        return self.width * self.height

    def display(self):
        """
        prints # shape of the rectangle
        """
        print('\n'*self.y, end='')
        for lst in range(self.height):
            print(' '*self.x + '#'*self.width)

    def update(self, *args, **kwargs):
        """
            Update reactangle attributes
            kwargs is skipped if args is not empty
            Args: args -  variable number of no-keyword args
                  kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle.
        """
        return {"id": self.id,"width": self.width,"height": self.height,"x": self.x,
            "y": self.y}
