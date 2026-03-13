from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/text-to-audio', methods=['POST'])
def text_to_audio():
    text = request.json.get('text')
    # Implement text-to-audio logic here
    return jsonify({'message': 'Audio generated for text: ' + text})

@app.route('/ppt-generation', methods=['POST'])
def ppt_generation():
    content = request.json.get('content')
    # Implement PowerPoint generation logic here
    return jsonify({'message': 'PowerPoint generated with content: ' + content})

if __name__ == '__main__':
    app.run(debug=True)