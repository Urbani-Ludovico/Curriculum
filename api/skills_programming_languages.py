from os import path

from modules.db import get_cursor


def main():
    cursor = get_cursor(path.abspath("db/db.sqlite"))

    cursor.execute("SELECT * FROM DIGITAL_SKILLS_PROGRAMMING_LANGUAGES TYPE")

    print(
        "\n".join(
            [f"\\item {row['NAME']} \\\\ \\progress{{{row['PERCENT']}}}" for row in cursor.fetchall()]
        )
    )


if __name__ == "__main__":
    main()
