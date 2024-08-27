from flask import Flask,render_template,request
from flask import jsonify
import google.generativeai as genai
import os
#import openai

api = "AIzaSyC6XTNnm_O-BCRuyAKgrhIr73_LgrNa4uQ"
genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-1.5-flash') #Creates a dictionary that maps the key "model" to the value "models/gemini-1.5-flash"

# os.environ["OPENAI_API_KEY"] = ""
# client = openai.OpenAI()

app = Flask(__name__)

#The @app.route decorator in Flask is used to bind a specific URL path to a Python functio
@app.route("/", methods=["GET","POST"]) #POST: Used to send data to the server to create or update a resource. Typically used for submitting form data, uploading files, etc.
def index():
    return(render_template("index.html"))

@app.route("/ai_agent", methods=["GET","POST"])
def ai_agent():
    return(render_template("ai_agent.html"))

@app.route("/ai_agent_reply", methods=["GET","POST"])
def ai_agent_reply():
    q = request.form.get("q")
    chat = model.start_chat()
    r = chat.send_message(q)
    # r_text = r.text
    # print(r)

    #Correctly extract the generated text from the response
    r_text = r.candidates[0].content.parts[0].text
    return(render_template("ai_agent_reply.html",r=r_text))

@app.route("/prediction", methods=["GET","POST"])
def prediction():
    return(render_template("index.html"))

@app.route("/joke_agent", methods=["GET", "POST"])
def joke_agent():
    if request.method =="POST":
        q = "Tell me a joke about Singapore"
        chat = model.start_chat()
        r = chat.send_message(q)
        r_text = r.candidates[0].content.parts[0].text  
        print(r_text)
        return render_template("joke_agent.html", r=r_text)
    return render_template("joke_agent.html")

@app.route("/generate", methods=["POST"])
def generate():
    # Logic to generate a new response
    q = "Tell me a joke about Singapore"
    chat = model.start_chat()
    r = chat.send_message(q)
    r_text = r.candidates[0].content.parts[0].text
    return jsonify({"r": r_text})


if __name__ == "__main__":
    app.run()
