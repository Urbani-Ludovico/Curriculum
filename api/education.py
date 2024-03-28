from os import path

from modules.date import Date, format_range
from modules.db import get_cursor
from modules.entity import Entity
from modules.latex_blocks import timeline
from modules.location import Location
from modules import globals


def main():
    cursor = get_cursor(path.abspath("db/db.sqlite"))

    cursor.execute("SELECT * FROM EDUCATION ORDER BY END DESC, START DESC, TITLE")
    rows = cursor.fetchall()

    out = []
    for row in rows:
        content = []
        if row["TYPE"]:
            content.append(f"\\ltsubtitle{{{row['TYPE']}}}")
        if row["TITLE"]:
            content.append(f"\\lttitle{{{row['TITLE']}}}")

        entity = None
        location = None
        if row["LOCATION"]:
            location = Location(cursor, row["LOCATION"])
        if row["FROM_ENTITY"]:
            entity = Entity(cursor, row["FROM_ENTITY"])
            if location is not None:
                content.append(f"From: \\ltloc{{{entity.name()}}}")
            else:
                content.append(f"From: \\ltloc{{{entity.complete()}}}")
        if location:
            if entity is None:
                content.append(f"\\ltloc{{{location.complete()}}}")
            else:
                content.append(f"\\ltloc{{{location.location()}}}")

        if row["RESULT"]:
            content.append(f"Result: {row['RESULT']}")
        out.append(timeline(date = format_range(Date(row["START"]), Date(row["END"])), content = f" \\\\[{globals.EVENT_LINE_SEP}] ".join(content)))

    print("\n".join(out))


if __name__ == "__main__":
    main()
