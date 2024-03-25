from datetime import date


class Date(object):
    ongoing = False
    year = None
    month = None
    day = None

    def __init__(self, dt):
        self.load(dt)

    def load(self, dt):
        self.ongoing = False
        self.year = None
        self.month = None
        self.day = None

        if dt.upper() == "ONGOING":
            self.ongoing = True
        elif isinstance(dt, str):
            s = dt.split("-")

            try:
                y = int(s[0])
                if y < 1900:
                    return
                self.year = y
            except IndexError:
                return
            except ValueError:
                return

            try:
                m = int(s[1])
                try:
                    date(self.year, m, 1)
                    self.month = m
                except ValueError:
                    return
            except IndexError:
                return
            except ValueError:
                return

            try:
                d = int(s[2])
                try:
                    date(self.year, self.month, d)
                    self.day = d
                except ValueError:
                    return
            except IndexError:
                return
            except ValueError:
                return

    def strftime_extended(self):
        if self.ongoing:
            return "ongoing"

        if self.year is not None:
            s = str(self.year)
            if self.month is not None:
                s = month_string_extended(self.month) + " " + s
                if self.day is not None:
                    s = str(self.day) + " " + s
                    return s.strip()
        return ""

    def strftime(self):
        if self.ongoing:
            return "ongoing"

        if self.year is not None:
            s = str(self.year)
            if self.month is not None:
                s = month_string(self.month) + " " + s
                return s.strip()

        return ""

    def __repr__(self):
        return f"{self.year}-{self.month}-{self.day}" if not self.ongoing else "ongoing"

    def __bool__(self):
        return self.ongoing or self.year is not None


def format_range(a, b, func = lambda x: x.strftime()):
    if a and b:
        a = func(a)
        b = func(b)
        if a == b:
            return "In " + a
        else:
            return a + " \\\\ " + b

    if a:
        return func(a)

    if b:
        return func(b)

    return ""


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def month_string_extended(i):
    if i in range(1, 13):
        return months[i - 1]


def month_string(i):
    if i in range(1, 13):
        return months[i - 1][:3]
