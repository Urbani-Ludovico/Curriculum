class Location:
    data = None

    def __init__(self, cursor, id):
        cursor.execute("SELECT * FROM LOCATIONS WHERE ID = ? LIMIT 1", id)
        self.data = cursor.fetchone()

    def complete(self):
        if self.data is None:
            return "--"

        out = []
        if self.data["NAME"]:
            out.append(self.data["NAME"])
        if self.data["ADDRESS"]:
            out.append(self.data["ADDRESS"])
        if self.data["CITY"] and (self.data["STATE"] or self.data["STATE_CODE"]):
            out.append(self.data["CITY"] + " (" + (self.data["STATE_CODE"] if self.data["STATE"] is None else self.data["STATE"]) + ")")
        elif self.data["CITY"]:
            out.append(self.data["CITY"])
        elif self.data["STATE"] or self.data["STATE_CODE"]:
            out.append(self.data["STATE_CODE"] if self.data["STATE"] is None else self.data["STATE"])

        if len(out):
            return ", ".join(out)

        return None

    def location(self):
        if self.data is None:
            return "--"

        out = []
        if self.data["ADDRESS"]:
            out.append(self.data["ADDRESS"])
        if self.data["CITY"] and (self.data["STATE"] or self.data["STATE_CODE"]):
            out.append(self.data["CITY"] + " (" + (self.data["STATE_CODE"] if self.data["STATE"] is None else self.data["STATE"]) + ")")
        elif self.data["CITY"]:
            out.append(self.data["CITY"])
        elif self.data["STATE"] or self.data["STATE_CODE"]:
            out.append(self.data["STATE_CODE"] if self.data["STATE"] is None else self.data["STATE"])

        if len(out):
            return ", ".join(out)

        return None
