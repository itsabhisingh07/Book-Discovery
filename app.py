from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


popular_df = pickle.load(open('books.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

@app.route('/')
@app.route('/')
def index():
   
    random_selection = popular_df.sample(n=8)
    
    default_books = []
    for _, row in random_selection.iterrows():
        item = [
            row['title'], 
            row['author'], 
            row['image'], 
            row['average_rating']
        ]
        default_books.append(item)
        

    return render_template('index.html', default_books=default_books)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    user_input = ""
    
    
    if request.method == 'POST':
        user_input = request.form.get('user_input')
    else:
        user_input = request.args.get('book_name')

    if not user_input:
        return render_template('index.html', error="Please enter a book name.")

    
    user_input = user_input.lower().strip() 
    
   
    found_title = None
    for title in popular_df['title']:
        if user_input in title.lower():
            found_title = title
            break 
    
    if found_title:
       
        idx = popular_df[popular_df['title'] == found_title].index[0]
        
     
        distances = similarity[idx]
        similar_books = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:5]
        
     
        book_details = {
            'title': popular_df.iloc[idx].title,
            'author': popular_df.iloc[idx].author,
            'image': popular_df.iloc[idx].image,
            'rating': popular_df.iloc[idx].average_rating,
            'year': popular_df.iloc[idx].year,
            'desc': popular_df.iloc[idx].description,
            'votes': popular_df.iloc[idx].get('num_ratings', 'N/A')
        }

        data = []
        for i in similar_books:
            item = []
            temp_df = popular_df.iloc[i[0]]
            item.extend([temp_df.title, temp_df.author, temp_df.image, temp_df.average_rating])
            data.append(item)

        return render_template('index.html', book=book_details, similar_books=data, found=True)

    else:
        return render_template('index.html', error="Book not found! Try typing the full name.", found=False)
    

if __name__ == '__main__':
    app.run(debug=True)