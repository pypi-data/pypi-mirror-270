from dataclasses import dataclass
from typing import List
from xml.etree.ElementTree import Element

from wos_parser.constants import NS
from wos_parser.elements import BibPageCount, Ids


@dataclass
class Item:
    ids: Ids
    """TODO"""
    bib_id: str
    """TODO"""
    bib_pagecount: BibPageCount
    """TODO"""
    keywords_plus: List[str]
    """TODO"""

    @classmethod
    def from_xml(cls, item: Element):
        """Generates an Item object from an item XML element"""
        return cls(
            ids=Ids.from_xml(item.find("ids", NS)),
            bib_id=item.find("bib_id", NS).text,
            bib_pagecount=(
                BibPageCount.from_xml(bib_pagecount)
                if (bib_pagecount := item.find("bib_pagecount", NS))
                else None
            ),
            keywords_plus=(
                [keyword.text for keyword in keywords]
                if (keywords := item.find("keywords_plus", NS))
                else None
            ),
        )
