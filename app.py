from flask import Flask, render_template, request
import requests
# api_key = "c9fc38ae0961e78162bcd6f8024a5887"
# url=f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=avengers"

# response = requests.get(url)
# print(response.status_code)
# data=response.json()
# print(data["results"][0]["title"])
# print(data["results"][0]["release_date"])
# print(data["results"][0]["overview"])

app = Flask(__name__)


@app.route('/')
def view():
    movie_name = request.args.get("movie")
    title = None
    release_date = None
    overview = None
    poster_url = None
    vote_average = None
    message = None
    if movie_name:
        api_key = "c9fc38ae0961e78162bcd6f8024a5887"
        try:
            url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data["results"]:
                    title = data["results"][0]["title"]
                    release_date = data["results"][0]["release_date"]
                    overview = data["results"][0]["overview"]
                    poster_path = data["results"][0]["poster_path"]
                    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
                    vote_average = data["results"][0]["vote_average"]

                else:
                    title = None
                    message = "Movie Not Found"
        except Exception as e:
            title = "Movie Not Found"
            print(e)

    #     print(movie_name)
    return render_template("index.html",
                           title=title,
                           release_date=release_date,
                           overview=overview,
                           poster_url=poster_url,
                           vote_average=vote_average,
                           message=message)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
