import csv
import io

rows = [
    {
        "title": "Trump kneecaps Anthropic, SpaceX bags Cursor and Databricks debuts AI agent coworker",
        "source": "SiliconANGLE",
        "url": "https://siliconangle.com/2026/06/19/trump-kneecaps-anthropic-spacex-bags-cursor-databricks-debuts-ai-agent-coworker/",
        "date": "2026-06-19"
    },
    {
        "title": "GPT-5.6 Rumors Heat Up as Users Swear ChatGPT Suddenly Got Smarter",
        "source": "Decrypt",
        "url": "https://decrypt.co/371699/openai-gpt-5-6-chatgpt-stealth-testing-rumors",
        "date": "2026-06-19"
    },
    {
        "title": "Arbor framework outperforms Claude Code and Codex by 2.5x in AI optimization benchmarks",
        "source": "Crypto Briefing",
        "url": "https://cryptobriefing.com/arbor-framework-outperforms-claude-code-codex/",
        "date": "2026-06-18"
    }
]

output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=["title","source","url","date"])
writer.writeheader()
for r in rows:
    writer.writerow(r)

with open("report.csv", "w", newline="") as f:
    f.write(output.getvalue().replace('\r\n', '\n'))

print("report.csv written successfully")
with open("report.csv", "r") as f:
    print(f.read())