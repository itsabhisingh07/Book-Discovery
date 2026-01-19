#  Book Discovery Engine

A machine learning-based web application that helps users discover their next favorite book. The app allows users to search for a book, view detailed insights (ratings, summary, publication info), and receive personalized recommendations for similar books.

##  Features
* **Smart Search:** Supports partial matching and case-insensitive search (e.g., searching "harry potter" finds "Harry Potter and the Sorcerer's Stone").
* **Content-Based Filtering:** Uses Cosine Similarity to recommend books based on genres, authors, and descriptions.
* **Interactive UI:** Clean, responsive interface with a "Featured Books" welcome section.
* **Rich Book Details:** Displays book covers, summaries, publication years, and ratings.
* **One-Click Discovery:** Users can click on recommended books to instantly view their details and get further suggestions.

##  Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn (CountVectorizer, Cosine Similarity), Pandas, NumPy
* **Data Processing:** NLTK / Regex (for text cleaning)

##  Project Structure
```text
Book-Discovery/
│
├── app.py                  # Main Flask application
├── requirements.txt        # List of dependencies
├── static/
│   └── style.css           # Styling for the web app
├── templates/
│   └── index.html          # HTML template
├── book_recommender.ipynb  # Jupyter Notebook for data cleaning & model training
├── .gitignore              # Specifies files to ignore (like large .pkl files)
└── README.md               # Project documentation
```