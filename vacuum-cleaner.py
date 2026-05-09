#CIT-223-054/2024
#STEPHEN MUIGA KIRAGU

#VACUUM CLEANER AGENT
# This program simulates a simple AI vacuum cleaner agent.
# The agent moves between rooms:
# Each room can either be:
#   -Dirty
#   -Clean
# Rules:
# 1. If the current room is dirty -> clean it
# 2. If current room is clean -> MOVE to the other rooms
# 3. Stop when all rooms are clean


# Environment/house
rooms = {
    "A": "Dirty",
    "B": "Dirty",
    "C": "Dirty",
    "D": "Dirty",
    "E": "Dirty"
}

# List of room names

room_names = list(rooms.keys())
# Start position
current_index = 0

# Function to display environment
def display_rooms():
    print("\nCurrent Room Status:")
    for room, status in rooms.items():
        print(f"Room {room}: {status}")

# Vacuum agent function
def vacuum_agent(room):

    print(f"\nVacuum is in Room {room}")

    if rooms[room] == "Dirty":
        print("Room is Dirty -> Cleaning...")
        rooms[room] = "Clean"

    else:
        print("Room already Clean.")


# Main Program
print("ROOM VACUUM CLEANER AGENT ")
while True:

    # Show environment
    display_rooms()

    # Current room
    current_room = room_names[current_index]

    # Run agent
    vacuum_agent(current_room)

    # Goal test
    if all(status == "Clean" for status in rooms.values()):
        print("\nAll rooms are clean.")
        break

    # Move to next room
    current_index = (current_index + 1) % len(room_names)

    print(f"Moving to Room {room_names[current_index]}...")


# Final status
display_rooms()