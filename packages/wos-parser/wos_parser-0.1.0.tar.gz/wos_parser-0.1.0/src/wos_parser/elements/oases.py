from dataclasses import dataclass
from typing import List
from xml.etree.ElementTree import Element

from wos_parser.constants import NS


@dataclass
class Oas:
    """TODO"""

    type: str
    """TODO"""

    @classmethod
    def from_xml(cls, oas: Element):
        """Generates an Oas object from an oas XML element"""
        return cls(**oas.attrib)


@dataclass
class Oases:
    """TODO"""

    count: str
    """TODO"""
    is_OA: str
    """TODO"""
    oases: List[Oas]
    """TODO"""

    @classmethod
    def from_xml(cls, oases: Element):
        """Generates an Oases object from an oases XML element"""
        return cls(**oases.attrib, oases=[Oas.from_xml(oas) for oas in oases])
