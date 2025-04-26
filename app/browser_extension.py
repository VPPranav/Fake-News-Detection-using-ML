"""
Browser Extension API Module

This module provides the API endpoints for the browser extension to check news content.
In a real implementation, this would be a separate extension for Chrome/Firefox.
"""

from flask import Blueprint, request, jsonify
from predictor import predict_news, get_confidence_score, get_source_credibility

# Create blueprint for browser extension API
browser_ext = Blueprint('browser_extension', __name__)

@browser_ext.route('/api/check-url', methods=['POST'])
def check_url():
    """API endpoint for the browser extension to check a URL"""
    data = request.json
    
    if not data or 'url' not in data or 'content' not in data:
        return jsonify({"error": "Missing URL or content"}), 400
    
    url = data['url']
    content = data['content']
    
    # Get basic prediction
    prediction = predict_news(content)
    
    # Get confidence score
    confidence = get_confidence_score(content)
    
    # Get source credibility
    source_credibility = get_source_credibility(url)
    
    return jsonify({
        "prediction": prediction,
        "confidence": confidence,
        "source_credibility": source_credibility,
        "extension_version": "1.0.0"
    })

@browser_ext.route('/api/extension-info', methods=['GET'])
def extension_info():
    """API endpoint to get information about the browser extension"""
    return jsonify({
        "name": "FakeNewsGuard Browser Extension",
        "version": "1.0.0",
        "description": "Check news articles for potential misinformation as you browse.",
        "supported_browsers": ["Chrome", "Firefox", "Edge"],
        "download_links": {
            "chrome": "#",
            "firefox": "#",
            "edge": "#"
        }
    })
