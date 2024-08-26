from flask import Flask,render_template,request
import google.generativeai as palm
import os
import openai

api = "AIzaSyC6XTNnm_O-BCRuyAKgrhIr73_LgrNa4uQ"
palm.configure(api_key=api)
model = {"model": "models/chat-bison-001"}

os.environ["OPENAI_API_KEY"] = ""
client = openai.OpenAI()

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
    r = client.chat.completions.create( #This is a method provided by the OpenAI Python library to generate a response from an OpenAI model.
        model="gemini-1.5-flash",
        messages=[{"role": "user", "content": q}],
    )
    r = r.choices[0].message.content
    return(render_template("ai_agent_reply.html",r=r))

@app.route("/prediction", methods=["GET","POST"])
def prediction():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()
