''' In Python, we can use the built-in classes for inehertating '''


class Text(str):
    def duplicate(self):
        return self + self


text = Text('Python')
print(text.lower())
print(text.duplicate())

''' Extending the built-in class '''


class TrackableList(list):
    def append(self, object):
        print('Append claled')
        super().append(object)


list = TrackableList()
list.append('1')
