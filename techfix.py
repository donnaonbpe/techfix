import time
import datetime
import winsound
import threading
from typing import List, Dict

class Alert:
    def __init__(self, name: str, alert_time: datetime.datetime, message: str):
        self.name = name
        self.alert_time = alert_time
        self.message = message

    def alert(self):
        print(f"Alert: {self.name}\nTime: {self.alert_time}\nMessage: {self.message}")
        winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1 second

class TechFix:
    def __init__(self):
        self.alerts: List[Alert] = []

    def add_alert(self, name: str, alert_time: datetime.datetime, message: str):
        alert = Alert(name, alert_time, message)
        self.alerts.append(alert)
        print(f"Scheduled: {name} at {alert_time}")

    def remove_alert(self, name: str):
        self.alerts = [alert for alert in self.alerts if alert.name != name]
        print(f"Removed alert: {name}")

    def start(self):
        def check_alerts():
            while True:
                now = datetime.datetime.now()
                for alert in self.alerts:
                    if now >= alert.alert_time:
                        alert.alert()
                        self.remove_alert(alert.name)
                time.sleep(60)  # Check every minute

        alert_thread = threading.Thread(target=check_alerts)
        alert_thread.daemon = True
        alert_thread.start()

if __name__ == "__main__":
    techfix = TechFix()
    # Example: Adding an alert for 2 minutes from now
    techfix.add_alert(
        name="Test Alert",
        alert_time=datetime.datetime.now() + datetime.timedelta(minutes=2),
        message="This is a test alert"
    )
    techfix.start()
    
    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting TechFix")