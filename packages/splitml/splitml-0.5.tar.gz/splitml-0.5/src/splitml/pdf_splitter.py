import fitz

from pathlib import Path

from tclogger import logger
from purehtml import purify_html_str

from .html_splitter import HTMLSplitter


class PDFSplitter:

    def split_pdf_doc(self, pdf_doc):
        results = []
        html_splitter = HTMLSplitter()
        for page_idx, page in enumerate(pdf_doc):
            logger.note(f"> Page {page_idx+1}")
            html_str = page.get_text("html")
            html_str = purify_html_str(html_str)
            # logger.mesg(html_str)
            nodes = html_splitter.split_html_str(html_str, format=format)
            results.extend(nodes)

        return results

    def read_pdf_bytes(self, pdf_bytes):
        # https://github.com/pymupdf/PyMuPDF/issues/612
        doc = fitz.open("pdf", pdf_bytes)
        return doc

    def read_pdf_file(self, pdf_path):
        if not Path(pdf_path).exists():
            warn_msg = f"File not found: {pdf_path}"
            logger.warn(warn_msg)
            raise FileNotFoundError(warn_msg)
        doc = fitz.open(pdf_path)
        return doc

    def split_pdf_bytes(self, pdf_bytes):
        pdf_doc = self.read_pdf_bytes(pdf_bytes)
        return self.split_pdf_doc(pdf_doc)

    def split_pdf_file(self, pdf_path):
        pdf_doc = self.read_pdf_file(pdf_path)
        return self.split_pdf_doc(pdf_doc)
