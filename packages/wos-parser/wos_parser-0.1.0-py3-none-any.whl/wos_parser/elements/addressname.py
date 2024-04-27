from dataclasses import dataclass
from typing import List
from xml.etree.ElementTree import Element

from wos_parser.constants import NS
from wos_parser.elements import AddressSpec, Name


@dataclass
class AddressName:
    """An object representing an address associated with an author name"""

    address_spec: AddressSpec
    """An address specification"""
    names: List[Name]
    """The names associated with the address"""

    @classmethod
    def from_xml(cls, address_name: Element):
        """Creates an AddressName object from an address_name XML element"""
        address_names = address_name.find("names", NS)
        if address_names is not None:
            names = [Name.from_xml(name) for name in address_names]
        else:
            names = None
        return cls(
            address_spec=AddressSpec.from_xml(address_name.find("address_spec", NS)),
            names=names,
        )
