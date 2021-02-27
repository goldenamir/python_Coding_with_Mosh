''' In python there is no need to have UIControl as below to iterate in the draw function, since
the function can iterate in any iterable object (if it is iterable). So, we remove UI control which 
uses methamorphism idea.j'''


# we are removing this function if we want to iterate in the iterable object
# class TextBox(UIControl):
#     def draw(self):
#         print('TextBox')


class DropDownList(UIControl):
    def draw(self):
        print('DropDownList')


# def draw(control):
#     control.draw()

def draw(controls):
    for control in controls:
        control.draw()
