from Library.Token import Token


class LexicalAnalyser:
    pointer = 0

    def __init__(self, tids, indata):
        self.__data = indata
        self.__tid_s = tids

    def get_next_token(self):
        # print("p->", self.pointer)
        if self.pointer >= len(self.__data):
            return None
        matched = False
        tid = None
        ln = 1
        while True:
            # print("len->", ln)
            if not matched:
                for i in self.__tid_s:
                    # print("check-", self.__data[self.pointer:self.pointer + ln], i)
                    if i.matches(self.__data[self.pointer:self.pointer + ln]):
                        tid = i
                        matched = True
                        break
            else:
                flag = False
                # print("match check-", self.__data[self.pointer:self.pointer + ln])
                for i in self.__tid_s:
                    if i.matches(self.__data[self.pointer:self.pointer + ln]):
                        tid = i
                        flag = True
                        break
                if not flag:
                    tt = Token(tid.id, self.__data[self.pointer:self.pointer + ln - 1])
                    self.pointer = self.pointer + ln - 1
                    # print("matched 1", tt.id, tt.lexeme)
                    return tt

            if self.pointer + ln <= len(self.__data):
                ln += 1
                continue
            else:
                if matched:
                    tt = Token(tid.id, self.__data[self.pointer:self.pointer + ln - 1])
                    self.pointer = self.pointer + ln - 1
                    # print("matched 2", tt.id, tt.lexeme)
                    return tt
                else:
                    if self.pointer != len(self.__data) - 1:
                        self.pointer += 1
                        print("\nWarning:Panic Mode:Skipped Token\'"+ self.__data[self.pointer - 1] + "\'")
                        return self.get_next_token()
                    else:
                        self.pointer += 1
                        print("Error out of chars")
                        exit(1)
