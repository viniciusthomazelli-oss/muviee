from flask import Flask, render_template
import os

app = Flask(__name__)

FILMES = [
    {
        "id": 1,
        "titulo": "PAW Patrol: The Dino Movie",
        "data_lancamento": "14 de Agosto de 2026",
        "sinopse": "A Patrulha Canina embarca em uma aventura pré-histórica em um mundo repleto de dinossauros. Assista ao ",
        "trailer_url": "https://www.youtube.com/embed/xgI5iYmOf5Q", # Substitua pelo ID do trailer real
        "poster_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBm0zhR1fXFyn7rTgSR1LnYXq8Z_z5rVOmyOO7r_6aCSbOZKBTusNgUoKy&s=10"
    },
    {
        "id": 2,
        "titulo": "Insidious: Out of the Further",
        "data_lancamento": "21 de Agosto de 2026",
        "sinopse": "O próximo capítulo aterrorizante da franquia Sobrenatural que explora as profundezas do Além. Assista ao ",
        "trailer_url": "https://www.youtube.com/embed/ZuQuOnYnr3Q?si=DN2WRVvg4O-SCjtt",
        "poster_url": "https://m.media-amazon.com/images/M/MV5BMTY4YjM1OGItMDlmMi00OTU1LWEzM2MtZGMyZTQ1NzhiM2VhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
    },
    {
        "id": 3,
        "titulo": "Practical Magic 2",
        "data_lancamento": "11 de Setembro de 2026",
        "sinopse": "As irmãs bruxas mais famosas do cinema retornam com novas magias e feitiços. Assista ao ",
        "trailer_url": "https://www.youtube.com/embed/Ho10_4IX1jE?si=FJDn6bwYKW2BbTgt",
        "poster_url": "https://ihorror.com/wp-content/uploads/2025/05/Practical-Magic-2-Movie.jpg"
    },
    {
        "id": 4,
        "titulo": "Forgotten Island",
        "data_lancamento": "25 de Setembro de 2026",
        "sinopse": "Uma expedição descobre uma ilha remota com criaturas esquecidas pelo tempo. Assista ao ",
        "trailer_url": "https://www.youtube.com/embed/f7mFVeWnVLw?si=Xfz3aTxqKd_vWi3d",
        "poster_url": "https://upload.wikimedia.org/wikipedia/en/6/65/Forgotten_Island_poster.jpeg"
    },
    {
        "id": 5,
        "titulo": "The Legend of Aang: The Last Airbender",
        "data_lancamento": "8 de Outubro de 2026",
        "sinopse": "A adaptação épica para o cinema que acompanha as aventuras adultas de Aang. Assista ao ",
        "trailer_url": "https://www.youtube.com/embed/34j4XKx7OMw?si=gfY9z6n86byxpX51",
        "poster_url": "https://upload.wikimedia.org/wikipedia/pt/c/ca/Avatar_Aang_The_Last_Airbender_poster.jpg"
    }
]

@app.route("/")
def index():
    return render_template("index.html", filmes=FILMES)

if __name__ == "__main__":
    # O Render exige que o app use uma porta dinâmica definida pelo sistema
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)