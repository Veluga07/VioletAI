# routes.py

from flask import request, jsonify
from . import app
from ..models.model import generate_text
from ..filters.filter import filter_content

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get('prompt')
    result = generate_text(prompt)
    filtered_result = filter_content(result)
    return jsonify({'text': filtered_result})
