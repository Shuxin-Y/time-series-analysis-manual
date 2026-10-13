import textwrap

import audit_flowcharts as audit
import sitekit


def test_main_exit_status_follows_errors(tmp_path, capsys):
    root = tmp_path
    docs = root / "docs"
    (docs / "flowcharts").mkdir(parents=True)
    (docs / "glossary").mkdir()
    (docs / "01-workflow").mkdir()
    sitekit.write_project(root, {}, nav=["01-workflow/index.md"])
    (docs / "01-workflow" / "index.md").write_text(
        '# P1: Data\n\n```mermaid\ngraph TD\n    P1["P1: Data"] --> P2["P2 Gate"]\n```\n', encoding="utf-8")
    (docs / "flowcharts" / "inventory.yml").write_text(textwrap.dedent('''
        nodes:
          - id: P1
            label: "P1: Data"
            phase: MASTER
            areas: [31]
            section: "01-workflow/index.md#p1-data"
    '''), encoding="utf-8")
    status = audit.main(["--root", str(root)])
    out = capsys.readouterr().out
    assert status == 1
    assert "leaf P2 has no inventory row" in out
    assert out.strip().endswith("1 error(s), 0 warning(s)")

    (docs / "flowcharts" / "inventory.yml").write_text(textwrap.dedent('''
        nodes:
          - id: P1
            label: "P1: Data"
            phase: MASTER
            areas: [31]
            section: "01-workflow/index.md#p1-data"
          - id: P2
            label: "P2 Gate"
            phase: MASTER
            areas: [31]
            section: "01-workflow/index.md#p1-data"
    '''), encoding="utf-8")
    assert audit.main(["--root", str(root)]) == 0
