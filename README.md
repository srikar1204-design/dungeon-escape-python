# Dungeon Escape (Python)

Small text-based game I wrote while learning Python.

You start in a room and move around using simple text commands like `go north` or `go east`. Somewhere in the map there’s a key, and once you grab it you can unlock a heavy metal door and escape.

## Commands

- `go <direction>` – move to another room (e.g. `go north`)
- `take <item>` – pick up an item in the room (e.g. `take key`)
- `inventory` – see what you're holding
- `look` – reprint the current room description
- `help` – show all commands
- `quit` – exit the game

## How to run

From the project folder:

```bash
python3 dungeon_escape.py
