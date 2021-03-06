from flask import Flask, render_template
from pokeapi import PokeAPI
from random import randrange

app = Flask(__name__)
api = PokeAPI()

@app.route('/')
def index():
    pokemon = api.getPokemon(randrange(782))
    return render_template('index.html', pokemon=pokemon)
  
@app.route('/<poke>')
def norand(poke):
    pokemon = api.getPokemon(poke)
    return render_template('norand.html',pokemon=pokemon)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
