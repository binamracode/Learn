class TagCloud:
    def __init__(self, tags={}):
        self.__tags = tags

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags.items())

    def __str__(self):
        return str(self.__tags)

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def remove(self, tag):
        if tag not in self.__tags:
            raise KeyError(f"{tag} not found in the TagCloud object.")
        del self.__tags[tag]


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("java")
cloud.add("java")
cloud.add("java")
print(cloud)