class Color:
    def __init__(self):
        self.restore = "\033[00m"
        self.green = "\033[92m"
        self.blue = "\033[94m"
        self.red = "\033[91m"
        self.cyan = "\033[96m"
        self.purple = "\033[95m"
        self.yellow = "\033[93m"
        self.white = "\033[97m"

    @property
    def restore(self):
        return self._restore

    @restore.setter
    def restore(self, restore):
        self._restore = restore

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, green):
        self._green = green

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, blue):
        self._blue = blue

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, red):
        self._red = red

    @property
    def cyan(self):
        return self._cyan

    @cyan.setter
    def cyan(self, cyan):
        self._cyan = cyan

    @property
    def purple(self):
        return self._purple

    @purple.setter
    def purple(self, purple):
        self._purple = purple

    @property
    def yellow(self):
        return self._yellow

    @yellow.setter
    def yellow(self, yellow):
        self._yellow = yellow

    @property
    def white(self):
        return self._white

    @white.setter
    def white(self, white):
        self._white = white
