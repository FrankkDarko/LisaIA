import os
import openai
from datetime import timedelta
from flask import Flask, redirect, render_template, request, url_for, Response, stream_with_context, session

app = Flask(__name__)
app.secret_key = os.urandom(30)
app.permanent_session_lifetime = timedelta(minutes=50)

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_text(messages):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.6,
        max_tokens=1000,
    )

    output = response.choices[0].message.content.strip()
    return output


@app.route('/logout')
def logout():
    if 'system' in session.keys():
        session['data'] = [{"role": "system", "content": session['system']}, ]
    else:
        session['system'] = "You are a helpful assistant."
        session['data'] = [{"role": "system", "content": session['system']}, ]
    return redirect(url_for('chat'))


@app.route('/changesys', methods=['GET', 'POST'])
def changesys():
    session.pop('data', None)
    if request.method == 'POST':
        # get the description submitted on the web page
        prompt = request.form.get('description')
        if len(prompt) > 0:
            session['system'] = prompt
            session['data'] = [{"role": "system", "content": session['system']}, ]
            return redirect(url_for('chat'))
    return render_template('changesys.html')


@app.route('/', methods=['GET', 'POST'])
def chat():
    if 'data' in session.keys():
        messages = session['data']
        if request.method == 'POST':
            # get the description submitted on the web page
            prompt = request.form.get('description')
            if len(prompt) > 0:
                session['data'].append({"role": "user", "content": prompt}, )

                messages = session['data']
                a_description = generate_text(messages)

                messages.append({"role": "assistant", "content": a_description}, )
                session['data'] = messages

    else:
        session['system'] = os.getenv("PROMPT_SYS")
        session['data'] = [{"role": "system", "content": session['system']},
                           {"role": "assistant", "content": os.getenv("PROMTP_1_ASSISTANT")},
                           {"role": "user", "content": os.getenv("PROMTP_1_USER")},
                           ]

    return render_template('index.html', data=session['data'])


"""
def starter():
    app.run(port=os.getenv("FLASK_PORT"), host=os.getenv("FLASK_HOST"))
"""


