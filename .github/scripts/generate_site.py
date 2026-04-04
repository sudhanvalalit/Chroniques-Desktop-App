import datetime
import json
import os
import urllib.request
from pathlib import Path


def _fetch_latest_release(repo: str, token: str) -> dict:
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")

    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def _format_release_section(release: dict) -> str:
    tag = release.get("tag_name", "N/A")
    name = release.get("name") or tag
    release_url = release.get("html_url", "")
    published_at = release.get("published_at", "")
    body = (release.get("body") or "No release notes provided.").strip()
    assets = release.get("assets", [])

    published_display = "N/A"
    if published_at:
        published_display = published_at.split("T", 1)[0]

    lines = [
        "## Latest Release",
        f"- Version: [{name}]({release_url}) (`{tag}`)",
        f"- Published: {published_display}",
    ]

    if assets:
        lines.append("- Downloads:")
        for asset in assets:
            label = asset.get("name", "Asset")
            url = asset.get("browser_download_url", release_url)
            lines.append(f"  - [{label}]({url})")
    else:
        lines.append(f"- Downloads: [View all release assets]({release_url})")

    lines.extend(["", "### Release Notes", "", body, ""])
    return "\n".join(lines)


def _strip_main_title(readme_text: str) -> str:
    lines = readme_text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].startswith("# "):
        lines.pop(0)
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    repo = os.environ.get("GITHUB_REPOSITORY", "").strip()
    token = os.environ.get("GITHUB_TOKEN", "").strip()

    if not repo or not token:
        raise RuntimeError("GITHUB_REPOSITORY and GITHUB_TOKEN are required.")

    root = Path.cwd()
    readme_path = root / "README.md"
    site_dir = root / "site"
    site_dir.mkdir(parents=True, exist_ok=True)

    readme_text = readme_path.read_text(encoding="utf-8")
    release = _fetch_latest_release(repo, token)

    release_section = _format_release_section(release)
    readme_body = _strip_main_title(readme_text)
    generated_at = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    index_content = "\n".join(
        [
            "---",
            "title: Chroniques Desktop App",
            "theme: jekyll-theme-architect",
            "---",
            "",
            "# Chroniques Desktop App",
            "",
            "_This page is automatically generated from the latest GitHub release and README on main._",
            "",
            release_section,
            "## Features And Documentation",
            "",
            readme_body,
            f"_Last updated: {generated_at}_",
            "",
        ]
    )

    (site_dir / "index.md").write_text(index_content, encoding="utf-8")
    (site_dir / "_config.yml").write_text("theme: jekyll-theme-architect\n", encoding="utf-8")


if __name__ == "__main__":
    main()