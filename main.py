import functions_framework
from flask import jsonify
from src.translator import translate_content

@functions_framework.http
def translate(request):
    request_args = request.args

    if request_args and "content" in request_args:
        content = request_args["content"]
    is_english, translated_content = translate_content(content)
    return jsonify({
        "is_english": is_english,
        "translated_content": translated_content,
    })
