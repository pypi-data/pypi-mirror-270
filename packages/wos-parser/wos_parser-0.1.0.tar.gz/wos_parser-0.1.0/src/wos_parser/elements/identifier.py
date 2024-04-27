from dataclasses import dataclass
from xml.etree.ElementTree import Element


@dataclass
class Identifier:
    """An object representing an identifier of a publication"""

    type: str
    """The type of the identifier, e.g., 'doi' or 'pmid'"""
    value: str
    """The value of the identifier, i.e., the actual identifier"""

    @classmethod
    def from_xml(cls, identifier: Element):
        """Generates an Identifier object from an identifier XML element"""
        return cls(**identifier.attrib)
