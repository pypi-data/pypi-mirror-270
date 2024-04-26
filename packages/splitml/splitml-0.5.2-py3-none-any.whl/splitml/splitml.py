from pathlib import Path
from pprint import pformat
from typing import Union

from tclogger import logger

from .stats import stat_tokens
from .groupers import NodesGrouper
from .html_splitter import HTMLSplitter
from .pdf_splitter import PDFSplitter
from .text_splitter import TextSplitter


def split_html_str(html_str: str, input_format=None):
    return HTMLSplitter().split_html_str(html_str, input_format=input_format)


def split_html_file(html_path: Union[Path, str], input_format=None):
    return HTMLSplitter().split_html_file(html_path, input_format=input_format)


def chunk_html_str(html_str: str, input_format=None):
    nodes = HTMLSplitter().split_html_str(html_str, input_format=input_format)
    grouped_nodes = NodesGrouper().group_nodes(nodes)
    return grouped_nodes


def chunk_html_file(html_path: Union[Path, str], input_format=None):
    nodes = HTMLSplitter().split_html_file(html_path, input_format=input_format)
    grouped_nodes = NodesGrouper().group_nodes(nodes)
    return grouped_nodes


def split_pdf_bytes(pdf_bytes: bytes):
    return PDFSplitter().split_pdf_bytes(pdf_bytes)


def split_pdf_file(pdf_path: Union[Path, str]):
    return PDFSplitter().split_pdf_file(pdf_path)


def chunk_pdf_bytes(pdf_bytes: bytes):
    nodes = PDFSplitter().split_pdf_bytes(pdf_bytes)
    grouped_nodes = NodesGrouper().group_nodes(nodes)
    return grouped_nodes


def chunk_pdf_file(pdf_path: Union[Path, str]):
    nodes = PDFSplitter().split_pdf_file(pdf_path)
    grouped_nodes = NodesGrouper().group_nodes(nodes)
    return grouped_nodes


def split_text_str(text_str: str):
    return TextSplitter().split_text_str(text_str)


def split_text_file(text_path: Union[Path, str]):
    return TextSplitter().split_text_file(text_path)


def chunk_text_str(text_str: str):
    nodes = TextSplitter().split_text_str(text_str)
    grouped_nodes = NodesGrouper("text").group_nodes(nodes)
    return grouped_nodes


def chunk_text_file(text_path: Union[Path, str]):
    nodes = TextSplitter().split_text_file(text_path)
    grouped_nodes = NodesGrouper("text").group_nodes(nodes)
    return grouped_nodes


if __name__ == "__main__":
    sample_root = Path(__file__).parent / "samples"

    # file_pattern = "*.html.md"
    # html_paths = sorted(
    #     list(sample_root.glob(file_pattern)),
    #     key=lambda x: str(x).lower(),
    # )[:2]
    # splitter = HTMLSplitter()
    # grouper = NodesGrouper()
    # for html_path in html_paths:
    #     logger.note(f"> Processing: {html_path.name}")
    #     nodes = splitter.split_html_file(html_path)
    #     logger.success(f"  - {len(nodes)} nodes.")
    #     stat_tokens(nodes)
    #     grouped_nodes = grouper.group_nodes(nodes)
    #     logger.success(f"  - {len(grouped_nodes)} grouped nodes.")
    #     stat_tokens(grouped_nodes)

    # file_pattern = "*.pdf"
    # pdf_paths = sorted(
    #     list(sample_root.glob(file_pattern)),
    #     key=lambda x: str(x).lower(),
    # )[:1]
    # splitter = PDFSplitter()
    # for pdf_path in pdf_paths:
    #     logger.note(f"> Processing: {pdf_path.name}")
    #     nodes = splitter.split_pdf_file(pdf_path)
    #     logger.success(f"  - {len(nodes)} nodes.")
    #     stat_tokens(nodes)
    #     grouped_nodes = NodesGrouper().group_nodes(nodes)
    #     logger.success(f"  - {len(grouped_nodes)} grouped nodes.")
    #     stat_tokens(grouped_nodes)

    file_pattern = "*.html.md"
    file_paths = sorted(
        list(sample_root.glob(file_pattern)),
        key=lambda x: str(x).lower(),
    )[:1]
    splitter = TextSplitter()
    grouper = NodesGrouper("text")
    for file_path in file_paths:
        logger.note(f"> Processing: {file_path.name}")
        nodes = splitter.split_text_file(file_path)
        logger.success(f"  - {len(nodes)} nodes.")
        stat_tokens(nodes)
        grouped_nodes = grouper.group_nodes(nodes)
        logger.success(f"  - {len(grouped_nodes)} grouped nodes.")
        stat_tokens(grouped_nodes)

    logger.success(pformat(grouped_nodes[0], indent=4, sort_dicts=False))

    # [**/src]
    # python -m splitml.splitml
