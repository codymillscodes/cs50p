class Halfling:
    def __init__(
        self,
        potatoes=0,
        destiny=0,
        orcs=0,
        danger_level=1,
        max_potatoes=10,
        max_destiny=10,
        max_orcs=10,
    ):
        self._destiny = destiny
        self._potatoes = potatoes
        self._orcs = orcs
        self._danger_level = danger_level
        self._turn = 1
        self._state = "playing"
        self._max_potatoes = max_potatoes
        self._max_destiny = max_destiny
        self._max_orcs = max_orcs

    # overload
    def __str__(self):
        return f"Potato({self._potatoes}, {self._destiny}, {self._orcs}, {self._danger_level}, {self._max_potatoes}, {self._max_destiny}, {self._max_orcs})"

    # Getters and setters
    @property
    def destiny(self):
        return self._destiny

    @destiny.setter
    def destiny(self, n):
        if n < 0:
            self._destiny = 0
        elif n > self._max_destiny:
            self._destiny = self._max_destiny
        else:
            self._destiny = n

    @property
    def potatoes(self):
        return self._potatoes

    @potatoes.setter
    def potatoes(self, n):
        if n <= 0:
            self._potatoes = 0
        elif n > self._max_potatoes:
            self._potatoes = 10
        else:
            self._potatoes = n

    @property
    def orcs(self):
        return self._orcs

    @orcs.setter
    def orcs(self, n):
        if n <= 0:
            self._orcs = 0
        elif n > self._max_orcs:
            self._orcs = 10
        else:
            self._orcs = n

    @property
    def danger_level(self):
        return self._danger_level

    @danger_level.setter
    def danger_level(self, n):
        self._danger_level = n

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, n):
        self._turn = n

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, s):
        if s not in ["playing", "win", "lose"]:
            s = "playing"
        else:
            self._state = s

    def get_max_points(self, stat):
        if stat == "potatoes":
            return self._max_potatoes
        if stat == "destiny":
            return self._max_destiny
        if stat == "orcs":
            return self._max_orcs

    @property
    def stats(self):
        return {
            "potatoes": self._potatoes,
            "max_potatoes": self._max_potatoes,
            "destiny": self._destiny,
            "max_destiny": self._max_destiny,
            "orcs": self._orcs,
            "max_orcs": self._max_orcs,
            "turn": self._turn,
            "danger_level": self._danger_level,
        }

    def reset(self):
        self._destiny = 0
        self._potatoes = 0
        self._orcs = 0
        self._danger_level = 1
        self._turn = 1
        self._state = "playing"
