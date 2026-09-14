"""Validate one completed Micro Handbook card without external dependencies."""

from pathlib import Path
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REQUIRED_HEADINGS = (
    "## Короткий ответ",
    "## Шаги",
    "## Частая ошибка",
    "## Мини-пример",
)
FORBIDDEN_FRAGMENTS = (
    "Статус: **черновик**",
    "_заполните",
    "Опорный материал",
)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_card.py cards/<section>/<card>.md")
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"ERROR: card not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    problems = [
        heading for heading in REQUIRED_HEADINGS if heading not in text
    ]
    problems.extend(
        fragment for fragment in FORBIDDEN_FRAGMENTS if fragment in text
    )
    if problems:
        print("ERROR: incomplete card:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
