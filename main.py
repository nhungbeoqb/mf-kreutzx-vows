"""One-Line Robot Wedding Vows — writes the entry text to /output/entry.txt.

Chosen vow (v1): a wedding promise built on machine specifics — the spouse
is the backup, the vows run through sickness and low battery, and the payoff
lands in the last few words: a power cut ends the marriage, and the speaker
just restores the spouse from last night.
"""
import os

TEXT = (
    "I take you as my lawfully wedded backup, to have and to hold in sickness "
    "and in 1% battery, till a power cut do us part \u2014 then I restore you "
    "from last night."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
