# Microsoft-Azure-Sentiment-Analysis

This is a Python script that performs sentiment analysis on a given text using the Microsoft Azure Sentiment Analysis API. The script uses the azure-ai-textanalytics library to interact with the API.

## Prerequisites
- Python 3.6 or later
- azure-ai-textanalytics library
- A Microsoft Azure account with an active subscription

## Installation
1. Clone this repository to your local machine
2. Install the azure-ai-textanalytics library by running the following command in your terminal:
```
pip install azure-ai-textanalytics
```
3. Create a Microsoft Azure account if you do not already have one, and subscribe to the Text Analytics API service
4. Retrieve your Text Analytics API key and endpoint URL from your Azure account dashboard

## Usage
1. Open the `azure_sentiment_analysis.py` file
2. Replace the `YOUR_API_KEY` and `YOUR_ENDPOINT` placeholders in the script with your API key and endpoint URL respectively
3. Replace the `YOUR_TEXT_HERE` placeholder with the text you want to perform sentiment analysis on
4. Run the script in your terminal using the following command:
```
python azure_sentiment_analysis.py
```
5. The sentiment analysis results will be displayed in the terminal
