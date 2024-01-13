######

#Py Header details


# Requirements - Requires pywin32 be installed
#   Open a command prompt or terminal and run the following command to install the pywin32 package: pip install pywin32
#   After install run an update for the latest version using the following command: python.exe -m pip install --upgrade pip
#   if necessary add the install location to PATH environment variable in Windows
#   if necessary restart your IDE

#####

###### Code ######


# Imports the various windows event logs.  Some logs may require Admin access to read.  Requires pywin32 be installed
import win32evtlog
import win32evtlogutil
import win32security
import win32con
import datetime

def get_recent_events(log_name, num_events=10):
    # Open the event log
    hand = win32evtlog.OpenEventLog(None, log_name)

    # Get the number of events in the log
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    # Read recent events
    events = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)

    # Fetch the most recent events
    recent_events = []
    for i in range(min(num_events, total)):
        event = win32evtlogutil.SafeReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ, 0)
        recent_events.append(event)

    # Close the event log
    win32evtlog.CloseEventLog(hand)
    win32evtlogutil.safe

    return recent_events

def print_event_details(event):
    event_time = event.TimeGenerated.Format()
    event_type = win32evtlogutil.SafeGetEventMessage(event, event.Sid)

    print(f"Event Time: {event_time}")
    print(f"Event Type: {event_type}")
    print(f"Event Category: {event.EventCategory}")
    print(f"Event ID: {event.EventID}")
    print(f"Event Source: {event.SourceName}")
    print(f"Event Description: {event.StringInserts}")
    print("=" * 50)

def main():
    log_name = "System"
    num_events_to_fetch = 5

    recent_events = get_recent_events(log_name, num_events_to_fetch)

    print(f"Recent {num_events_to_fetch} events from {log_name} log:")
    print("=" * 50)

    for event in recent_events:
        print_event_details(event)

if __name__ == "__main__":
    main()




