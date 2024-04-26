import markdown2
import re

from pathlib import Path

from bs4 import BeautifulSoup
from purehtml import purify_html_str
from tclogger import logger
from typing import Literal

from .constants import SPLIT_TAGS, TAG_TYPE_MAP
from .stats import count_tokens


class HTMLSplitter:
    def get_tag_type(self, element):
        tag_type = ""
        for key, tags in TAG_TYPE_MAP.items():
            if element.name in tags:
                tag_type = key
                break
        return tag_type

    def remove_separators(self, text: str) -> str:
        new_text = text
        chars_map = {
            "\n+": " ",
            "-\n": "",
            "\f": "",
        }
        for k, v in chars_map.items():
            new_text = re.sub(k, v, new_text)
        return new_text

    def read_html_file(self, html_path):
        if not Path(html_path).exists():
            warn_msg = f"File not found: {html_path}"
            logger.warn(warn_msg)
            raise FileNotFoundError(warn_msg)

        encodings = ["utf-8", "latin-1"]
        for encoding in encodings:
            try:
                with open(html_path, "r", encoding=encoding, errors="ignore") as rf:
                    html_str = rf.read()
                    return html_str
            except UnicodeDecodeError:
                pass
        else:
            warn_msg = f"No matching encodings: {html_path}"
            logger.warn(warn_msg)
            raise UnicodeDecodeError(warn_msg)

    def is_atomized(self, element):
        # check if any children of element has tag in SPLIT_TAGS
        for child in element.descendants:
            if child.name in SPLIT_TAGS:
                return False
        return True

    def md2html(self, md_str):
        return markdown2.markdown(md_str)

    def check_input_format(func):
        def wrapper(
            self, html_str, input_format: Literal["html", "markdown"] = "html", **kwargs
        ):
            if input_format == "markdown":
                html_str = self.md2html(html_str)
            return func(self, html_str, input_format, **kwargs)

        return wrapper

    @check_input_format
    def split_html_str(
        self,
        html_str,
        input_format: Literal["html", "markdown"] = "html",
        page_idx=-1,
        remove_seps=False,
    ):
        results = []
        soup = BeautifulSoup(html_str, "html.parser")
        for idx, element in enumerate(soup.find_all(SPLIT_TAGS)):
            if not self.is_atomized(element):
                continue
            element_str = str(element)
            markdown_str = purify_html_str(
                element_str,
                output_format="markdown",
                keep_format_tags=False,
                keep_group_tags=False,
                math_style="latex",
            )

            if remove_seps:
                markdown_str = self.remove_separators(markdown_str)

            item = {
                "html": element_str,
                "text": markdown_str,
                "tag": element.name,
                "tag_type": self.get_tag_type(element),
                "html_len": len(element_str),
                "text_len": len(markdown_str),
                "text_tokens": count_tokens(markdown_str),
                "node_idx": idx,
                "page_idx": page_idx,
            }
            results.append(item)

        return results

    def split_html_file(
        self, html_path, input_format: Literal["html", "markdown"] = "html"
    ):
        ext = Path(html_path).suffix
        if not input_format:
            if ext == ".md":
                input_format = "markdown"
            else:
                input_format = "html"
        else:
            input_format = input_format

        html_str = self.read_html_file(html_path)
        return self.split_html_str(html_str, input_format=input_format)
