"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

NEGATIVE = [
      'pillock', 'lickspittle', 'smwllfungus', 'ninnyhammer', 'mumpsimus', 'pettifogger',
      'mooncalf','picklepuss', 'stinker', 'stinkpot','lousy', 'rapscallion', 'scallywag',
      'flibbertigibbet']


    
@app.route('/')   
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.</html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Choose your AWESOMENESS:
          <select name="awesomeness">
          <option value='awesome' >awesome</option>
          <option value='terrific'>terrific</option>
            <option value='fantastic'>fantastic</option>
            <option value='neato'>neato</option>
            <option value='fantabulous'>fantabulous</option>
            <option value='wowza'>wowza</option>
            <option value='oh-so-not-meh'>oh-so-not-meh</option>
            <option value='brilliant'>brilliant</option>
            <option value='ducky'>ducky</option>
            <option value='coolio'>coolio</option>
            <option value='incredible'>incredibile</option>
            <option value='wonderful'>wonderful</option>
            <option value='smashing'>smashing</option>
            <option value='lovely'>lovely</option>
          </select>
          <input type="submit" value="Submit">
        </form>
        <form action='/diss'>
          What's your name? <input type="text" name="person">
          Get insultedgit 
           <select name="negative">
          <option value='pillock' >pillock</option>
          <option value='lickspittle'>lickspittle</option>
            <option value='smwllfungus'>smwllfungus</option>
            <option value='ninnyhammer'>ninnyhammer</option>
            <option value='mumpsimus'>mumpsimus</option>
            <option value='pettifogger'>pettifogger</option>
            <option value='mooncalf'>mooncalf</option>
            <option value='picklepuss'>picklepuss</option>
            <option value='stinker'>stinker</option>
            <option value='stinkpot'>stinkpot</option>
            <option value='lousy'>lousy</option>
            <option value='rapscallion'>rapscallion</option>
            <option value='scallywag'>scallywag</option>
            <option value='flibbertigibbet'>flibbertigibbet</option>
          </select>
          <input type="submit" value="Submit" name="negative">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    
    # compliment = choice(AWESOMENESS)
    compliment=request.args.get("awesomeness")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """
@app.route('/diss')
def diss_person():
    player = request.args.get("person")
    insult = request.args.get("negative")
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """
  

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0", port=5001)
 