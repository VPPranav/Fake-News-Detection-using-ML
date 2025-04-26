---
# 📰 FakeNewsGuard — AI-Powered Fake News Detection

FakeNewsGuard is an AI-powered web application designed to detect fake news content. Users can input a news article or social media post to receive real-time predictions on whether the content is real or fake. The application also evaluates source credibility, analyzes sentiment and bias, checks for suspicious keywords, and provides summarized explanations.

# Dataset link : https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets

---

## 🔍 Features

- 🧠 **AI-Powered Detection**: Utilizes a Logistic Regression model trained on TF-IDF features.
- ✅ **Prediction Confidence**: Shows confidence percentage for each prediction.
- 🔗 **Source Credibility Analysis**: Checks the domain’s credibility and political alignment.
- 📊 **Sentiment & Bias Analyzer**: Identifies emotional tone and political leanings.
- 🧾 **Fact Check Matching**: Flags common fake phrases and links to verified fact-checks.
- 📄 **Auto Summary & Explanation**: Generates concise summaries and highlights problematic content.
- 💬 **Social Media Post Checker**: Dedicated form to analyze social media posts.
- 🎓 **Educational Resources**: Includes learning materials on fake news and digital literacy.

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (custom UI), JavaScript (Chart.js)
- **Machine Learning**: Scikit-learn (Logistic Regression, TF-IDF Vectorizer)
- **Utilities**: Joblib, BeautifulSoup, Requests

---

## 📁 Project Structure

```
FAKE_NEWS_DETECTION/
├── app/
│   ├── static/
│   │   └── uploads/
│   ├── __init__.py
│   ├── app.py
│   ├── browser_extension.py
│   └── predictor.py
│
├── dataset/
│   ├── Fake.csv
│   └── True.csv
│
├── models/
│   ├── logistic_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebook/
│   └── fake_news_detection.ipynb
│
├── templates/
│   ├── about.html
│   ├── education.html
│   ├── index.html
│   └── social_check.html
│
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fake-news-guard.git
   cd fake-news-guard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train or load the model**:
   - Train using `notebook/fake_news_detection.ipynb`, **or**
   - Ensure pre-trained `logistic_model.pkl` and `tfidf_vectorizer.pkl` are in the `models/` directory.

4. **Run the app**:
   ```bash
   python app/app.py
   ```

5. **View in browser**:
   ```
   http://localhost:5000
   ```

---

## ⚠️ Disclaimer

> This application is trained on historical news data (2015–2017) and is intended **solely for demonstration and educational purposes**. It should not be relied upon for official fact-checking or journalistic use.

---

## 🙋‍♂️ Author

**Pranav V P**

- 🔗 [LinkedIn](https://www.linkedin.com/in/pranav-vp-3636b825a/)
- 🐦 [Twitter / X](https://x.com/Pranav62196016)
- 📸 [Instagram](https://www.instagram.com/pranav_vp_07)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
```

---

Let me know if you’d like a badge section (e.g., GitHub stars, forks, license) or demo screenshots added!
