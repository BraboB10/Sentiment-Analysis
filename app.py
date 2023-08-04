from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        sentiment, word_sentiments = analyze_sentiment(text)
        return render_template('index.html', text=text, sentiment=sentiment, word_sentiments=word_sentiments)

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    word_sentiments = []
    for sentence in blob.sentences:
        sentence_blob = TextBlob(str(sentence))
        sentence_sentiment = sentence_blob.sentiment
        word_sentiments.append((sentence, sentence_sentiment.polarity, sentence_sentiment.subjectivity))

    if sentiment_score > 0:
        sentiment = 'Positive'
    elif sentiment_score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, word_sentiments

if __name__ == '__main__':
    app.run(debug=True)
