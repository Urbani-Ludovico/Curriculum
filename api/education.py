from os import path

from modules.date import Date, format_range
from modules.db import get_cursor
from modules.entity import Entity
from modules.latex_blocks import timeline
from modules.location import Location


def main():
    cursor = get_cursor(path.abspath("db/db.sqlite"))

    cursor.execute("SELECT * FROM EDUCATION ORDER BY END DESC, START DESC, TITLE")
    rows = cursor.fetchall()

    out = []
    for row in rows:
        content = []
        if row["TYPE"]:
            content.append(row["TYPE"])
        if row["TITLE"]:
            content.append(row["TITLE"])

        entity = None
        location = None
        if row["LOCATION"]:
            location = Location(cursor, row["LOCATION"])
        if row["FROM_ENTITY"]:
            entity = Entity(cursor, row["FROM_ENTITY"])
            if location is not None:
                content.append(f"From: {entity.name()}")
            else:
                content.append(f"From: {entity.complete()}")
        if location:
            if entity is None:
                content.append(f"From: {location.complete()}")
            else:
                content.append(location.location())

        if row["RESULT"]:
            content.append(f"Result: {row['RESULT']}")
        out.append(timeline(date = format_range(Date(row["START"]), Date(row["END"])), content = " \\\\ ".join(content)))

    print("\n".join(out))


if __name__ == "__main__":
    main()
