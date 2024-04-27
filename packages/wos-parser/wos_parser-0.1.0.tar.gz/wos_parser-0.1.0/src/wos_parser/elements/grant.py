from dataclasses import dataclass
from typing import List
from xml.etree.ElementTree import Element

from wos_parser.constants import NS


@dataclass
class Grant:
    """An object representing grant informatio"""

    grant_agency: str = None
    """Name of the grant agency"""
    pref: str = None
    """If "Y", `grant_agency` is the unified grant agency name"""
    grant_ids: List[str] = None
    """IDs of all grants by this agency"""

    @classmethod
    def from_xml(cls, grant: Element):
        """Generates an Organization object from an organization XML element"""
        grant_agency = grant.find("grant_agency", NS)
        grant_ids_xml = grant.find("grant_ids", NS)
        if grant_ids_xml is not None:
            grant_ids = [grant_id.text for grant_id in grant_ids_xml]
        else:
            grant_ids = None

        if grant_agency is not None:
            return cls(
                grant_agency=grant_agency.text,
                **grant_agency.attrib,
                grant_ids=grant_ids,
            )
        else:
            return cls(grant_ids=grant_ids)
