from pathlib import Path
from pprint import pformat
from typing import Union

from tclogger import logger

from .stats import stat_tokens
from .groupers import NodesGrouper
from .html_splitter import HTMLSplitter
from .pdf_splitter import PDFSplitter


def split_html_str(html_str: str, format=None):
    return HTMLSplitter().split_html_str(html_str, format=format)


def split_html_file(html_path: Union[Path, str], format=None):
    return HTMLSplitter().split_html_file(html_path, format=format)


def chunk_html_str(html_str: str, format=None):
    nodes = HTMLSplitter().split_html_str(html_str, format=format)
    grouped_nodes = NodesGrouper().group_nodes(nodes)
    return grouped_nodes


def chunk_html_file(html_path: Union[Path, str], format=None):
    nodes = HTMLSplitter().split_html_file(html_path, format=format)
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

    file_pattern = "*.pdf"
    pdf_paths = sorted(
        list(sample_root.glob(file_pattern)),
        key=lambda x: str(x).lower(),
    )[:1]
    splitter = PDFSplitter()
    for pdf_path in pdf_paths:
        logger.note(f"> Processing: {pdf_path.name}")
        nodes = splitter.split_pdf_file(pdf_path)
        logger.success(f"  - {len(nodes)} nodes.")
        stat_tokens(nodes)
        grouped_nodes = NodesGrouper().group_nodes(nodes)
        logger.success(f"  - {len(grouped_nodes)} grouped nodes.")
        stat_tokens(grouped_nodes)
    logger.success(pformat(grouped_nodes[0], indent=4, sort_dicts=False))

    # [**/src]
    # python -m splitml.splitml
