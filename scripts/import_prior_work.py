"""Copy prior local coursework without nested Git metadata; verify every file."""
import csv
import hashlib
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = {
    "PYTHON": "Python/Previous-Practice",
    "ML-DL-CV": "ML-DL-CV/Previous-Practice",
    "LLM-Mastery": "LLM/Previous-Practice",
    "System-Design-Engineering": "System-Design-Engineer/Previous-Practice",
}
EXCLUDED = {".git", ".DS_Store", "node_modules", ".venv", "venv", "__pycache__", ".ipynb_checkpoints"}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    # After placement, old source paths are historical: do not recreate duplicates.
    manifest = ROOT / "docs" / "import-manifest.csv"
    if (ROOT / "docs" / "material-migration.json").exists():
        with manifest.open(encoding="utf-8", newline="") as handle:
            entries = list(csv.DictReader(handle))
        for entry in entries:
            target = (ROOT / entry["destination"]).resolve()
            if not target.is_relative_to(ROOT):
                raise ValueError(f"Manifest destination outside repository: {target}")
            if not target.is_file() or digest(target) != entry["sha256"]:
                raise ValueError(f"Imported file changed or missing: {target}")
        print(f"Verified {len(entries)} organized files. No files copied; original layout not recreated.")
        return
    rows = []
    for name, folder in MAPPING.items():
        source = ROOT.parent / name
        if not source.is_dir():
            raise FileNotFoundError(source)
        destination = ROOT / folder
        for path in sorted(source.rglob("*")):
            relative = path.relative_to(source)
            if any(part in EXCLUDED for part in relative.parts):
                continue
            if path.is_symlink():
                raise ValueError(f"Review symbolic link before importing: {path}")
            target = destination / relative
            if path.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            source_hash = digest(path)
            if target.exists() and digest(target) != source_hash:
                raise ValueError(f"Refusing to overwrite modified file: {target}")
            if not target.exists():
                shutil.copy2(path, target)
            if digest(target) != source_hash:
                raise ValueError(f"Copy verification failed: {target}")
            rows.append([name, relative.as_posix(), target.relative_to(ROOT).as_posix(), path.stat().st_size, source_hash])
        print(f"{name}: {sum(row[0] == name for row in rows)} files verified")
    (ROOT / "docs").mkdir(exist_ok=True)
    with (ROOT / "docs" / "import-manifest.csv").open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["repository", "source_relative_path", "destination", "bytes", "sha256"])
        writer.writerows(rows)

if __name__ == "__main__":
    main()
