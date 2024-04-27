from dataclasses import dataclass
from typing import List
from xml.etree.ElementTree import Element

from wos_parser.constants import NS
from wos_parser.elements import PhysicalSection


@dataclass
class Reference:
    """An object representing a reference cited in a publication"""

    uid: str = None
    """Cited reference identifier. There are two types of uid values: 1) the UID of
a matching source item in Web of Science and 2) the UID of the parent
(citing) document, followed by an increment. A value of the second type
indicates a reference for which there is no matching source item.

Note that because of data corrections and deletions, the uid of a cited
reference can change. In addition, a uid can be added to a cited reference
that previously had none. """
    occurenceOrder: str = None
    """Position in the publication's bibliography."""
    citedAuthor: str = None
    """First author of the cited document."""
    year: str = None
    """Publication year of the cited document"""
    page: str = None
    """Starting page number of the cited document.

Be aware that the value of the `page` attribute may be an identifier such
as ARTN (article number). The identifier may appear twice in a cited
reference, once in the `page` attribute and once in the `art_no` attribute."""
    citedTitle: str = None
    """Title of the cited document.

For references processed from 2012 forward, cited references are
captured with full titles when those titles are supplied by the citing article,
regardless of whether the cited reference matches a source item.

For references processed prior to 2012, it is likely that a citing title will not
be included. However, some earlier cover dates may have been updated
in 2012 or later. In this case there may be a full citing title presented if the
title is covered as a source, or the author included the full cited title in the
reference."""
    citedWork: str = None
    """Title of the cited publication.

The value of this element may be a full work title or an abbreviated work
title.

The full work title is shown if the reference is from an article processed in
2012 or later and the cited publication is also a source publication or the
author included the full title in the reference. An abbreviated work is shown
if the reference refers to a publication that is not covered as a source and
the author did not provide the full work title or the cited reference is from
an article processed before 2012."""
    doi: str = None
    """Digital Object Identifier.

From 2002 forward, the doi of a cited reference is captured when supplied
by the citing article."""
    volume: str = None
    """Volume the pubication appeared in."""
    art_no: str = None
    """Article number.

The article number is a unique item identifier assigned by the journal in
which the citing article is published and not by the authors of the citing
article. This identifier is prefaced by ARTN (for article number), PII (for
publisher item identifier), or UNSP (for unspecified).
Not all cited references have this element.
    """
    assignee: str = None
    """The assignee of a cited patent."""
    patent_no: str = None
    """Number of a cited patent."""
    physicalSections: List[PhysicalSection] = None
    """List of PhysicalSection objects, where each one represents a citation location of this reference"""

    @classmethod
    def from_xml(cls, reference: Element):
        """Creates a Reference object from an reference XML element"""
        physicalSections = [
            PhysicalSection.from_xml(child)
            for child in reference
            if (name := child.tag.replace("{" + NS[""] + "}", "")) == "physicalSection"
        ]
        if len(physicalSections) == 0:
            physicalSections = None
        return cls(
            **reference.attrib,
            **{
                name: child.text
                for child in reference
                if (name := child.tag.replace("{" + NS[""] + "}", ""))
                != "physicalSection"
            },
            physicalSections=physicalSections,
        )
