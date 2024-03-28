from os import path

from modules.date import Date, format_range
from modules.db import get_cursor
from modules.entity import Entity
from modules.latex_blocks import timeline, timeline_content
from modules.location import Location


def main():
    cursor = get_cursor(path.abspath("db/db.sqlite"))

    cursor.execute("SELECT * FROM EDUCATION ORDER BY END DESC, START DESC, TITLE")

    print(
        "\n".join(
            [timeline(
                date = format_range(Date(row["START"]), Date(row["END"])),
                content = timeline_content(
                    row["TITLE"],
                    suptitle = row["TYPE"],
                    location = Location(cursor, row["LOCATION"]),
                    entity = Entity(cursor, row["FROM_ENTITY"]),
                    entity_prefix = "From",
                    result = row["RESULT"],
                    content = row["LATEX_DESCRIPTION"]
                )
            ) for row in cursor.fetchall()]
        )
    )


if __name__ == "__main__":
    main()
