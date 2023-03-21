import os
from dotenv import load_dotenv
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
load_dotenv()
openai.organization="org-YxpZaJEnJ52NPderjfdXJua0"
"""openai_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_key"""
openai.api_key="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"

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        """if request.is_json:"""
        data = request.get_json()
        text = data["text"]
        max_tokens = int(data["max_tokens"])
        print(text)
        print(max_tokens)
        """else:
            text = request.form["text"]
            max_tokens = int(request.form["max_tokens"])"""
    
        prompt, summary_length = generate_summary(text, max_tokens)
        response = openai.Completion.create(model="text-davinci-003",
                                            prompt=prompt, 
                                            temperature=0.7, 
                                            max_tokens=max_tokens,
                                            top_p=1,
                                            frequency_penalty=0, 
                                            presence_penalty=0)
        summary = response.choices[0].text
        summary_length = len(summary)
        return redirect(url_for("index", result=summary, length=summary_length))
    

    result = request.args.get("result")
    length = request.args.get("length")
    print(result)
    print(length)
    return {
        "result": result,
        "length": length
    }

    # return render_template("index.html", result=result, length=length)

def generate_summary(text, max_tokens):
    prompt = f'Summarize the following text:\n\n{text}\n\nSummary: {{length}} '
    prompt += f'{{length:{max_tokens}}}'
    return prompt.capitalize(), max_tokens
