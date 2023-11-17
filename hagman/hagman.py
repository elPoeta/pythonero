class Hagman:
    def __init__(self, word="hello", limit_fail=5):
        self.word = ' '.join(s for s in list(word.upper()))        
        self.fails = 0
        self.display = "_ " * len(self.word)
        self.limit_fail = limit_fail
        self.letters = []
        self.ascii_pics = self.set_ascii_pics()

    def set_ascii_pics(self):
        first_common_pics = "   _____       *** Py-Hagman *** \n  |     |  \n  |     |     Fails: %%fails%%,  Letters: %%letters%%  \n  |     "
        last_common_pic = "__|__        %%display%% \n"
        return [
             f"{first_common_pics}\n  |        \n  |        \n  |        \n{last_common_pic}",
             f"{first_common_pics}|  \n  |        \n  |        \n  |        \n{last_common_pic}",
             f"{first_common_pics}|  \n  |     O  \n  |        \n  |        \n{last_common_pic}",
             f"{first_common_pics}|  \n  |     O  \n  |     |  \n  |        \n{last_common_pic}",
             f"{first_common_pics}|  \n  |     O  \n  |    /|\ \n  |        \n{last_common_pic}",
             f"{first_common_pics}|  \n  |     O  \n  |    /|\ \n  |    / \ \n{last_common_pic}",
        ]
        
    def print_pics(self, pos=0):
        print(self.ascii_pics[pos]
              .replace('%%display%%', self.display)
              .replace('%%fails%%', str(self.fails))
              .replace('%%letters%%', str(self.letters)))    