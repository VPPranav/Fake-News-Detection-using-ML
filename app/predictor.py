import joblib
import os
import requests
import json
import re
from urllib.parse import urlparse
import numpy as np
from bs4 import BeautifulSoup
import random  # For demo purposes only

# Get absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the model and vectorizer using full path
model = joblib.load(os.path.join(BASE_DIR, "models", "logistic_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "models", "tfidf_vectorizer.pkl"))

# Credible news sources database (simplified for demo)
CREDIBLE_SOURCES = {
    "nytimes.com": {"score": 85, "bias": "center-left", "factual": "high"},
    "wsj.com": {"score": 87, "bias": "center-right", "factual": "high"},
    "reuters.com": {"score": 92, "bias": "center", "factual": "very high"},
    "apnews.com": {"score": 93, "bias": "center", "factual": "very high"},
    "bbc.com": {"score": 88, "bias": "center-left", "factual": "high"},
    "theonion.com": {"score": 20, "bias": "satire", "factual": "very low"},
    "breitbart.com": {"score": 45, "bias": "extreme-right", "factual": "mixed"},
    "infowars.com": {"score": 15, "bias": "extreme-right", "factual": "very low"},
}

# Suspicious keywords that might indicate fake news
SUSPICIOUS_KEYWORDS = [
    "shocking truth", "they don't want you to know", "mainstream media won't tell you",
    "secret", "conspiracy", "miracle", "shocking", "you won't believe", 
    "government doesn't want you to know", "doctors hate this", "one weird trick"
]

def predict_news(text):
    """Predict if news is real or fake using the pre-trained model"""
    vectorized_text = vectorizer.transform([text])
    prediction = model.predict(vectorized_text)
    return "FAKE" if prediction[0] == 0 else "REAL"

def get_confidence_score(text):
    """Get confidence score for the prediction"""
    vectorized_text = vectorizer.transform([text])
    
    # Get probability scores
    proba = model.predict_proba(vectorized_text)[0]
    
    # Return confidence percentage and class
    if proba[0] > proba[1]:  # If fake news probability is higher
        return {"score": round(proba[0] * 100, 1), "class": "FAKE"}
    else:
        return {"score": round(proba[1] * 100, 1), "class": "REAL"}

def get_source_credibility(url):
    """Get credibility score for a news source"""
    if not url:
        return None
    
    try:
        # Extract domain from URL
        domain = urlparse(url).netloc
        if domain.startswith('www.'):
            domain = domain[4:]
        
        # Check if domain is in our database
        if domain in CREDIBLE_SOURCES:
            return {
                "domain": domain,
                "score": CREDIBLE_SOURCES[domain]["score"],
                "bias": CREDIBLE_SOURCES[domain]["bias"],
                "factual": CREDIBLE_SOURCES[domain]["factual"]
            }
        
        # If not in database, return a default score
        return {
            "domain": domain,
            "score": 50,  # Neutral score
            "bias": "unknown",
            "factual": "not rated"
        }
    except:
        return None

def fact_check_claim(text):
    """
    Check if the claim has been fact-checked before
    In a real implementation, this would use Google Fact Check API or similar
    """
    # For demo purposes, we'll return mock data
    # In production, you would integrate with a real fact-checking API
    
    # Check if text contains suspicious keywords
    suspicious_count = sum(1 for keyword in SUSPICIOUS_KEYWORDS if keyword.lower() in text.lower())
    
    if suspicious_count > 0:
        return {
            "has_matches": True,
            "matches": [
                {
                    "claim": text[:100] + "...",
                    "rating": "False" if suspicious_count > 2 else "Mostly False",
                    "source": "FactCheck.org",
                    "url": "https://www.factcheck.org/example-check"
                }
            ],
            "suspicious_keywords": [k for k in SUSPICIOUS_KEYWORDS if k.lower() in text.lower()]
        }
    else:
        return {
            "has_matches": False,
            "matches": [],
            "suspicious_keywords": []
        }

def generate_summary(text):
    """
    Generate a summary of the news article
    In a real implementation, this would use a language model like GPT-3.5 or T5
    """
    # For demo purposes, we'll just return the first 200 characters
    # In production, you would use a proper summarization model
    
    summary = text[:200] + "..." if len(text) > 200 else text
    
    # Generate explanation for why we flagged it
    prediction = predict_news(text)
    confidence = get_confidence_score(text)
    
    explanation = ""
    if prediction == "FAKE":
        explanation = "This content was flagged because "
        
        # Check for suspicious keywords
        suspicious_keywords = [k for k in SUSPICIOUS_KEYWORDS if k.lower() in text.lower()]
        if suspicious_keywords:
            explanation += f"it contains suspicious phrases like '{suspicious_keywords[0]}'. "
        
        # Add confidence information
        explanation += f"Our model is {confidence['score']}% confident this is misleading content. "
        
        # Add emotional language check
        sentiment = analyze_sentiment(text)
        if sentiment["emotional_score"] > 70:
            explanation += "The text also uses highly emotional language, which is common in misleading content."
    
    return {
        "summary": summary,
        "explanation": explanation if prediction == "FAKE" else ""
    }

def analyze_sentiment(text):
    """
    Analyze sentiment and bias in the text
    In a real implementation, this would use a sentiment analysis model
    """
    # For demo purposes, we'll use a simple rule-based approach
    # In production, you would use a proper sentiment analysis model
    
    # Check for emotional words (simplified)
    emotional_words = ["outrage", "shocking", "terrible", "amazing", "incredible", 
                      "disaster", "catastrophe", "miracle", "unbelievable"]
    
    emotional_count = sum(1 for word in emotional_words if word.lower() in text.lower())
    emotional_score = min(100, emotional_count * 20)  # Scale up to 100
    
    # Determine political bias (simplified)
    left_words = ["progressive", "liberal", "democrat", "socialism", "equality"]
    right_words = ["conservative", "republican", "tradition", "freedom", "patriot"]
    
    left_count = sum(1 for word in left_words if word.lower() in text.lower())
    right_count = sum(1 for word in right_words if word.lower() in text.lower())
    
    if left_count > right_count + 2:
        bias = "left"
    elif right_count > left_count + 2:
        bias = "right"
    else:
        bias = "neutral"
    
    return {
        "emotional_score": emotional_score,
        "bias": bias,
        "tone": "emotional" if emotional_score > 50 else "neutral"
    }
