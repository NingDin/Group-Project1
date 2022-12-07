from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
data = ["I love you","I am okay", "I hate you","Wow: pending home sales now down by nearly 37% year/year, which is worst annual decline on record (going back to 2002)" ]
print(sentiment_pipeline(data))
