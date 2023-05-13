from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

API_KEY = '42ca7dade0b74dfda50bde169236d7f6'
ENDPOINT = 'https://text-analytics-assignment.cognitiveservices.azure.com/'

def client():
    # Authenticate the client
    client = TextAnalyticsClient(
        endpoint=ENDPOINT,
        credential=AzureKeyCredential(API_KEY))
    return client
