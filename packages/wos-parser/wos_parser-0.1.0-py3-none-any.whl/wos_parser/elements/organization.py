from dataclasses import dataclass
from xml.etree.ElementTree import Element


@dataclass
class Organization:
    """An object representing an organization"""

    name: str
    """Name of the organization as listed in a publication"""
    pref: str = None
    """If "Y", `name` is the unified organization name"""

    @classmethod
    def from_xml(cls, organization: Element):
        """Generates an Organization object from an organization XML element"""
        return cls(
            name=organization.text,
            **organization.attrib,
        )
