import smtplib
import schedule
import time

def send_email(subject, body, recipients, sender_email, sender_password):
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP_SSL('smtp.your_email_provider.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipients, message)
        print("Email sent successfully.")

def compose_email():
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")
    recipients = input("Enter recipient email addresses (separated by comma): ").split(',')
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    schedule_time = input("Enter scheduled time (format: HH:MM): ")

    schedule.every().day.at(schedule_time).do(send_email, subject, body, recipients, sender_email, sender_password)

    print(f"Email scheduled to be sent at {schedule_time}")

def main():
    print("Welcome to the Email Scheduler!")
    while True:
        print("\n1. Compose Email\n2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            compose_email()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
