class Stack:
    __stack = []

    def push(self, data):
        self.__stack.append(data)

    def pop(self):
        if len(self.__stack) == 0:
            return None
        else:
            top = self.__stack[-1]
            self.__stack = self.__stack[:-1]
            return top
