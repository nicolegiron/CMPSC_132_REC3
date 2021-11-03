# Recitation Activity #3
# I completed this code in room: I need help to start

class Button:
    '''
        >>> x = Button(3, 'A')
        >>> y = Button(8, 't')
        >>> x
        A
        >>> print(x)
        Button A at position 3
        >>> y*5
        'ttttt'
    '''

    def __init__(self, position, key):
        self.position = position
        self.key = key
        self.pressed = 0

    def __repr__(self):
        return "{}".format(self.key)

    def __str__(self):
        return "Button {} at position {}".format(self.key, self.position)

    def __mul__(self, other):
        return self.key * other

    def __rmul__(self, other):
        return self.key * other



class Keyboard(Button):
    """
        A sequence of Button objects in a Python list, storing these Buttons in a dictionary where the keys will be
        integers that represent the position on the Keyboard, and the values will be the respective Button objects.
        >>> b1 = Button(0, "H")
        >>> b2 = Button(1, "i")
        >>> b3 = Button(3, "m")
        >>> b4 = Button(4, "o")
        >>> b5 = Button(5, " ")
        >>> k = Keyboard([b1, b2, b3, b4, b5])
        >>> k.buttons[0].key
        'H'
        >>> k.press(1)
        'i'
        >>> k._type([0, 1])
        'Hi'
        >>> k._type([1, 0])
        'iH'
        >>> k._type([0, 1, 5, 3, 4, 3])
        'Hi mom'
        >>> b1.pressed
        3
        >>> b2.pressed
        4
    """

    def __init__(self, button_list):
        self.buttons = {}
        for b in button_list:
            self.buttons[b.position] = b


    def press(self, info):
        """
            Parameters:
              info: position of the button pressed
            Returns:
               Button's output
        """
        self.buttons[info].pressed += 1
        return self.buttons[info].key



    def _type(self, typing):
        """
            Parameters:
              typing: list of positions of buttons pressed
            Returns:
               Total output
        """
        total = ""
        for value in typing:
            if value in self.buttons:
                self.buttons[value].pressed += 1
                total += self.buttons[value].key
        return total
