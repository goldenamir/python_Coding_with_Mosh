# here we are going to have a concept of reading from 'stream' not from a 'file' which is bit different

# creating costum function
class InvalidOperationError(Exception):
    pass


class Stream():
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open.')
        self.opened = True

    def closed(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already close.')
        self.opened = False


# define a class of stream
class FileStream(Stream):
    def read(self):
        print('reading data from file.')


class NetworkStream(Stream):
    def read(self):
        print('reading from a network')
