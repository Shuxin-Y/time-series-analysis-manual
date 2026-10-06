"""Browser smoke test: build the site, serve it, click a flowchart leaf and walk a glossary chain.

Needs Playwright with Chromium (`pip install playwright && playwright install chromium`); skipped otherwise.
The CDN scripts (Mermaid, MathJax, js-yaml) are loaded from the network, as on the published site.
"""
import re
import socket
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

sync_api = pytest.importorskip("playwright.sync_api")

REPO = Path(__file__).resolve().parents[2]
# Material's repository widget asks api.github.com for the latest release; the repository has none (404).
ALLOWED_ERROR_ORIGIN = "api.github.com"


class _LoopbackServer(ThreadingHTTPServer):
    address_family = socket.AF_INET6


class _QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@pytest.fixture(scope="module")
def site_url(tmp_path_factory):
    from mkdocs.commands.build import build
    from mkdocs.config import load_config

    site_dir = tmp_path_factory.mktemp("site")
    build(load_config(config_file=str(REPO / "mkdocs.yml"), site_dir=str(site_dir)))
    server = _LoopbackServer(("::1", 0), partial(_QuietHandler, directory=str(site_dir)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://[::1]:{server.server_address[1]}/"
    server.shutdown()


@pytest.fixture(scope="module")
def page():
    with sync_api.sync_playwright() as p:
        try:
            browser = p.chromium.launch()
        except sync_api.Error as exc:
            pytest.skip(f"Chromium is not installed for Playwright: {exc}")
        page = browser.new_page()
        page.console_errors = []

        def record(message):
            if message.type == "error" and ALLOWED_ERROR_ORIGIN not in (message.location or {}).get("url", ""):
                page.console_errors.append(message.text)

        page.on("console", record)
        page.on("pageerror", lambda exc: page.console_errors.append(str(exc)))
        yield page
        browser.close()


def svg_node(page, node_id):
    page.wait_for_selector(".mermaid-container g.node.flowchart-link", timeout=20000)
    dom_id = page.evaluate(
        "nid => [...document.querySelectorAll('g.node[id]')].map(g => g.id).find(id => new RegExp('^flowchart-' + nid + '-\\\\d+$').test(id))",
        node_id)
    assert dom_id, f"no rendered node {node_id}"
    return page.locator(f'[id="{dom_id}"]')


def test_leaf_click_lands_on_its_section(page, site_url):
    page.goto(site_url + "01-workflow/p07-error-process/")
    garch = svg_node(page, "P7_GARCH")
    garch.scroll_into_view_if_needed()
    garch.click()
    page.wait_for_url(re.compile(r".*reference/10-volatility/#garch$"))
    assert page.url.endswith("reference/10-volatility/#garch")


def test_glossary_chip_opens_the_upstream_term(page, site_url):
    page.goto(site_url + "reference/04-estimation/")
    page.locator('.glossary-term[data-term="Joint density"]').first.click()
    drawer = page.locator(".glossary-drawer.open")
    drawer.wait_for(timeout=10000)
    assert drawer.locator("h3").inner_text().startswith("Joint density")
    drawer.locator('.glossary-chip[data-term="Independence"]').click()
    page.wait_for_function("() => document.querySelector('.glossary-drawer h3').textContent.startsWith('Independence')")
    assert "Joint density" in page.locator(".glossary-crumbs").inner_text()
    for disabled in ("", "design-system-showcase/"):  # GLOSSARY_DISABLED_PAGES, read from glossary/index.yml
        page.goto(site_url + disabled)
        page.wait_for_load_state("networkidle")
        assert page.locator(".glossary-term").count() == 0, disabled


def test_no_console_errors(page, site_url):
    assert page.console_errors == []
