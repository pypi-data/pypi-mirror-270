from dataclasses import dataclass
from xml.etree.ElementTree import Element
from typing import List

from wos_parser.constants import NS
from wos_parser.elements import AddressSpec, Name


@dataclass
class Publisher:
    address_spec: AddressSpec
    """AddressSpec object representing the address information of the publisher"""
    names: List[Name]
    """List of Name objects representing the names of the publisher"""

    @classmethod
    def from_xml(cls, publisher: Element):
        """Creates a Publisher element from a publisher XML element

        :param publisher: An XML publisher element
        :type publisher: Element
        """
        return cls(
            address_spec=AddressSpec.from_xml(publisher.find("address_spec", NS)),
            names=[Name.from_xml(name) for name in publisher.find("names", NS)],
        )
