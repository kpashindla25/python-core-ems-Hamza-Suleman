import json
#im using a json file for this task as they are known to be the best for file handling
#especially when using dicionaries as i plan to use

#file handling

try:
    with open('events.json', 'r') as f:
        events = json.load(f)
except FileNotFoundError:
    events = {}
#this uses error handling to open the file events.json in read mode and read the file
#if the file does not exist then it creates it and also an events dictionary in the file

def write_to_file():
    with open('events.json', 'w') as f:
        json.dump(events, f)
#this will write the current dictionary events into the json file
#dump() is how python converts text into json format for saving
#this function will write everything to the file whenever it is called

#functions

def list_events():
    for event_id, event in sorted(events.items()):
        print(f"Event ID: {event_id} | Event Name: {event['name']} | Number of Attendees: {len(event['attendees'])}")
#this function prints out all of the events saved in the file
#it uses the dictionary to print the event id and the name of the event
#the sorted command ensures the events are sorted by id number

def create_event(event_id, name):
    events[event_id] = {'name': name, 'attendees': []}
    write_to_file()
    print(f"Event '{name}' created.")
#this will create an event by creating a new key in the dictionary in the json file and then write it to file

def edit_event(event_id,name):
    if event_id in events:
        events[event_id]['name'] = name
        write_to_file()
        print(f"Event {event_id} name successfully changed to: {events[event_id]['name']}.")
    else:
        print("Event not found.")
#this function will change the name of an event that the user specifies and will write it to the file

def delete_event(event_id):
    if event_id in events:
        events.pop(event_id)
        write_to_file()
        print(f"Event {event_id} successfully removed.")
    else:
        print("Event not found.")
#this function deletes an event that the user specifies and updates the file

def add_attendee(event_id, attendee):
    if event_id in events:
        events[event_id]['attendees'].append(attendee)
        write_to_file()
        print(f"{attendee} added to event {events[event_id]['name']}.")
    else:
        print("Event not found.")
#this function can add an attendee to a specific event by the id

def list_attendees(event_id):
    if event_id in events:
        for attendee in events[event_id]['attendees']:
            print(attendee)
    else:
        print("Event not found.")
#this function will list all of the attendees for a specific event

#body

def web_app():
    while True:
        print("\nEvent Management Web App")
        print("1. List Events")
        print("2. Create Event")
        print("3. Edit Event")
        print("4. Delete Event")
        print("5. Add Attendee")
        print("6. List Attendees")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            list_events()
        elif choice == '2':
            event_id = input("Enter Event ID: ")
            name = input("Enter Event Name: ")
            create_event(event_id, name)
        elif choice == '3':
            event_id = input("Enter Event ID To Edit: ")
            name = input("Enter New Event Name: ")
            edit_event(event_id,name)
        elif choice == '4':
            event_id = input("Enter Event ID: ")
            delete_event(event_id)
        elif choice == '5':
            event_id = input("Enter Event ID: ")
            attendee = input("Enter Attendee Name: ")
            add_attendee(event_id, attendee)
        elif choice == '6':
            event_id = input("Enter Event ID: ")
            list_attendees(event_id)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")
#this is the main body of the code, as we've created function for every option,
#we can just take a user input for an operation and pass parameters to a function based on their response

web_app()