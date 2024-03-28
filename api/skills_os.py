from os import path

from modules.db import get_cursor


def main():
    cursor = get_cursor(path.abspath("db/db.sqlite"))

    cursor.execute("SELECT * FROM DIGITAL_SKILLS_OS TYPE")

    print(
        "\n".join(
            [f"\\item {row['TYPE']}" + (f": {row['VERSIONS']}" if row["VERSIONS"] else "") + f"\\\\ \\progress{{{row['PERCENT']}}}" for row in cursor.fetchall()]
        )
    )


if __name__ == "__main__":
    main()
