from Library.Token import Token


class LexicalAnalyser:
    def __init__(self, tids, indata):
        pass

    def get_next_token(self):
        pass


'''
mydict = {
    'operators':{
        'arithmetic':('+','-','/','*','='),
        'assignment':'=',
        'inc_dic':('++','--')
    },
    'comments':{
        'single_line':'//',
        'multipleLineStart':'/*',
        'multipleLineEnd':'*/'
    },
    'header':{
        'Standard Input Output':'stdio.h',
        'Standard Library':'stdlib.h'
    },
    'delimiter':{
        'semicolon':';'
    },
    'blocks':{
        'curly_open_brace':'{',
        'curly_closed_brace':'}',
        'open_paranthesis':'(',
        'closed_paranthesis':')'
    },
    'built_in_functions':{
        'Print':'printf',
        'Scan':'scanf',
        'Main_function':'main'
    }
}
def istoken(lexeme):
    for name in mydict.keys():
        for token in mydict[name]:
            for value in mydict[name][token]:
                if (value == lexeme):
                    print(token)
'''
