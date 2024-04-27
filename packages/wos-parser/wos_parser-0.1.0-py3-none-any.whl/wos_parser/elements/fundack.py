from dataclasses import dataclass
from typing import List
from xml.etree.ElementTree import Element

from wos_parser.constants import NS
from wos_parser.elements import Grant


@dataclass
class FundAck:
    """An object representing funding acknowledgment information"""

    fund_text: str
    """Funding acknowledgment text from the publication"""
    grants: List[Grant]
    """List of Grant objects representing individual grant info"""

    @classmethod
    def from_xml(cls, fund_ack: Element):
        """Generates a FundAck object from a fund_ack XML element"""
        fund_text_xml = fund_ack.find("fund_text", NS)
        if fund_text_xml is not None:
            fund_text = fund_text_xml[0].text
        else:
            fund_text = None
        grants_xml = fund_ack.find("grants", NS)
        if grants_xml is not None:
            grants = [Grant.from_xml(grant) for grant in grants_xml]
        else:
            grants = None

        return cls(fund_text=fund_text, grants=grants)
