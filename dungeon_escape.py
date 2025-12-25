# dungeon_escape.py
# Text adventure: move between rooms, pick up items, escape with a key.

# --- WORLD SETUP ---

rooms = {
    "foyer": {
        "description": "You are in a small, dusty foyer. There is a door to the north and a hallway to the east.",
        "exits": {
            "north": "library",
            "east": "hallway"
        },
        "items": []
    },
    "library": {
        "description": "You are in a quiet library filled with old books. Something glints on a table.",
        "exits": {
            "south": "foyer"
        },
        "items": ["key"]
    },
    "hallway": {
        "description": "You are in a narrow hallway. The foyer is to the west, and a heavy metal door lies to the east.",
        "exits": {
            "west": "foyer",
            "east": "exit"
        },
        "items": []
    },
    "exit": {
        "description": "A heavy metal door leading outside. Fresh air seeps in through the cracks.",
        "exits": {},
        "items": []
    }
}

current_room = "foyer"      # player starts here
inventory = []              # what the player is carrying


# --- HELPER FUNCTIONS ---

def show_room():
    """Print where the player is and what they see."""
    room = rooms[current_room]
    print(f"\n== {current_room.upper()} ==")
    print(room["description"])

    if room["items"]:
        print("You see:", ", ".join(room["items"]))

    exits = ", ".join(room["exits"].keys())
    if exits:
        print(f"Exits: {exits}")


def show_help():
    """Print available commands."""
    print("Commands:")
    print("  go <direction>   - move to another room (e.g. 'go north')")
    print("  take <item>      - pick up an item (e.g. 'take key')")
    print("  inventory        - show what you're carrying")
    print("  look             - re-show the room description")
    print("  help             - show this help")
    print("  quit             - quit the game")


def move(direction):
    """Try to move in the given direction. Handle locked exit."""
    global current_room
    room = rooms[current_room]

    if direction not in room["exits"]:
        print("You can't go that way.")
        return

    next_room = room["exits"][direction]

    # If trying to go to exit without key, block
    if next_room == "exit" and "key" not in inventory:
        print("The door is locked. You probably need a key.")
        return

    current_room = next_room
    print(f"You move {direction}...")

    # Check win condition
    if current_room == "exit":
        print("\nYou unlock the door and step into the fresh air. You escaped!")
        raise SystemExit


def take_item(item_name):
    """Take an item from the room and put it in inventory."""
    room = rooms[current_room]
    if item_name in room["items"]:
        room["items"].remove(item_name)
        inventory.append(item_name)
        print(f"You pick up the {item_name}.")
    else:
        print("You don't see that here.")


def show_inventory():
    """List items the player is carrying."""
    if inventory:
        print("You are carrying:", ", ".join(inventory))
    else:
        print("You are not carrying anything.")


# --- GAME LOOP ---

print("Welcome to Dungeon Escape!")
print("Find a way out. Type 'help' for commands.\n")

while True:
    show_room()
    command = input("\n> ").strip().lower()

    if command in ("quit", "exit"):
        print("You give up and sit down in the dust. Game over.")
        break

    elif command == "help":
        show_help()

    elif command == "look":
        # show_room() will run again at the top of the loop
        continue

    elif command == "inventory":
        show_inventory()

    elif command.startswith("go "):
        _, direction = command.split(" ", 1)
        move(direction)

    elif command.startswith("take "):
        _, item_name = command.split(" ", 1)
        take_item(item_name)

    else:
        print("I don't understand that command. Type 'help' for options.")
