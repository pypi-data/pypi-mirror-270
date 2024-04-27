from dataclasses import dataclass
from xml.etree.ElementTree import Element
from typing import List

from wos_parser.constants import NS
from wos_parser.elements import AddressName, CategoryInfo, FundAck, Language, Reference


@dataclass
class FullRecordMetadata:
    """An object representing the full record metadata"""

    languages: List[Language]
    """Languages of the record"""
    normalized_languages: List[Language]
    """Normalized languages of the record"""
    normalized_doctypes: List[str]
    """Normalized document types of the record"""
    references: List[Reference]
    """Cited references"""
    addresses: List[AddressName]
    """Addresses associated with the authors"""
    reprint_addresses: List[AddressName]
    """Reprint addresses associated with the authors"""
    category_info: CategoryInfo
    """Categories of the record"""
    fund_ack: FundAck
    """Funding acknowledgment information"""
    keywords: List[str]
    """List of keywords of the publication"""
    abstracts: List[str]
    """List of abstracts of the publication"""

    @classmethod
    def from_xml(cls, fullrecord_metadata: Element):
        """Generates a FullRecordMetadata object from a fullrecord_metadata XML element"""

        if reprint_addresses_xml := fullrecord_metadata.find("reprint_addresses", NS):
            reprint_addresses = (
                [
                    AddressName.from_xml(address_name)
                    for address_name in reprint_addresses_xml
                ],
            )
        else:
            reprint_addresses = None

        if keywords_xml := fullrecord_metadata.find("keywords", NS):
            keywords = [keyword.text for keyword in keywords_xml]
        else:
            keywords = None

        if abstracts_xml := fullrecord_metadata.find("abstracts", NS):
            abstract_texts = [
                abstract.text
                for abstracts in abstracts_xml
                for abstract in abstracts.find("abstract_text", NS)
            ]

        else:
            abstract_texts = None

        return cls(
            languages=[
                Language.from_xml(language)
                for language in fullrecord_metadata.find("languages", NS)
            ],
            normalized_languages=[
                Language.from_xml(language)
                for language in fullrecord_metadata.find("normalized_languages", NS)
            ],
            normalized_doctypes=[
                doctype.text
                for doctype in fullrecord_metadata.find("normalized_doctypes", NS)
            ],
            references=[
                Reference.from_xml(ref)
                for ref in fullrecord_metadata.find("references", NS)
            ],
            addresses=[
                AddressName.from_xml(address_name)
                for address_name in fullrecord_metadata.find("addresses", NS)
            ],
            reprint_addresses=reprint_addresses,
            category_info=(
                CategoryInfo.from_xml(category_info_xml)
                if (category_info_xml := fullrecord_metadata.find("category_info", NS))
                else None
            ),
            fund_ack=(
                FundAck.from_xml(fund_ack_xml)
                if (fund_ack_xml := fullrecord_metadata.find("fund_ack", NS))
                else None
            ),
            keywords=keywords,
            abstracts=abstract_texts,
        )
