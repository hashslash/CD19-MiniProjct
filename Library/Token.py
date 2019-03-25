class Token:
    id = ''
    lexeme = ""

    def __init__(self, tid, lexeme):
        self.id = tid
        self.lexeme = lexeme

    def __eq__(self, o: object) -> bool:
        if o.id == self.id:
            return True
        else:
            return False

    def __str__(self):
        return self.id

    def __hash__(self):
        __hash = 0
        for i in self.id:
            __hash += ord(i)
        return __hash
