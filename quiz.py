"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import ast
import json
from apikey import key
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask import Flask, render_template, redirect, url_for

genai.configure(api_key=key)

app = Flask(__name__)

def savefile(filename, content):
    if os.path.exists(filename):
        mode = 'a'  # Append to existing file
    else:
        mode = 'w'  # Create a new file

    with open(filename, mode) as f:
        f.write(content)

# Create the model
generation_config = {
  "temperature": 1.2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 2000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="topic related mcq questions , python list formate[{'Q':'what, why, how','O':{'a':'option a','b':'option b','c':'option c','d':'option d',},'A':'a'}, ]",
)

lst=[]


@app.route('/', methods=['GET', 'POST'])
def home():
    return '''
     <form action="/quiz" method="POST">
        <label for="topic">Your Topic:</label>
        <input type="text" id="topic" name="topic"><br><br>
        <button type="submit">Submit</button>
    </form>
    '''


@app.route('/quiz', methods=['POST'])
def quiz():
    topic = request.form.get('topic')
    response = model.generate_content([topic])
    savefile(topic, response.text)
    # strlst = json.loads(response.text)
    lst = ast.literal_eval(response.text)
    # print(response.text)
    if isinstance(lst, list):
        return render_template('quize.html',topic=topic,questions=lst)
    else:
      return f"<p>{response.text}</p>"


def checkscore(key,value,lst=lst):
  key=int(key[-1])-1
  answers = [item['A'] for item in lst]
  if answers[key] == value:
      return True
  else:
      return False

@app.route('/score', methods=['POST'])
def score():
  no_ques=len([item['A'] for item in lst])
  corr_ans=0
  mark=2
  score=0
  atmp_ques=0
  wrng_attmp=[]

  if request.method == 'POST':
      for key, value in request.form.items():
          atmp_ques+=1
          if checkscore(key,value):
              corr_ans+=1
              score+=mark
          else:
              wrng_attmp.append({"question_number": key, "question_text": (lst[int(key[-1])-1])['Q'] })
  wrng_ans=no_ques-corr_ans
  result_data = {
    "total_questions": no_ques,
    "correct_answers": corr_ans,
    "wrong_answers": wrng_ans,
    "total_score": score,
    "wrong_questions": wrng_attmp
}
  return render_template('result.html',**result_data)



if __name__ == '__main__':
    app.run(debug=True,port=5000)