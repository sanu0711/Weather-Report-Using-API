# Weather SMS Notifier

A Python script that fetches current weather information using the OpenWeather API and sends it as an SMS using Twilio.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project is a Python script that allows you to fetch current weather information for a specific location using the OpenWeather API and send it as an SMS using Twilio. It can be used to receive weather updates on your phone via SMS, making it convenient for quick weather checks.

## Features

- Fetches current weather data (description and temperature) from OpenWeather API.
- Sends weather data as an SMS to a specified phone number using Twilio.
- Easy-to-use and customizable for different locations.

## Prerequisites

Before you can use this project, ensure you have the following prerequisites:

- OpenWeather API Key: Sign up at [OpenWeather](https://openweathermap.org/api) to obtain an API key.
- Twilio Account SID and Auth Token: Sign up at [Twilio](https://www.twilio.com/) to obtain your credentials.
- Python 3.x installed on your system.

## Getting Started

Follow these steps to get started with the Weather SMS Notifier:

1. Install the required Python packages:

   ```bash
   pip install requests twilio

