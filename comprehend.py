import boto3

def analyze_sentiment(text):
    comprehend = boto3.client("comprehend", region_name="ca-central-1")
    response = comprehend.detect_sentiment(
        Text=text,
        LanguageCode="en"
    )
    return response["Sentiment"]
