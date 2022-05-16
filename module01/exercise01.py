class Time:
    # constructor
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour  # _hour: attribute
        self._minute = minute  # _minute: attribute
        self._second = second  # _second: attribute

    @property  # read
    def hour(self):
        return self._hour

    @hour.setter  # write
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError(f"Hour ({hour}) must be between 0-23")
        self._hour = hour

    @property  # read
    def minute(self):
        return self._minute

    @minute.setter  # write
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError(f"Minute ({minute}) must be between 0-60")
        self._minute = minute

    @property  # read
    def second(self):
        return self._second

    @second.setter  # write
    def second(self, second):
        if not (0 <= second < 60):
            raise ValueError(f"Second ({second}) must be between 0-60")
        self._second = second

