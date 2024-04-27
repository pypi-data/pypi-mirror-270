from dataclasses import dataclass
from xml.etree.ElementTree import Element


@dataclass
class Title:
    """A Title object represents a publication's title"""

    type: str
    """The type of the title (e.g., source or the actual publication)"""
    text: str
    """The text representation of the title"""

    @classmethod
    def from_xml(cls, title: Element):
        """Creates a Title object from an XML title element

        :param title: An XML title element
        :type title: Element
        """
        return cls(type=title.attrib["type"], text=title.text)
