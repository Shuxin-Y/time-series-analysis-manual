"""Spec acceptance criterion 3: every one of the 34 areas has at least one leaf in some sub-diagram.

Area 1 (math foundations) is Part 0 by design (spec section 8): it is satisfied by foundation sections, the
phase-F rows that sub-diagrams draw as refs. Areas 2-34 need a leaf, so they count only rows that are neither
foundation sections nor master phase boxes (which sit on the master diagram, not in a sub-diagram).
"""
from pathlib import Path

import audit_flowcharts as audit
import sitekit

FOUNDATION_AREA = 1


def test_every_area_has_a_leaf():
    docs = Path(audit.load_site_config(sitekit.REPO / "mkdocs.yml")["docs_dir"])
    rows, findings = audit.load_inventory(docs.joinpath(*audit.INVENTORY_PATH))
    assert not findings
    foundation = {a for r in rows if r.phase == audit.FOUNDATION_PHASE for a in r.areas}
    leaves = {a for r in rows if r.phase not in (audit.FOUNDATION_PHASE, audit.MASTER_PHASE) for a in r.areas}
    assert FOUNDATION_AREA in foundation, "area 1 has no foundation section"
    missing = sorted(set(audit.AREAS) - {FOUNDATION_AREA} - leaves)
    assert not missing, f"areas without a leaf: {missing}"
