import re


class TokenIdentifier:
    id = ''
    regex = ""

    def __init__(self, tid, regex):
        self.id = tid
        self.regex = regex

    def __eq__(self, o: object) -> bool:
        if o.id == self.id:
            return True
        else:
            return False

    def __str__(self):
        return self.id + "(" + self.regex + ")"

    def matches(self, string):
        return self.regex.match(string)
