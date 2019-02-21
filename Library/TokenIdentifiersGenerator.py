from Library.TokenIdentifier import TokenIdentifier


class TokenIdentifiersGenerator:
    token_identifier_list = []

    def __init__(self, stream):
        self.stream = stream
        self.__generate()

    def token_identifiers(self):
        return self.token_identifier_list

    def __generate(self):
        for i in self.stream:
            id, regex = i.split()
            tokenid = TokenIdentifier(id, regex)
            self.token_identifier_list.append(tokenid)
