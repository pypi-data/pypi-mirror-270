from dataclasses import dataclass
from xml.etree.ElementTree import Element


@dataclass
class Page:
    """A Page object represents the page range of a publication"""

    begin: str = None
    """First page"""
    end: str = None
    """Last page"""
    page_count: str = None
    """Number of pages"""

    @classmethod
    def from_xml(cls, page: Element):
        """Creates a Page object from a page XML element

        :param page: A page XML element
        :type page: Element
        """
        return cls(**page.attrib)
