"""
JD / CV Tailoring Assistant.
Lee perfil desde _shared/config; analiza JD; sugiere headline, summary, bullets y "why I fit".
NO inventa experiencia ni herramientas fuera del perfil o no-claim-list.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHARED = ROOT.parent / "_shared"
sys.path.insert(0, str(SHARED))

import yaml

CONFIG = SHARED / "config"
PROFILE_PATH = CONFIG / "profile.yaml"
NO_CLAIM_PATH = CONFIG / "no-claim-list.txt"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

# Keywords que indican rol BI / Data Analyst (para scoring)
BI_KEYWORDS = [
    "sql", "power bi", "dax", "kpi", "dashboard", "excel", "power query",
    "data quality", "reporting", "analytics", "etl", "data model", "star schema",
    "reconciliation", "retail", "profitability", "recurrence", "retention",
]

def load_profile():
    with open(PROFILE_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_no_claim():
    with open(NO_CLAIM_PATH, encoding="utf-8") as f:
        lines = [l.strip().lower() for l in f if l.strip() and not l.startswith("#")]
    return [x for x in lines if x]

def extract_keywords(text):
    text_lower = text.lower()
    words = set(re.findall(r"[a-z][a-z0-9']+", text_lower))
    # Bigrams comunes
    bigrams = set(re.findall(r"power bi|power query|data quality|star schema|kpi", text_lower))
    return words | bigrams

def score_jd_fit(text, profile_keywords, no_claim):
    text_lower = text.lower()
    hits = [k for k in profile_keywords if k in text_lower]
    warnings = [n for n in no_claim if n in text_lower]
    bi_hits = [k for k in BI_KEYWORDS if k in text_lower]
    return {
        "profile_keywords_in_jd": hits,
        "bi_keywords_in_jd": bi_hits,
        "no_claim_mentioned": warnings,
        "suggest_emphasize": [k for k in profile_keywords if k in text_lower][:15],
    }

def suggest_headline(profile, fit):
    primary = profile["positioning"]["primary"]
    emphasize = fit.get("suggest_emphasize", [])[:3]
    parts = [primary]
    if "sql" in [x.lower() for x in emphasize]: parts.append("SQL")
    if "power bi" in [x.lower() for x in emphasize]: parts.append("Power BI")
    if "kpi" in [x.lower() for x in emphasize]: parts.append("KPI & Reporting")
    return " | ".join(parts[:4])

def suggest_summary(profile, fit):
    lines = [
        profile["positioning"]["primary"] + " with focus on " + ", ".join(profile["positioning"]["stack_order"][:3]) + ".",
        "Experience in " + ", ".join(profile["strengths"][:4]) + ".",
        "Business-oriented, KPI and data quality focused; clear documentation and traceability.",
    ]
    return " ".join(lines)

def suggest_bullets(profile, fit):
    strengths = profile.get("strengths") or []
    emphasize = [str(k).lower() for k in fit.get("suggest_emphasize", [])]
    ordered = []
    for s in strengths:
        s_str = str(s) if isinstance(s, str) else ""
        if not s_str:
            continue
        if any(k in s_str.lower() for k in emphasize):
            ordered.insert(0, s_str)
        else:
            ordered.append(s_str)
    return ordered[:6]

def suggest_why_fit(profile, fit):
    parts = [
        "My profile aligns with the role: " + profile["positioning"]["primary"] + ".",
        "I work daily with " + ", ".join(profile["positioning"]["stack_order"][:4]) + ".",
    ]
    if fit.get("profile_keywords_in_jd"):
        parts.append("The JD emphasizes " + ", ".join(fit["profile_keywords_in_jd"][:5]) + ", which I use in my current work.")
    parts.append("I focus on KPIs, data quality, and business-ready reporting, not on tools I have not used.")
    return " ".join(parts)

def main():
    if len(sys.argv) > 1:
        jd_path = Path(sys.argv[1])
        jd_text = jd_path.read_text(encoding="utf-8")
    else:
        jd_text = sys.stdin.read()
    if not jd_text.strip():
        print("No JD text provided. Usage: python tailor.py < jd.txt  or  python tailor.py jd.txt")
        return

    profile = load_profile()
    no_claim = load_no_claim()
    profile_keywords = [k.lower() for k in profile.get("keywords", [])]
    fit = score_jd_fit(jd_text, profile_keywords + BI_KEYWORDS, no_claim)

    headline = suggest_headline(profile, fit)
    summary = suggest_summary(profile, fit)
    bullets = suggest_bullets(profile, fit)
    why_fit = suggest_why_fit(profile, fit)

    out_lines = [
        "# JD Tailoring Output",
        "",
        "## Keywords in JD (from your profile)",
        ", ".join(fit["profile_keywords_in_jd"]) if fit["profile_keywords_in_jd"] else "(none)",
        "",
        "## [!] Do NOT claim (mentioned in JD)",
        ", ".join(fit["no_claim_mentioned"]) if fit["no_claim_mentioned"] else "(none)",
        "",
        "## Recommended headline",
        headline,
        "",
        "## Suggested summary (adapt manually)",
        summary,
        "",
        "## Bullets to emphasize (from your profile)",
        *("- " + b for b in bullets),
        "",
        "## Why I fit (skeleton)",
        why_fit,
    ]
    report = "\n".join(out_lines)
    print(report)

    out_file = OUT / "tailoring_latest.md"
    out_file.write_text(report, encoding="utf-8")
    print(f"\nSaved to {out_file}")

if __name__ == "__main__":
    main()
