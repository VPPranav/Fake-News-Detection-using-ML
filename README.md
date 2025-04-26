Based on your uploaded files, here's a `README.md` that documents your **Fake News Detection Web Application** project:

---

```markdown
# 📰 FakeNewsGuard — AI-Powered Fake News Detection

FakeNewsGuard is an AI-powered web application designed to detect fake news content. It allows users to input a news article or social media post and get real-time predictions on whether the content is real or fake. The app also evaluates source credibility, performs sentiment and bias analysis, checks for suspicious keywords, and provides a summarized explanation.

## 🔍 Features

- 🧠 **AI-Powered Detection**: Uses a Logistic Regression model trained on TF-IDF features.
- ✅ **Prediction Confidence**: Displays confidence percentage for the prediction.
- 🔗 **Source Credibility Analysis**: Checks domain credibility and political bias.
- 📊 **Sentiment & Bias Analyzer**: Evaluates emotional language and political leanings.
- 🧾 **Fact Check Matching**: Flags known fake phrases and links to fact-checking sources.
- 📄 **Auto Summary & Explanation**: Generates a brief summary and flags issues.
- 💬 **Social Media Post Checker**: A separate form for analyzing tweets/posts.
- 🎓 **Educational Resources**: Provides learning materials on fake news and misinformation.

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Custom modern UI), JavaScript (Chart.js)
- **ML**: Scikit-learn (Logistic Regression, TF-IDF Vectorizer)
- **Others**: Joblib, BeautifulSoup, Requests

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

3. **Train or load model**:
   - Train the model using `fake_news_detection.ipynb`, or
   - Ensure `logistic_model.pkl` and `tfidf_vectorizer.pkl` are in the `models/` folder.

4. **Run the app**:
   ```bash
   python app.py
   ```

5. **Open in browser**:
   ```
   http://localhost:5000
   ```

## ⚠️ Disclaimer

> This tool is trained on data from 2015–2017 and is for **demonstration and educational purposes** only. It is not suitable for use as a production-grade fact-checking tool.

## 🙋‍♂️ Author

**Pranav V P**

- [LinkedIn](https://www.linkedin.com/in/pranav-vp-3636b825a/)
- [Twitter/X](https://x.com/Pranav62196016)
- [Instagram](https://www.instagram.com/pranav_vp_07)

---

## 📄 License

This project is licensed under the MIT License.
```

---
