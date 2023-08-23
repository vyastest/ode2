import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import  os

# Load data from CSV file
filepath = r"C:\Users\Malleswari\oda_spa\web_data.csv"
data = pd.read_csv(filepath)

# Perform sentiment analysis using TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment == 0:
        return 'Neutral'
    else:
        return 'Negative'

data['Sentiment'] = data['Review'].apply(get_sentiment)

# Count the occurrences of each sentiment label
sentiment_counts = data['Sentiment'].value_counts()

# Streamlit app
st.title('Sentiment Analysis App')

# Display sentiment distribution using a bar chart
st.subheader('Sentiment Distribution')
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, ax=ax)
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
st.pyplot(fig)