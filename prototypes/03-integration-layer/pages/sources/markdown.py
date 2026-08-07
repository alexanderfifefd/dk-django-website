import markdown

MARKDOWN_EXTENSIONS = ["fenced_code", "tables", "smarty"]


def render_markdown(text: str) -> str:
    return markdown.markdown(text, extensions=MARKDOWN_EXTENSIONS)
