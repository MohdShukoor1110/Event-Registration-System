"""
A global dictionary to store all event data.
Each key is the event name, and the value is a dictionary of event details.
"""
events = {}

"""
Prompts the user to enter event details and creates a new event entry.
The event is stored as a dictionary within the 'events' dictionary.
"""
def create_event():
    print()
    name = input("Enter event name: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    location = input("Enter event location: ")
    capacity = int(input("Enter event capacity: "))
    
    # Store event details in a dictionary with an empty list for participants
    events[name] = {
        "date": date,
        "location": location,
        "capacity": capacity,
        "participants": []
    }
    print(f"Event '{name}' created successfully!")

"""
Allows a user to register for an existing event.
It checks if the event exists and if it has not reached its capacity.
"""
def register_participant():
    if not events:
        print()
        print("No events registered yet.")
        return
    print()
    event_name = input("Enter the event name you want to register for: ")
    
    # Check if the entered event name exists as a key in the events dictionary
    if event_name in events:
        
        # Check if the event is at full capacity
        if len(events[event_name]["participants"]) < events[event_name]["capacity"]:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            events[event_name]["participants"].append({
                "name": name,
                "email": email
            })
            print(f"Participant '{name}' registered successfully for event '{event_name}'!")
        else:
            print(f"Sorry, the event '{event_name}' is already at full capacity.")
    else:
        print(f"No such event named '{event_name}' found.")

"""
Displays a list of all registered events and their details.
"""
def list_events():
    if len(events) != 0:
        print()
        print("Available Events:")
        for event_name, details in events.items():
            print(f"Event: {event_name}, Date: {details['date']}, Location: {details['location']}, Registrations: {len(details['participants'])}/{details['capacity']}")
    else:
        print()
        print("No events available.")

"""
Prints the list of participants for a specific event.
"""
def generate_participant_list():
    if not events:
        print()
        print("No events registered yet.")
        return
    print()
    event_name = input("Enter the event name to get the participant list: ")
    
    # Check if the event name exists
    if event_name in events:
        print()
        print(f"Participants for event '{event_name}':")
        for participant in events[event_name]["participants"]:
            print(f"Name: {participant['name']}, Email: {participant['email']}")
    else:
        print(f"No such event named '{event_name}' found.")

"""
The main function that runs the event registration system.
It displays a menu and calls other functions based on user choice.
"""
def main():
    while True:
        print("\nEvent Registration System")
        print("1. Create Event")
        print("2. Register Participant")
        print("3. List Events")
        print("4. Generate Participant List")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            create_event()
        elif choice == 2:
            register_participant()
        elif choice == 3:
            list_events()
        elif choice == 4:
            generate_participant_list()
        elif choice == 5:
            # Exit the main loop and end the program
            print()
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to start the application
if __name__ == "__main__":
    main()