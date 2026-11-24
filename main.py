"""Fortune in a Pot — writes one kind, funny fortune for a houseplant.

The fortune is written to /output/entry.txt (UTF-8, one line, <= 120 chars).
Pure standard library; no network, no secrets, no files read.
"""

import os

FORTUNE = (
    "The sun has saved its best light just for you — this spring, you'll "
    "outgrow the windowsill and take over the room."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
