from transformers import pipeline

def get_model():
    model_name = "TamirG765/finetuning-sentiment-analysis"
    sentiment_analysis = pipeline("sentiment-analysis", model=model_name)
    return sentiment_analysis

def analyze_sentiment(text, model):
    results = model(text)
    for result in results:
        if result['label'] == 'LABEL_1':
            result['label'] = 'Positive 😊'
        elif result['label'] == 'LABEL_0':
            result['label'] = 'Negative 🤬'
    return results

