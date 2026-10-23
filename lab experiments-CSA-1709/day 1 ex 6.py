def vacuum_cleaner():
    # Initial state: Dictionary mapping room to its status ('Dirty' or 'Clean')
    # Let's assume Room A is dirty and Room B is dirty, and vacuum starts at Room A
    room_status = {'A': 'Dirty', 'B': 'Dirty'}
    vacuum_location = 'A'
    
    print(f"Initial Location: Room {vacuum_location}")
    print(f"Initial Status: {room_status}\n")
    
    cost = 0
    
    for room in ['A', 'B']:
        vacuum_location = room
        print(f"Vacuum moved to Room {vacuum_location}.")
        cost += 1 # Movement cost
        
        if room_status[vacuum_location] == 'Dirty':
            print(f"Room {vacuum_location} is Dirty. Cleaning...")
            room_status[vacuum_location] = 'Clean'
            cost += 1 # Sucking cost
        else:
            print(f"Room {vacuum_location} is already Clean.")
            
    print("\n--- Final Status ---")
    print(f"Room Status: {room_status}")
    print(f"Total Performance Cost: {cost}")

if __name__ == "__main__":
    vacuum_cleaner()
