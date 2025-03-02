from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

# External API endpoint for random words
BASE_RANDOM_WORD_API = "https://random-word-api.herokuapp.com/word"
# List of special characters to insert
SPECIAL_CHARS = list("!@#$%^&*()")


def generate_phrase_with_specials(words):
    """
    Joins a list of words into a phrase.
    If multiple words, it randomly inserts special characters between them.
    If a single word, it only optionally adds special characters at the beginning and/or end.
    """
    if len(words) == 1:
        phrase = words[0]
    else:
        phrase = words[0]
        for word in words[1:]:
            mode = random.choice([0, 1, 2])
            if mode == 0:
                #space
                phrase += " " + word
            elif mode == 1:
                # Space, special char, space
                phrase += " " + random.choice(SPECIAL_CHARS) + " " + word
            else:
                # Special char directly concatenated
                phrase += random.choice(SPECIAL_CHARS) + word

    # Optionally add a special character at the beginning and/or end
    if random.choice([True, False]):
        phrase = random.choice(SPECIAL_CHARS) + phrase
    if random.choice([True, False]):
        phrase = phrase + random.choice(SPECIAL_CHARS)

    return phrase


def get_random_phrase():
    """
    Queries the external Random Word API to generate a random phrase.
    A random number of words (between 1 and 4) is requested, and then special characters are inserted accordingly.
    """
    num_words = random.randint(1, 4)
    api_url = f"{BASE_RANDOM_WORD_API}?number={num_words}"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) and data:
            return generate_phrase_with_specials(data)
        else:
            return "No word found"
    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def index():
    generated_phrase = ""
    if request.method == "POST":
        generated_phrase = get_random_phrase()
    return render_template("index.html", generated_phrase=generated_phrase)


if __name__ == "__main__":
    app.run(debug=True)
