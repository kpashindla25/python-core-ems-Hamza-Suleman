#Recreating my event management webapp using more OOP fundamentals and abstraction techniques

import json
#im using a json file for this task as they are known to be the best for file handling
#especially when using dicionaries as i plan to use

#This code recreates the webbapp from the previous versions but uses classes for each event and attendee
#I have also used abstraction to protect the inner workings of each class and their attributes
#This is an example of using the 4 pillars of OOP, mostly throught the use of encapsulation and abstraction

class Attendee:
    def __init__(self, name):
        self.__name = name

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self,new_name):
        self.__name = new_name
#This class encapsulates the attendees, and includes a method get_name for accessing the protected attribute 'name'

class Event:
    def __init__(self, event_id, name, date, location):
        self.__event_id = event_id
        self.__name = name
        self.__date = date
        self.__location = location
        self.__attendees = []

    @property
    def event_id(self):
        return self.__event_id

    @event_id.setter
    def event_id(self, new_id):
        self.__event_id = new_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date):
        self.__date = new_date

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, new_location):
        self.__location = new_location

    def add_attendee(self, attendee):
        self.__attendees.append(attendee)

    @property
    def attendees(self):
        return self.__attendees

    @attendees.setter
    def attendees(self,new_attendee):
        self.__attendees = new_attendee

    def get_event_info(self):
        return (f"Event ID: {self.__event_id}\n"
                f"Event Name: {self.__name}\n"
                f"Event Date: {self.__date}\n"
                f"Event Location {self.__location}\n"
                f"Number of Attendees: {len(self.__attendees)}\n"
                f"------------------------------------------")

    def set_name(self, name):
        self.__name = name

    def __del__(self):
        pass  #Optionally handle cleanup actions here, such as saving data, this solved some issues with duplicate data
#This class encapsulates an event, it stores the event details and includes a method for adding attendees
#In order to output the details of an event the get_event_info method is used to call the protected attributes
#The set_name method is used to set the abstracted name for the event without cuasing name mangaling issues

class EventNotFoundException(Exception):
    def __str__(self):
        return f"Event was not found. Please check the event ID and try again."
#This class is a custom exception, it will be used in the webapp to raise a specific
#exception when a user tries to query an event that doesnt exist
#this is useful as we can use this exception to handle this type of error separately from
#other issues that can arise
#The exception prints an error statement when the class is called

