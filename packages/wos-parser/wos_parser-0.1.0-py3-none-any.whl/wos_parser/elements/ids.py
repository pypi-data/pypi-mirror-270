from dataclasses import dataclass
from xml.etree.ElementTree import Element


@dataclass
class Ids:
    """TODO: What info is captured by this?"""

    avail: str
    """TODO"""
    label: str
    """TODO"""

    @classmethod
    def from_xml(cls, ids: Element):
        """Generates and Ids object from an ids XML element"""
        return cls(**ids.attrib, label=ids.text)
