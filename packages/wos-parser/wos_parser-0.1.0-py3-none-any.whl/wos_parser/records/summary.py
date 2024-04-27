from dataclasses import dataclass
from xml.etree.ElementTree import Element
from typing import List

from wos_parser.constants import NS
from wos_parser.elements import Name, PubInfo, Publisher, Title


@dataclass
class Summary:
    """The Summary class represents a summary of a single record."""

    wuid: str
    """Identifies the collection where the record is stored"""
    edition: str
    """Identifies the edition where the record is stored"""
    pub_info: PubInfo
    """Holds basic information about the publication"""
    titles: List[Title]
    """A list of Title objects representing the publication's titles"""
    names: List[Name]
    """A list of Name objects representing the publication's authors"""
    doctypes: List[str]
    """A list of the document types this publication falls into"""
    publishers: List[Publisher]
    """A list of Publisher objects representing the publication's publishers"""

    @classmethod
    def from_xml(cls, summary: Element):
        """Creates a Summary object from an XML summary element

        :param summary: An XML summary element
        :type summary: Element
        """
        if publishers_xml := summary.find("publishers", NS):
            publishers = [Publisher.from_xml(publisher) for publisher in publishers_xml]
        else:
            publishers = None
        return cls(
            wuid=summary.find("EWUID/WUID", NS).attrib["coll_id"],
            edition=summary.find("EWUID/edition", NS).attrib["value"],
            pub_info=PubInfo.from_xml(summary.find("pub_info", NS)),
            titles=[Title.from_xml(title) for title in summary.find("titles", NS)],
            names=[Name.from_xml(name) for name in summary.find("names", NS)],
            doctypes=[doctype.text for doctype in summary.find("doctypes", NS)],
            publishers=publishers,
        )
