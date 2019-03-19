from re import compile, match

from _pytest.compat import NoneType


class TokenIdentifier:
    id = ''
    regex = ""

    def __init__(self, tid, regex):
        self.id = tid
        self.regex = regex

    def __eq__(self, o: object) -> bool:
        try:
            return self.id == object.id
        except:
            return False

    def __hash__(self):
        __hash = 0
        for i in self.id:
            __hash += ord(i)
        return __hash

    def __str__(self):
        return str(self.id)

    def matches(self, string):
        matcch = match(self.regex, string)
        try:
            if matcch.group() == string:
                # print(matcch.group(), string)
                return True
            else:
                return False
        except:
            return False
