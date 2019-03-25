class Stack:
    __stack = []

    def __init__(self):
        pass

    def __str__(self):
        s = ""
        for i in self.__stack:
            s += str(i) + " "
        return s

    def __len__(self):
        return len(self.__stack)

    def push(self, data):
        self.__stack.append(data)

    def pop(self):
        if len(self.__stack) == 0:
            return None
        else:
            top = self.__stack[-1]
            self.__stack = self.__stack[:-1]
            return top

    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False
