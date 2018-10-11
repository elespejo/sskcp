class Generation:
    def __init__(self):
        self.gens = []

    def add(self, generator):
        self.gens.append(generator)
        return self

    def generate(self, where):
        for g in self.gens:
            g.start(where)
