from dataclasses import dataclass
from typing import List
from xml.etree.ElementTree import Element

from wos_parser.constants import NS
from wos_parser.elements import Identifier, Name, Oases, Subject
from wos_parser.records import FullRecordMetadata, Item, Summary


@dataclass
class Record:
    """A Record object represenst a single Web of Science record, i.e., one publication."""

    # static_data
    uid: str
    """Unique ID of the record"""
    summary: Summary
    """A Summary object with basic information on the publication"""
    fullrecord_metadata: FullRecordMetadata
    """The full record including all available metadata"""
    item: Item
    """TODO: What is captured by the item element?"""
    contributors: List[Name]
    """List of contributors (authors for whom a Publons Profile/ResearcherID or an ORCID identifier is provided)"""

    # dynamic_data
    # TODO: What is cluster_related?
    identifiers: List[Identifier]
    """List of identifiers for the record, e.g. ISSN or DOI"""
    # TODO: What is ic_related?
    oases: Oases
    """TODO"""
    # TODO: What is citation_related?
    citation_topics: List[Subject]
    """TODO"""

    @classmethod
    def from_xml(cls, record: Element):
        """Creates a Record object from an XML record element

        :param record: An XML element representing a record
        :type record: Element
        """
        contributors_xml = record.find("static_data/contributors", NS)
        if contributors_xml is not None:
            contributors = [
                Name.from_xml(name)
                for contributor in contributors_xml
                for name in contributor
            ]
        else:
            contributors = None
        return cls(
            uid=record.find("UID", NS).text,
            summary=Summary.from_xml(record.find("static_data/summary", NS)),
            fullrecord_metadata=FullRecordMetadata.from_xml(
                record.find("static_data/fullrecord_metadata", NS)
            ),
            item=Item.from_xml(record.find("static_data/item", NS)),
            contributors=contributors,
            identifiers=[
                Identifier.from_xml(identifier)
                for identifier in record.find(
                    "dynamic_data/cluster_related/identifiers", NS
                )
            ],
            oases=(
                Oases.from_xml(oases)
                if (oases := record.find("dynamic_data/ic_related/oases", NS))
                is not None
                else None
            ),
            citation_topics=(
                [Subject.from_xml(subject) for subject in subjects]
                if (
                    subjects := record.find(
                        "dynamic_data/citation_related/citation_topics/subj-group",
                        NS,
                    )
                )
                is not None
                else None
            ),
        )