class EventManager:
    def __init__(self):
        try:
            with open('events.json', 'r') as f:
                events_data = json.load(f)
            print("Data Loaded Successfully!")
        except (FileNotFoundError, json.JSONDecodeError):
            events_data = {}
            print("Creating Database...")
        #This is exception handling, it makes sure the program doesnt stop if the file isnt already there
        self.__events = {}
        for event_id, event_data in events_data.items():
            event = Event(event_id, event_data['name'], event_data['date'], event_data['location'])
            for attendee_name in event_data.get('attendees', []):
                event.add_attendee(Attendee(attendee_name))
            self.__events[event_id] = event

    def write_to_file(self):
        events_data = {
            event_id: {
                'name': event.name,
                'date': event.date,
                'location': event.location,
                'attendees': [attendee.get_name for attendee in event.attendees]
            }
            for event_id, event in self.__events.items()
        }
        #This adds the event information and attendees information to the dictionary and writes it to the file
        #dump() is how python converts text into json format for saving
        with open('events.json', 'w') as f:
            json.dump(events_data, f)
        #This method deals with file handling, it writes to the file from the working program memory

    def list_events(self):
        if len(self.__events.items()) > 0:
            for event_id, event in sorted(self.__events.items()):
                print(event.get_event_info())
        else:
            print("There are no current events! Please press 2 to create a new event.")
    #this function prints out all of the events saved in the file
    #it uses the dictionary to print the event id and the name of the event
    #the sorted command ensures the events are sorted by id number
    #the function uses the method in the event class to return the event info as it is protected due to abstraction

    def create_event(self, event_id, name, date, location):
        if event_id in self.__events:
            print("Event ID already exists.")
            return

        new_event = Event(event_id, name, date, location)
        self.__events[event_id] = new_event
        self.write_to_file()
        print(f"Event '{name}' created.")
    #this will create an event by creating a new key in the dictionary in the json file and then write it to file
    #the method first checks if the event already exists, and if it does it does not add the duplicate

    def edit_event_name(self, event_id, name):
        if event_id in self.__events:
            self.__events[event_id]._Event__name = name
            self.write_to_file()
            print(f"Event {event_id} name successfully changed to: {name}.")
        else:
            raise EventNotFoundException
    #this method will change the name of an event that the user specifies and will write it to the file
    #custom exception handling is used here instead of a simple print statement, this can help identify specific errors

    def edit_event_date(self, event_id, date):
        if event_id in self.__events:
            self.__events[event_id]._Event__date = date
            self.write_to_file()
            print(f"Event {event_id} date successfully changed to: {date}.")
        else:
            raise EventNotFoundException

    def edit_event_location(self, event_id, location):
        if event_id in self.__events:
            self.__events[event_id]._Event__location = location
            self.write_to_file()
            print(f"Event {event_id} location successfully changed to: {location}.")
        else:
            raise EventNotFoundException

    def delete_event(self, event_id):
        if event_id in self.__events:
            del self.__events[event_id]
            self.write_to_file()
            print(f"Event {event_id} successfully removed.")
        else:
            raise EventNotFoundException
    #this function deletes an event that the user specifies and updates the file, again with custom exception handling

    def add_attendee(self, event_id, attendee_name):
        if event_id in self.__events:
            event = self.__events[event_id]
            attendee = Attendee(attendee_name)
            event.add_attendee(attendee)
            self.write_to_file()
            print(f"{attendee_name} added to event {event._Event__name}.")
        else:
            raise EventNotFoundException
    #this function can add an attendee to a specific event by the id, it also ensures that the attendees get written
    #to the file along with their specific events

    def list_attendees(self, event_id):
        if event_id in self.__events:
            event = self.__events[event_id]
            for attendee in event._Event__attendees:
                print(attendee.get_name)
        else:
            raise EventNotFoundException
    #this function will list all of the attendees for a specific event using the method included in the attendee class
    #to access protected attributes due to the abstraction techniques employed

    #below is a method that creates the entire front end of the webapp, it alows the user to navigate various functions
    #and includes custom error handling to deal with exceptions as well as writing all the user inputs
    #and changes to the file, the webapp includes all the functions outlines in the assessment brief
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
                date = input("Enter Event Date: (dd/mm/yyyy) ")
                location = input("Enter Event Location: ")
                self.create_event(event_id, name, date, location)
            elif choice == '3':
                event_id = input("Enter Event ID To Edit: ")
                print(f"\nWhat would you like to edit for Event {event_id}?")
                print("1. Event Name")
                print("2. Event Date")
                print("3. Event Location")
                edit_choice = input("Select an option: ")
                if edit_choice == '1':
                    try:
                        name = input("Enter New Event Name: ")
                        self.edit_event_name(event_id, name)
                    except EventNotFoundException as e:
                        print(e)
                elif edit_choice == '2':
                    try:
                        date = input("Enter New Event Date: ")
                        self.edit_event_date(event_id, date)
                    except EventNotFoundException as e:
                        print(e)
                elif edit_choice == '3':
                    try:
                        location = input("Enter New Event Location: ")
                        self.edit_event_location(event_id, location)
                    except EventNotFoundException as e:
                        print(e)
            elif choice == '4':
                try:
                    event_id = input("Enter Event ID: ")
                    self.delete_event(event_id)
                except EventNotFoundException as e:
                    print(e)
            elif choice == '5':
                try:
                    event_id = input("Enter Event ID: ")
                    attendee_name = input("Enter Attendee Name: ")
                    self.add_attendee(event_id, attendee_name)
                except EventNotFoundException as e:
                    print(e)
            elif choice == '6':
                try:
                    event_id = input("Enter Event ID: ")
                    self.list_attendees(event_id)
                except EventNotFoundException as e:
                    print(e)
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select again.")
#The above class includes all of the webapp functions like before, the only difference is now it uses the new classes-
#to call the protected attributes due to the abstraction we have used
#Each option what requires a user input now includes custom exception handling to check if the input is acceptable

event_manager = EventManager()
event_manager.web_app()
#to initialise the webapp we first instantiate the EventManager() class, and then run the web_app() method within it

#Overall this program creates the event management system using object oriented programming as much as possible,
#we have used examples of encapsulation and abstraction mainly. In this code we did not get an opportunity to use
#inheritance or polymorphism howevever im sure they can be implemented if I recreated the program again.