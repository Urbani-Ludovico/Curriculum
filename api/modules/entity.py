from .location import Location


class Entity:
    data = None
    location = None

    def __init__(self, cursor, id):
        cursor.execute("SELECT * FROM ENTITIES WHERE ID = ? LIMIT 1", (id,))
        self.data = cursor.fetchone()

        if self.data and self.data["LOCATION"]:
            self.location = Location(cursor, self.data["LOCATION"])

    def complete(self):
        if self.data is None:
            return None

        out = []
        if self.data["NAME"]:
            out.append(self.data["NAME"])
        if self.location:
            loc = self.location.location()
            if loc:
                out.append(loc)

        return ", ".join(out)

    def name(self):
        return self.data["NAME"]

    def __bool__(self):
        return self.data is not None
