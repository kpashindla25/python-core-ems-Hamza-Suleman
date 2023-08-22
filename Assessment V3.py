#Recreating my event management webapp using more OOP fundamentals and abstraction techniques

import json

#This code recreates the webbapp from the previous versions but uses classes for each event and attendee
#I have also used abstraction to protect the inner workings of each class and their attributes
#This is an example of using the 4 pillars of OOP, mostly throught the use of encapsulation and abstraction

class Attendee:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
#This class encapsulates the attendees, and includes a method get_name for accessing the protected attribute 'name'

class Event:
    def __init__(self, event_id, name):
        self.__event_id = event_id
        self.__name = name
        self.__attendees = []

    def add_attendee(self, attendee):
        self.__attendees.append(attendee)

    def get_event_info(self):
        return f"Event ID: {self.__event_id} | Event Name: {self.__name} | Number of Attendees: {len(self.__attendees)}"
#This class encapsulates an event, it stores the event details and includes a method for adding attendees
#In order to output the details of an event the get_event_info method is used to call the protected attributes

class EventManager:
    def __init__(self):
        try:
            with open('events.json', 'r') as f:
                events_data = json.load(f)
        except FileNotFoundError:
            events_data = {}

        self.__events = {event_id: Event(event_id, event_data['name']) for event_id, event_data in events_data.items()}

    def write_to_file(self):
        events_data = {event_id: {'name': event.__name} for event_id, event in self.__events.items()}
        with open('events.json', 'w') as f:
            json.dump(events_data, f)

    def list_events(self):
        for event_id, event in sorted(self.__events.items()):
            print(event.get_event_info())

    def create_event(self, event_id, name):
        if event_id in self.__events:
            print("Event ID already exists.")
            return

        new_event = Event(event_id, name)
        self.__events[event_id] = new_event
        self.write_to_file()
        print(f"Event '{name}' created.")

    def edit_event(self, event_id, name):
        if event_id in self.__events:
            self.__events[event_id]._Event__name = name
            self.write_to_file()
            print(f"Event {event_id} name successfully changed to: {name}.")
        else:
            print("Event not found.")

    def delete_event(self, event_id):
        if event_id in self.__events:
            del self.__events[event_id]
            self.write_to_file()
            print(f"Event {event_id} successfully removed.")
        else:
            print("Event not found.")

    def add_attendee(self, event_id, attendee_name):
        if event_id in self.__events:
            event = self.__events[event_id]
            attendee = Attendee(attendee_name)
            event.add_attendee(attendee)
            self.write_to_file()
            print(f"{attendee_name} added to event {event._Event__name}.")
        else:
            print("Event not found.")

    def list_attendees(self, event_id):
        if event_id in self.__events:
            event = self.__events[event_id]
            for attendee in event._Event__attendees:
                print(attendee.get_name())
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
                attendee_name = input("Enter Attendee Name: ")
                self.add_attendee(event_id, attendee_name)
            elif choice == '6':
                event_id = input("Enter Event ID: ")
                self.list_attendees(event_id)
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select again.")
#The above class includes all of the webapp functions like before, the only difference is now it uses the new classes-
#to call the protected attributes due to the abstraction we have used

event_manager = EventManager()
event_manager.web_app()

#Overall this program creates the event management system using object oriented programming as much as possible,
#we have used examples of encapsulation and abstraction mainly. In this code we did not get an opportunity to use
#inheritance or polymorphism howevever im sure they can be implemented if I recreated the program again