from dataclasses import dataclass
from xml.etree.ElementTree import Element


@dataclass
class BibPageCount:
    """TODO"""

    type: str
    """TODO"""
    number: str
    """TODO"""

    @classmethod
    def from_xml(cls, bib_pagecount: Element):
        """Generates a BibPageCount object from an bib_pagecount XML element"""
        return cls(**bib_pagecount.attrib, number=bib_pagecount.text)
