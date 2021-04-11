class TagCloud():
    def __init(self):
        self.__tags = {}  # in order to make 'tag' attribute private for the class and can
        # and can not been used out side the class

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()

print(cloud.__dict__)

cloud.add('Python')
cloud.add('Python')
cloud.add('Python')

print(cloud.__tags['PYTHON'])
