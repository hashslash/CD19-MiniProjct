class Production:

    def __init__(self, id, variable, rhs):
        self.id = id
        self.variable = variable
        self.rhs = rhs

    def __str__(self):
        prod = str(self.variable) + " > "
        for i in self.rhs:
            prod += str(i) + " "
        return prod
