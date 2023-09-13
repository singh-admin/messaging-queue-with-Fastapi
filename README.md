# messaging-queue-with-Fastapi
using fastapi framework and using inbuild method of fastapi able to messaging ( using mailtrap.com service) 

# Mailtrap SMTP Configuration

This project uses Mailtrap for SMTP email testing and development purposes. Mailtrap allows you to test email functionality without sending actual emails to recipients. Follow the steps below to configure Mailtrap SMTP for your project:

## Step 1: Sign Up for Mailtrap

1. Go to [Mailtrap](https://mailtrap.io/) and sign up for a free or paid account.

## Step 2: Create an Inbox

1. After signing in, create a new inbox in Mailtrap.

## Step 3: Get SMTP Credentials

1. In your Mailtrap inbox, you'll find SMTP settings. These settings include the SMTP server, port, username, and password.

## Step 4: Configure Your Application

In your project's configuration file (e.g., `config.py`), or environment variables, set the following SMTP parameters with the values from your Mailtrap inbox:

```python
MAILTRAP_HOST = 'your-smtp-server.mailtrap.io'
MAILTRAP_PORT = 2525
MAILTRAP_USERNAME = 'your-username'
MAILTRAP_PASSWORD = 'your-password'

