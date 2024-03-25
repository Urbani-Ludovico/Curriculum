def timeline(date = None, content = None):
    date = "" if date is None else date
    content = "" if content is None else content
    return f"\\tldate{{{date}}} & \\tlcontent{{{content}}} \\\\"
