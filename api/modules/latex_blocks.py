from . import globals


def timeline(date = None, content = None):
    date = "" if date is None else date
    content = "" if content is None else content
    return f"\\tldate{{{date}}} & \\tlcontent{{{content}}} \\\\"


def timeline_content(title, suptitle = None, subtitle = None, location = None, entity = None, entity_prefix = "By", result = None, content = None):
    out = []
    if suptitle is not None:
        out.append(f"\\ltsubtitle{{{suptitle}}}")

    out.append(f"\\lttitle{{{title}}}")

    if subtitle is not None:
        out.append(f"\\ltsubtitle{{{subtitle}}}")

    if entity:
        if location and entity.data["LOCATION"] == location.data["ID"]:
            out.append(f"{entity_prefix}: \\ltloc{{{entity.name()}}}")
        else:
            out.append(f"{entity_prefix}: \\ltloc{{{entity.complete()}}}")
    if location:
        out.append(f"Location: \\ltloc{{{location.complete()}}}")

    if result is not None:
        out.append(f"Result: {result}")

    if content is not None:
        out.append(content)

    return f" \\\\[{globals.EVENT_LINE_SEP}] ".join(out)
