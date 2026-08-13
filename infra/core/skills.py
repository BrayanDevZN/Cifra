"""
salva o nome e o caminho das skills
"""
from pathlib import Path
BASIC_PATH = Path("repository/prompts/")

CMD = {
    "name": "cmd",
    "path": BASIC_PATH / "cmd.md"
}

MANAGER = {
    "name": "manager",
    "path": BASIC_PATH / "manager.md"
}

SECURITY = {
    "name": "security",
    "path": BASIC_PATH / "security.md"
}

CODE = {
    "name": "code",
    "path": BASIC_PATH / "code.md"
}