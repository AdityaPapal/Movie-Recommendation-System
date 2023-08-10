from flask import Flask, render_template, request
import pickle
import requests

app = Flask(__name__,template_folder='template')

def fetch_poster(movie_id):
    # Your fetch_poster function code here
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

@app.route('/demo')
def index():
    movies_list = pickle.load(open("movies_list.pkl", 'rb'))
    return render_template('demo.html', movies_list = movies_list['title'].values[1])

# @app.route("/index")
# def index2():
#     movies_list = pickle.load(open("movies_list.pkl", 'rb'))
#     movies_list = movies_list['title'].values[1]

#     return render_template('index.html',suggestions=suggestions,movie_type=types[5:],movieid=mid,movie_overview=overview,movie_names=names,movie_date=dates,movie_ratings=ratings,search_name=m_name)

@app.route('/recommend', methods=['POST'])
def recommend():
    movies = pickle.load(open("movies_list.pkl", 'rb'))
    similarity = pickle.load(open("similarity.pkl", 'rb'))

    index = movies[movies['title'] == movies].index[0]
    distance = sorted(enumerate(similarity[index]), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]]['id']
        recommend_movie.append(movies.iloc[i[0]]['title'])
        recommend_poster.append(fetch_poster(movie_id))
    
    
if __name__ == '__main__':
    app.run(debug=True)
