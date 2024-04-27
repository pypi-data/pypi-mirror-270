from dataclasses import dataclass
from xml.etree.ElementTree import Element

from wos_parser.constants import NS
from wos_parser.elements import Page


@dataclass
class PubInfo:
    """Holds basic information about a publication"""

    issue: str = None
    """Issue of the source the publication appeared in"""
    pubtype: str = None
    """Type of the source the publication appeared in (e.g. Journal or Book)"""
    sortdate: str = None
    """Sorting date"""
    early_access_date: str = None
    """The early access date of the publication"""
    has_abstract: str = None
    """Whether an abstract is included in the record"""
    coverdate: str = None
    """Cover date of the source publication"""
    pubmonth: str = None
    """Month of publication"""
    early_access_month: str = None
    """The early access month of the publication"""
    vol: str = None
    """Volume of the source the publication appeared in"""
    part_no: str = None
    """Part of the source the publication appeared in"""
    pubyear: str = None
    """Year of publication"""
    early_access_year: str = None
    """The early access year of the publication"""
    page: Page = None
    """Page range object"""
    supplement: str = None
    """If the source the publication appeared in was a supplement"""
    special_issue: str = None
    """If the source the publication appeared in was a special issue"""

    @classmethod
    def from_xml(cls, pub_info: Element):
        """Creates a PubInfo object from a pub_info XML element

        :param pub_info: A pub_info XML element
        :type pub_info: Element
        """
        return cls(**pub_info.attrib, page=Page.from_xml(pub_info.find("page", NS)))
