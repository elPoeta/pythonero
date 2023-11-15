class Hagman:
    def __init__(self, word="hello"):
        self.word = word.upper()
        self.fails = 0
        self.display = "_ " * len(self.word)
        self.limit_fail = 5;
        self.ascii_pics = [
             "   _____   \n  |     |  \n  |     |  \n  |        \n  |        \n  |        \n  |        \n__|__      \n",
             "   _____   \n  |     |  \n  |     |  \n  |     |  \n  |        \n  |        \n  |        \n__|__      \n",
             "   _____   \n  |     |  \n  |     |  \n  |     |  \n  |     O  \n  |        \n  |        \n__|__      \n",
             "   _____   \n  |     |  \n  |     |  \n  |     |  \n  |     O  \n  |     |  \n  |        \n__|__      \n",
             "   _____   \n  |     |  \n  |     |  \n  |     |  \n  |     O  \n  |    /|\ \n  |        \n__|__      \n",
             "   _____   \n  |     |  \n  |     |  \n  |     |  \n  |     O  \n  |    /|\ \n  |    / \ \n__|__      \n",
        ]
    
    def print_pics(self, pos=0):
        print(self.ascii_pics[pos])    