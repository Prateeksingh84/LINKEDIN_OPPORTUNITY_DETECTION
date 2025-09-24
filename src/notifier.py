# notifier_demo.py

import os
import csv
import requests
import smtplib
from email.mime.text import MIMEText

def notify_slack(webhook_url: str, message: str):
    try:
        resp = requests.post(webhook_url, json={"text": message})
        resp.raise_for_status()
        print(f"Slack notification sent: {message}")
    except Exception as e:
        print(f"Slack notify failed: {e}")

def notify_email(smtp_host, smtp_port, smtp_user, smtp_pass, from_addr, to_addr, subject, body):
    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    try:
        server = smtplib.SMTP(smtp_host, int(smtp_port))
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print(f"Email sent to {to_addr} with subject: {subject}")
    except Exception as e:
        print(f"Email send failed: {e}")

if __name__ == "__main__":
    # Slack notification (you need a valid webhook for this to actually work)
    slack_webhook = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    slack_message = "Test Slack notification"
    print("Calling notify_slack …")
    notify_slack(slack_webhook, slack_message)

    # Email notification (you need valid SMTP credentials)
    smtp_host = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "your_email@gmail.com"
    smtp_pass = "your_password"
    from_addr = "your_email@gmail.com"
    to_addr = "recipient_email@example.com"
    subject = "Test Email"
    body = "This is a test email sent from Python."
    print("Calling notify_email …")
    notify_email(smtp_host, smtp_port, smtp_user, smtp_pass, from_addr, to_addr, subject, body)
