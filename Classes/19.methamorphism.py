from abc import ABC, abstractmethod


class UIControl:
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('TextBox')


class DropDownList(UIControl):
    def draw(self):
        print('DropDownList')


# def draw(control):
#     control.draw()

def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
TextBoxL = TextBox()

print(isinstance(ddl, DropDownList))
print(isinstance(TextBoxL, TextBox))

# draw(ddl)

# we use this method 'methamorphism' for making an interface
draw([ddl, TextBoxL])
