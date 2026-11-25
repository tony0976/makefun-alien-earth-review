"""Writes an alien tourist's one-line review of Earth to /output/entry.txt."""
import os

TEXT = "Earth review: lovely planet, but the locals pay rent to sleep on a rock flying through space, then complain they never get enough rest. Three stars, would abduct again."

# Rule: the review must be a single line of 1 to 200 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
