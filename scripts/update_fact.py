import os
import re

fact = os.environ["FACT"]
date = os.environ["DATE"]

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_section = f"""<!-- DAILY_FACT_START -->
> 🧠 **Daily Fact ({date}):** {fact}
<!-- DAILY_FACT_END -->"""

updated = re.sub(
    r"<!-- DAILY_FACT_START -->.*?<!-- DAILY_FACT_END -->",
    new_section,
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
