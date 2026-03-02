# 5 School Notification System (Polymorphism with Methods)
# Base class
class Notification:
    def send_message(self):
        print("Sending notification")


# Subclass EmailNotification
class EmailNotification(Notification):
    def send_message(self):
        print("Sending notification via Email")


# Subclass SMSNotification
class SMSNotification(Notification):
    def send_message(self):
        print("Sending notification via SMS")


# Subclass AppNotification
class AppNotification(Notification):
    def send_message(self):
        print("Sending notification via Mobile App")


# Create objects
email = EmailNotification()
sms = SMSNotification()
app = AppNotification()

# Polymorphism demonstration
notifications = [email, sms, app]

for n in notifications:
    n.send_message()
