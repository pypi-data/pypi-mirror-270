from dataclasses import dataclass

from xml.etree.ElementTree import Element


@dataclass
class PhysicalSection:
    """Represents the section in which a citation of a reference occurred"""

    physicalLocation: str
    """Percentage how far into the paper the citation occurred"""
    label: str
    """Label of the section where the citation occurred"""
    section: str = None
    """Parent section where the citation occurred"""
    function: str = None
    """Function of the section"""

    @classmethod
    def from_xml(cls, physicalSection: Element):
        """Generates a PhysicalSection object from a physicalSection XML element"""
        return cls(**physicalSection.attrib, label=physicalSection.text)
