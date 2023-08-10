from flask import Flask,request,jsonify,render_template  
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

@app.route("/")
def home():
    return "<h1>Hello, world</h1>"

@app.route("/recommendation",methods = ['post'])
def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
    a,b,c,d,e = recommend_movie[0],recommend_movie[1],recommend_movie[2],recommend_movie[3],recommend_movie[4]    
    return a,b,c,d,e 




if __name__ == "__main__":
    app.run(debug=True)