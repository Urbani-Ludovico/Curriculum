from os import path

from modules.date import Date
from modules.db import get_cursor
from modules.entity import Entity
from modules.latex_blocks import timeline, timeline_content
from modules.location import Location


def main():
    cursor = get_cursor(path.abspath("db/db.sqlite"))

    cursor.execute("SELECT * FROM QUALIFICATIONS ORDER BY DATE DESC, TITLE")

    print(
        "\n".join(
            [timeline(
                date = Date(row["DATE"]).strftime(),
                content = timeline_content(
                    row["TITLE"],
                    location = Location(cursor, row["WHERE"]),
                    entity = Entity(cursor, row["BY"]),
                    content = row["LATEX_DESCRIPTION"]
                )
            ) for row in cursor.fetchall()]
        )
    )


if __name__ == "__main__":
    main()
