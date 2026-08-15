import os
import json

output_dir = r"c:\Oikos Univ\files_analysis"
with open(os.path.join(output_dir, "transcripts.json"), "r", encoding="utf-8") as f:
    transcripts = json.load(f)

f1 = "2026-08-10 17-10-20.mp4"
f2 = "2026-08-10 17-11-58.mp4"

print("--- File 1: 2026-08-10 17-10-20.mp4 ---")
print(transcripts.get(f1, {}).get("text", ""))

print("\n--- File 2: 2026-08-10 17-11-58.mp4 ---")
print(transcripts.get(f2, {}).get("text", ""))
