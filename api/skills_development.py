from os import path

from modules.db import get_cursor


def main():
    cursor = get_cursor(path.abspath("db/db.sqlite"))

    cursor.execute("SELECT * FROM DIGITAL_SKILLS_DEVELOPMENT TITLE")

    print(
        "\n".join(
            [f"\\item {row['TITLE']}" + (f": \\\\ {row['LATEX_DESCRIPTION']}" if row["LATEX_DESCRIPTION"] else "") for row in cursor.fetchall()]
        )
    )


if __name__ == "__main__":
    main()
