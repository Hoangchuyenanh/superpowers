"""Run unittest in a Windows Python project's own virtual environment."""

import argparse
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Path to the project folder")
    args = parser.parse_args()

    project = args.project.expanduser().resolve()
    if not (project / "tests").is_dir():
        parser.error(f"No tests folder in {project}")

    python = project / ".venv" / "Scripts" / "python.exe"
    if not python.is_file():
        parser.error(f"Create the project's virtual environment first: {python}")

    print(f"Running tests in {project}", flush=True)
    result = subprocess.run(
        [str(python), "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=project,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
