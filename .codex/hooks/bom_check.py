from pathlib import Path
import os
import sys


def main() -> None:
    root_value = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("ASSISTANT_ROOT", "<ASSISTANT_ROOT>")
    root = Path(root_value).expanduser()
    if not root.exists():
        print(f"BOM check skipped: assistant root not found: {root}")
        return

    extensions = {".md", ".json", ".toml", ".yml", ".yaml", ".txt"}
    fixed = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in extensions:
            continue
        data = path.read_bytes()
        if data.startswith(b"\xef\xbb\xbf"):
            path.write_bytes(data[3:])
            fixed.append(str(path))

    if fixed:
        print("BOM check fixed files:")
        for item in fixed:
            print(f"- {item}")
    else:
        print("BOM check passed: 0 files with UTF-8 BOM")


if __name__ == "__main__":
    main()
