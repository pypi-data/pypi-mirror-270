from dataclasses import dataclass
from xml.etree.ElementTree import Element


@dataclass
class Subject:
    """An object representing subject of a record"""

    label: str
    """Label of the subject"""
    ascatype: str = None
    """ASCA type of the subject (e.g. traditional or extended)"""
    content_id: str = None
    """TODO"""
    content_type: str = None
    """TODO"""

    @classmethod
    def from_xml(cls, subject: Element):
        """Generates a Subject object from a subject XML element"""
        # Sanitize attribute names
        keys = list(subject.attrib.keys())
        for key in keys:
            if "-" in key:
                subject.attrib[key.replace("-", "_")] = subject.attrib[key]
                subject.attrib.pop(key)

        return cls(**subject.attrib, label=subject.text)
