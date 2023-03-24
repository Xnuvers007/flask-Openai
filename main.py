import openai
from flask import Flask, request, render_template

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

openai.api_key = "YOUR-APIKEY-OPENAI"

@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        input_text = request.form["input-text"]
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=input_text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
        output = completions.choices[0].text
        return render_template("index.html", output=output)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=80,
            debug=True)
