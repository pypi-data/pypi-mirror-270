import re

from pathlib import Path

from tclogger import logger
from typing import Literal

from .stats import count_tokens


class TextSplitter:
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

    def read_text_file(self, file_path):
        if not Path(file_path).exists():
            warn_msg = f"File not found: {file_path}"
            logger.warn(warn_msg)
            raise FileNotFoundError(warn_msg)

        encodings = ["utf-8", "latin-1"]
        for encoding in encodings:
            try:
                with open(file_path, "r", encoding=encoding, errors="ignore") as rf:
                    html_str = rf.read()
                    return html_str
            except UnicodeDecodeError:
                pass
        else:
            warn_msg = f"No matching encodings: {file_path}"
            logger.warn(warn_msg)
            raise UnicodeDecodeError(warn_msg)

    def split_text_str(self, text_str, page_idx=-1, remove_seps=False):
        results = []
        elements = text_str.splitlines()
        for idx, element in enumerate(elements):
            element_str = str(element)

            if remove_seps:
                element_str = self.remove_separators(element_str)

            item = {
                "html": "",
                "text": element_str,
                "tag": "",
                "tag_type": "",
                "html_len": 0,
                "text_len": len(element_str),
                "text_tokens": count_tokens(element_str),
                "node_idx": idx,
                "page_idx": page_idx,
            }
            results.append(item)

        return results

    def split_text_file(self, file_path):
        text_str = self.read_text_file(file_path)
        return self.split_text_str(text_str)
