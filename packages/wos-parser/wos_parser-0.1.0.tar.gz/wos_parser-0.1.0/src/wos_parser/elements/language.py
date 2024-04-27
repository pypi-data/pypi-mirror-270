from dataclasses import dataclass
from xml.etree.ElementTree import Element


@dataclass
class Language:
    """A Language object represents a language a record was published in"""

    type: str
    """The type of the language (e.g., primary)"""
    name: str
    """The name of the language (e.g., English)"""

    @classmethod
    def from_xml(cls, language: Element):
        """Generates a Language object from a language XML element"""
        return cls(name=language.text, **language.attrib)
