# process a list of Event objects using their attributes to 
# generate a report that lists all users currently logged in to the machines
# machine name, date and time, and logins/logouts

# keep track of logins and logouts and their times, create a list of current logins, remove on 
# logout. attach to machine names
# MUST be kept in chronological order
# sort() vs sorted() # sort modifies list, sorted creates new list
# sort/sorted take parameters! default is alphabetical

# def get_event_date?

# machine_users # add and remove on login/logout
# dictionary of sets is best. i hate dictionaries
# name of machine is key, current users are values
# add new entry if machine is new, update entry if not
# seperate function for processing/printing. easier to fix/change/reuse functions


def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines:
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
        print("{}: {}".format(machine, user_list))

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event("2020-01-21 12:45:56", "login", "myworkstation.local", "jordan"),
    Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
    Event("2020-01-21 18:53:21", "login", "webserver.local", "lane"),
    Event("2020-01-22 10:25:34", "logout", "myworkstation.local", "jordan"),
    Event("2020-01-21 18:20:01", "login", "webserver.local", "jordan"),
    Event("2020-01-23 11:24:35", "logout", "myworkstation.local", "chris"),
]

users = current_users(events)
generate_report(users)