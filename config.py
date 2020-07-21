import os

SCRIPT_PATH = f"{os.path.split(os.path.abspath(__file__))[0]}"
COPYRIGHT_OWNER = "Brandon James"
RENDERER_CONFIG = {
    "input_directory": f"{SCRIPT_PATH}/default/",
    "input_file_extensions": (".md", ".markdown"),
    "image_file_extensions": (".jpg", ".jpeg", ".png", ".svg"),
    "output_directory": f"{SCRIPT_PATH}/static/rendered/",
    "image_directory": f"{SCRIPT_PATH}/static/images/post/",
    "pandoc_extra_args": ["--from=markdown-implicit_figures"],
}
NOTES_DIR = "notes"
SITE_NAME = "core"
HEADER_TEXT = "A Simple, Markdown Based, Blogging Platform"
DEFAULT_META_DESCRIPTION = "A Simple, Markdown Based, Blogging Platform"
HEADER_IMAGE = "core.png"
NAV_LINKS = [
    ["/", "Home"],
    ["/about", "About"],
]
STYLESHEET = "core.css"
URI = "coreframework.blog"
PANDOC_PATH = "/usr/bin/pandoc"
PRODUCTION = True
CUSTOM_HEAD_HTML = ""
CUSTOM_FOOTER_HTML = ""