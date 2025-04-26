from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from predictor import predict_news, get_source_credibility, fact_check_claim, generate_summary
from predictor import analyze_sentiment, get_confidence_score
import requests
from werkzeug.utils import secure_filename

# Create Flask app
app = Flask(__name__, static_folder="static", template_folder="C:/Users/www12/OneDrive/Documents/Projects/fake_news_detection_webapp/templates")
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # not required for this project
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_data = None
    if request.method == "POST":
        news = request.form["news"]
        source_url = request.form.get("source_url", "")
        
        # Get basic prediction
        prediction = predict_news(news)
        
        # Get confidence score
        confidence = get_confidence_score(news)
        
        # Get source credibility if URL provided
        source_credibility = get_source_credibility(source_url) if source_url else None
        
        # Get fact check results
        fact_check_results = fact_check_claim(news)
        
        # Generate summary
        summary = generate_summary(news)
        
        # Analyze sentiment and bias
        sentiment_data = analyze_sentiment(news)
        
        prediction_data = {
            "prediction": prediction,
            "confidence": confidence,
            "source_credibility": source_credibility,
            "fact_check_results": fact_check_results,
            "summary": summary,
            "sentiment": sentiment_data,
            "news_text": news,
            "source_url": source_url
        }
        
    return render_template("index.html", prediction_data=prediction_data)

@app.route("/image-search", methods=["POST"])
def image_search():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No image selected"}), 400
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Perform reverse image search
        results = reverse_image_search(filepath)
        
        return jsonify({"results": results})

@app.route("/social-check", methods=["GET", "POST"])
def social_check():
    results = None
    if request.method == "POST":
        social_post = request.form.get("social_post", "")
        if social_post:
            # Basic prediction
            prediction = predict_news(social_post)
            
            # Get confidence score
            confidence = get_confidence_score(social_post)
            
            # Analyze sentiment and bias
            sentiment_data = analyze_sentiment(social_post)
            
            results = {
                "prediction": prediction,
                "confidence": confidence,
                "sentiment": sentiment_data,
                "post_text": social_post
            }
    
    return render_template("social_check.html", results=results)

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
