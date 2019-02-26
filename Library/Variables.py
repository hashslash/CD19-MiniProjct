class Variable:
    name = ""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        try:
            return self.name == other.name
        except:
            return False

    def __hash__(self):
        hash = 0
        for i in self.name:
            hash += ord(i)
        return hash
