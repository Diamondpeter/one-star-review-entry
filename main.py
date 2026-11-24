#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review of gravity to /output/entry.txt.
The review is 89 characters, inside the bounty gate of 1 to 160.
"""

import os

REVIEW = (
    "Gravity works fine until you drop something expensive. "
    "Then it works perfectly. One star."
)


def main() -> None:
    review = REVIEW.strip()
    if not 1 <= len(review) <= 160 or not review.strip():
        raise ValueError(f"review is {len(review)} characters, must be 1-160")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(review)
    print(f"wrote {len(review)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
