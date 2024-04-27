from dataclasses import dataclass
from xml.etree.ElementTree import Element
from typing import List

from wos_parser.constants import NS
from wos_parser.elements import Organization


@dataclass
class AddressSpec:
    """An AddressSpec object represents an address specification"""

    addr_no: str
    """Number of the address in the listing"""
    full_address: str
    """The full address"""
    street: str = None
    """The street"""
    city: str = None
    """The city"""
    state: str = None
    """The state"""
    country: str = None
    """The country"""
    zip: str = None
    """The zip code"""
    organizations: List[Organization] = None
    """List of organizations associated with this address"""
    suborganizations: List[Organization] = None
    """List of suborganizations associated with this address"""

    @classmethod
    def from_xml(cls, address_spec: Element):
        """Creates an AddressSpec object from an address_spec XML element"""
        if organizations_xml := address_spec.find("organizations", NS):
            organizations = [Organization.from_xml(org) for org in organizations_xml]
        else:
            organizations = None

        if suborganizations_xml := address_spec.find("suborganizations", NS):
            suborganizations = [
                Organization.from_xml(org) for org in suborganizations_xml
            ]
        else:
            suborganizations = None
        return cls(
            **address_spec.attrib,
            **{
                name: child.text
                for child in address_spec
                if (name := child.tag.replace("{" + NS[""] + "}", ""))
                not in ["organizations", "suborganizations"]
            },
            organizations=organizations,
            suborganizations=suborganizations,
        )
