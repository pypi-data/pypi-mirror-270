from dataclasses import dataclass
from typing import List
from xml.etree.ElementTree import Element

from wos_parser.constants import NS
from wos_parser.elements import Subject


@dataclass
class CategoryInfo:
    """An object that represents the category information of a record"""

    headings: List[str]
    """A list of category headings"""
    subheadings: List[str]
    """A list of category subheadings"""
    subjects: List[Subject]
    """A list of the record's subjects"""

    @classmethod
    def from_xml(cls, category_info: Element):
        """Generates a CategoryInfo object from a category_info XML element"""

        if headings_xml := category_info.find("headings", NS):
            headings = [child.text for child in headings_xml]
        else:
            headings = None

        if subheadings_xml := category_info.find("subheadings", NS):
            subheadings = [child.text for child in subheadings_xml]
        else:
            subheadings = None

        subjects = [
            Subject.from_xml(subject) for subject in category_info.find("subjects", NS)
        ]
        return cls(headings=headings, subheadings=subheadings, subjects=subjects)
