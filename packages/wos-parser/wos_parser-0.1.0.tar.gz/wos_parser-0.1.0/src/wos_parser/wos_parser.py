"""Main module."""

from wos_parser.records import Record

from tqdm.auto import tqdm

from typing import List
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


class WosParser:
    """The main class representing the XML parser."""

    def __init__(self) -> None:
        pass

    def parse_record(self, record: Element) -> Record:
        """Parse a single record

        :param record: An XML representation of a Web of Science record
        :type record: Element
        :return: A Record object
        :rtype: Record
        """
        return Record.from_xml(record)

    def parse_records(self, xml_file: str) -> List[Record]:
        tree = ET.parse(xml_file)
        records = tree.getroot()

        return [self.parse_record(record) for record in tqdm(records)]


if __name__ == "__main__":
    # records = WosParser().parse_records(
    #     "samples/1953_CORE/WR_1953_20230128210149_CORE_0002.xml"
    # )
    records = WosParser().parse_records(
        "samples/2023_CORE/WR_2023_20230111080536_CORE_0001.xml"
    )
    # records = WosParser().parse_records("samples/2023_CORE/single_rec.xml")
    print(records[1])
