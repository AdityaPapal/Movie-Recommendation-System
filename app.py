from flask import Flask,request,jsonify,render_template  
import pickle

app = Flask(__name__,template_folder='template')

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list= movies['title'].values





@app.route('/',methods = ['get','post'])
def index():
    if request.method == "GET":    
        movies_list = pickle.load(open("movies_list.pkl", 'rb'))
        return render_template('home.html', movies_list = movies_list['title'])
    else :
        selected_movie = request.form.get('movie')
        index = movies[movies['title'] == selected_movie].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
        recommend_movie = []    
        for i in distance[1:6]:
            recommend_movie.append(movies.iloc[i[0]].title)
        a, b, c, d, e = recommend_movie[0], recommend_movie[1], recommend_movie[2], recommend_movie[3], recommend_movie[4]
        return render_template("home.html", final_result=a,final_result2=b,final_result3=c,final_result4=d,final_result5=e)

        

if __name__ == "__main__":
    app.run(debug=True)