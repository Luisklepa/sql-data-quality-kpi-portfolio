"""
Mock Interview Generator.
Genera preguntas (reclutador + técnicas), esqueletos de respuesta, follow-ups y advertencias.
Usa _shared/config para mantener consistencia y no inventar experiencia.
"""
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

def load_profile():
    with open(PROFILE_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_no_claim():
    with open(NO_CLAIM_PATH, encoding="utf-8") as f:
        return [l.strip().lower() for l in f if l.strip() and not l.startswith("#")]

def build_recruiter_questions(profile):
    return [
        "Tell me about yourself and your current role.",
        "Why are you interested in this position / company?",
        "What are your strengths and how do they apply to this role?",
        "Describe a time when you had to explain a complex analysis to a non-technical stakeholder.",
        "Where do you see yourself in 2–3 years?",
        "What is your experience with [SQL / Power BI / reporting]?",
        "How do you prioritize when you have multiple reporting requests?",
    ]

def build_technical_questions(profile):
    return [
        "How do you approach building a new KPI dashboard from scratch?",
        "Explain how you ensure data quality before publishing a report.",
        "Describe your experience with dimensional modeling (star schema).",
        "How do you reconcile numbers between source systems and the report?",
        "What DAX or SQL patterns do you use most often for KPIs?",
        "How do you handle missing or duplicate data in your pipelines?",
    ]

def build_answer_skeletons(profile):
    return {
        "tell_me_about_yourself": (
            "I am a " + profile["positioning"]["primary"] + ". "
            "I work with " + ", ".join(profile["positioning"]["stack_order"][:4]) + ". "
            "My focus is on " + ", ".join(profile["strengths"][:3]) + ". "
            "I am business-oriented and like to tie analysis to decisions and KPIs."
        ),
        "data_quality": (
            "I check for nulls in key columns, duplicate keys, and range violations (e.g. discount 0–100). "
            "I reconcile totals: same KPI from source vs from the report. "
            "I document assumptions and limitations so stakeholders know what they can trust."
        ),
        "dimensional_modeling": (
            "I use star schema: fact tables with measures (quantity, revenue) and dimension tables (customer, product, date). "
            "This allows slicing by business attributes and keeps the model clear for Power BI and SQL."
        ),
        "strengths": (
            "SQL and Power BI for reporting, DAX for measures, and a strong focus on data quality and traceability. "
            "I am comfortable with Excel and Power Query for ad-hoc analysis and automation."
        ),
    }

def build_weak_answer_warnings(no_claim):
    return [
        "Do not claim experience with: " + ", ".join(no_claim[:10]) + ".",
        "Do not describe yourself as 'senior' or 'data scientist' if the profile does not say so.",
        "Do not say 'we used ML' for Power BI native forecasting; call it forecasting or trend analysis.",
        "Do not invent projects or tools; stick to what you can explain in detail.",
    ]

def build_follow_ups():
    return [
        "Can you give a concrete example from a recent project?",
        "What would you do differently today?",
        "How did you measure success of that deliverable?",
        "What was the business impact?",
    ]

def main():
    jd_path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    jd_text = jd_path.read_text(encoding="utf-8") if jd_path and jd_path.exists() else ""

    profile = load_profile()
    no_claim = load_no_claim()

    recruiter_q = build_recruiter_questions(profile)
    technical_q = build_technical_questions(profile)
    skeletons = build_answer_skeletons(profile)
    warnings = build_weak_answer_warnings(no_claim)
    follow_ups = build_follow_ups()

    lines = [
        "# Mock Interview — " + profile["candidate"]["name"],
        "",
        "## Likely recruiter questions",
        *("- " + q for q in recruiter_q),
        "",
        "## Likely technical questions",
        *("- " + q for q in technical_q),
        "",
        "## Answer skeletons (adapt with concrete examples)",
        "",
    ]
    for k, v in skeletons.items():
        lines.append(f"### {k}")
        lines.append(v)
        lines.append("")
    lines.extend([
        "## Follow-up questions to prepare for",
        *("- " + q for q in follow_ups),
        "",
        "## [!] Weak-answer warnings",
        *("- " + w for w in warnings),
        "",
        "## Business framing — talking points",
        "- I focus on KPIs and decision support, not just building reports.",
        "- I validate data and reconcile numbers before publishing.",
        "- I document assumptions and limitations so the business can trust the numbers.",
        "- I use SQL and Power BI as my core tools; Python for automation and prep when needed.",
    ])
    if jd_text.strip():
        lines.extend([
            "",
            "## JD-specific note",
            "Review the job description and prepare 2–3 examples that match their requirements. "
            "Do not claim tools from the JD that are in your no-claim list.",
        ])

    report = "\n".join(lines)
    out_file = OUT / "mock_interview_latest.md"
    out_file.write_text(report, encoding="utf-8")
    print("Report generated. Saved to", str(out_file))

if __name__ == "__main__":
    main()
