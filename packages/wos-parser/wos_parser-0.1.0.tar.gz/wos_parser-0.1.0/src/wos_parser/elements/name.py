from dataclasses import dataclass
from xml.etree.ElementTree import Element

from wos_parser.constants import NS


@dataclass
class Name:
    """A Name object represents a name of an author, publisher, or other role"""

    display_name: str = None
    """Full name. If no full name is given, then the display_name is the wos_standard name."""
    full_name: str = None
    """Full name as given by the source publication."""
    wos_standard: str = None
    """Surname followed by a comma and up to five initials."""
    first_name: str = None
    """First (given) name"""
    last_name: str = None
    """Surname or family name"""
    suffix: str = None
    """Generational suffix from a given name (JR, III, etc.)"""
    email_addr: str = None
    """Email address"""
    seq_no: str = None
    """Position of author in author list"""
    addr_no: str = None
    """Indicates which address in the address field is associated with this author. An author can be associated with multiple addresses."""
    role: str = None
    """Role. Possible values include author, editor and inventor. The full list of roles can be found in the schema document common_types.rawxml.public.xsd"""
    reprint: str = None
    """Reprint flag. A value of Y indicates that the author is the reprint author."""
    orcid_id: str = None
    """ORCID identifier provided by the publication"""
    orcid_id_tr: str = None
    """ORCID identifier as captured by TR"""  # TODO: Find out what TR is
    r_id: str = None
    """Researcher identifier"""
    unified_name: str = None
    """Unified name"""

    @classmethod
    def from_xml(cls, name: Element):
        """Create a Name object from an name XML element"""
        return cls(
            **name.attrib,
            **{child.tag.replace("{" + NS[""] + "}", ""): child.text for child in name},
        )
