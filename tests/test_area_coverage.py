"""Spec acceptance criterion 3: every one of the 34 areas has at least one leaf in some sub-diagram.

Master phase boxes sit on the master diagram, not in a sub-diagram, so their areas do not count.
"""
from pathlib import Path

import audit_flowcharts as audit
import sitekit


def test_every_area_has_a_leaf():
    docs = Path(audit.load_site_config(sitekit.REPO / "mkdocs.yml")["docs_dir"])
    rows, findings = audit.load_inventory(docs.joinpath(*audit.INVENTORY_PATH))
    assert not findings
    covered = {a for r in rows if r.phase != audit.MASTER_PHASE for a in r.areas}
    missing = sorted(set(audit.AREAS) - covered)
    assert not missing, f"areas without a leaf: {missing}"
