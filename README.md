# Cartoon Alert System

## Overview

The Cartoon Alert System is a web application that monitors Patrick Corrigan's website for new cartoon updates and sends alerts to subscribed users via SMS. This project uses Python for the backend, with a combination of Flask for the web interface, Redis for data storage, and the Twilio API for sending SMS notifications. The application also includes a cron job that runs daily to check for new cartoons and notify users. Additionally, the system analyzes the political cartoons using GPT-4o, providing a brief analysis along with the notification.

## Features

- **User Subscription**: Users can subscribe to receive SMS notifications for new cartoon updates by providing their phone numbers.
- **Daily Check**: A cron job runs daily to check for new cartoon updates on the specified website.
- **SMS Notifications**: Users receive an SMS notification whenever a new cartoon is detected.
- **Cartoon Analysis**: The system uses GPT-4o to provide a short analysis of the political cartoons.
- **Data Storage**: User phone numbers and other data are stored securely in Redis.

## Technologies Used

- **Python**: Backend language.
- **Flask**: Web framework for the application.
- **Redis**: In-memory data structure store for storing user data.
- **Twilio API**: For sending SMS notifications.
- **OpenAI API**: For analyzing the cartoons using GPT-4o.
- **GitHub Actions**: For running the daily cron job.
- **BeautifulSoup**: For web scraping to detect new cartoons.
- **Vercel**: For deployment.

## Setup and Installation

### Prerequisites

- Python 3.x
- Redis server
- Twilio account
- OpenAI account

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/JodhbirS/CartoonAlert.git
   cd cartoon-alert
   ```

2. **Create a virtual environment and activate it**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**: Create a `.env` file in the root directory and add your configuration variables:

   ```plaintext
   FLASK_SECRET_KEY=your_flask_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   REDIS_HOST=your_redis_host
   REDIS_PORT=your_redis_port
   REDIS_PASSWORD=your_redis_password
   CRON_SECRET=your_cron_secret
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_ORG_ID=your_openai_org_id
   ```

5. **Run Redis server**: Ensure that your Redis server is running. You can start it using:

   ```bash
   redis-server
   ```

6. **Run the application**:

   ```bash
   python app.py
   ```

## Usage

1. **Subscribe to Notifications**:

   - Visit the web interface.
   - Enter your phone number and submit the form to subscribe to notifications.

2. **Daily Check for New Cartoons**:
   - The GitHub Actions workflow is set up to run daily and trigger the `cron.py` script.
   - The script checks for new cartoon updates, analyzes them, and sends notifications to subscribed users.

## Deployment

### Deploying on Vercel

1. **Configure `vercel.json`**:

   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

2. **Deploy**:
   - Commit your changes and push to GitHub.
   - Vercel will automatically build and deploy your application.

### GitHub Actions for Cron Job

1. **Create Workflow File**: Add a `.github/workflows/cron-job.yml` file with the following content:

   ```yaml
   name: Run Cron Job

   on:
     schedule:
       - cron: "0 10 * * *"
     workflow_dispatch:

   jobs:
     run-cron:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2

         - name: Set up Python
           uses: actions/setup-python@v2
           with:
             python-version: "3.12"

         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install -r requirements.txt

         - name: Run Cron Job
           env:
             TWILIO_ACCOUNT_SID: ${{ secrets.TWILIO_ACCOUNT_SID }}
             TWILIO_AUTH_TOKEN: ${{ secrets.TWILIO_AUTH_TOKEN }}
             REDIS_PORT: ${{ secrets.REDIS_PORT }}
             REDIS_PASSWORD: ${{ secrets.REDIS_PASSWORD }}
             REDIS_HOST: ${{ secrets.REDIS_HOST }}
             CRON_SECRET: ${{ secrets.CRON_SECRET }}
             OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
             OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
           run: python cron.py
   ```

2. **Add Secrets**: Go to your GitHub repository settings and add the required secrets.
