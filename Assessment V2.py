#Recreating my event management webapp using OOP instead of just functions

import json

class EventManager:
    def __init__(self):
        try:
            with open('events.json', 'r') as f:
                self.events = json.load(f)
        except FileNotFoundError:
            self.events = {}

    def write_to_file(self):
        with open('events.json', 'w') as f:
            json.dump(self.events, f)

    def list_events(self):
        for event_id, event in sorted(self.events.items()):
            print(f"Event ID: {event_id} | Event Name: {event['name']} | Number of Attendees: {len(event['attendees'])}")

    def create_event(self, event_id, name):
        self.events[event_id] = {'name': name, 'attendees': []}
        self.write_to_file()
        print(f"Event '{name}' created.")

    def edit_event(self, event_id, name):
        if event_id in self.events:
            self.events[event_id]['name'] = name
            self.write_to_file()
            print(f"Event {event_id} name successfully changed to: {self.events[event_id]['name']}.")
        else:
            print("Event not found.")

    def delete_event(self, event_id):
        if event_id in self.events:
            self.events.pop(event_id)
            self.write_to_file()
            print(f"Event {event_id} successfully removed.")
        else:
            print("Event not found.")

    def add_attendee(self, event_id, attendee):
        if event_id in self.events:
            self.events[event_id]['attendees'].append(attendee)
            self.write_to_file()
            print(f"{attendee} added to event {self.events[event_id]['name']}.")
        else:
            print("Event not found.")

    def list_attendees(self, event_id):
        if event_id in self.events:
            for attendee in self.events[event_id]['attendees']:
                print(attendee)
        else:
            print("Event not found.")

    def web_app(self):
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
                self.list_events()
            elif choice == '2':
                event_id = input("Enter Event ID: ")
                name = input("Enter Event Name: ")
                self.create_event(event_id, name)
            elif choice == '3':
                event_id = input("Enter Event ID To Edit: ")
                name = input("Enter New Event Name: ")
                self.edit_event(event_id, name)
            elif choice == '4':
                event_id = input("Enter Event ID: ")
                self.delete_event(event_id)
            elif choice == '5':
                event_id = input("Enter Event ID: ")
                attendee = input("Enter Attendee Name: ")
                self.add_attendee(event_id, attendee)
            elif choice == '6':
                event_id = input("Enter Event ID: ")
                self.list_attendees(event_id)
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select again.")

event_manager = EventManager()
event_manager.web_app()
