from flask import Flask, jsonify, request
import difflib

app = Flask(__name__)

words = [
    "Palomino",
    "Chestnut",
    "Bay",
    "Mare",
    "Gelding",
    "Stallion",
    "Dressage",
    "Eventing",
    "Hand",
    "Endurance"
]

@app.route('/closest-term', methods=['GET'])
def get_closest_word():
    query_word = request.args.get('word', None)
    
    if not query_word:
        return jsonify({"error": "No word provided"}), 400
    
    closest_matches = difflib.get_close_matches(query_word, words, n=1, cutoff=0.0)
    
    if closest_matches:
        closest_word = closest_matches[0]
        return jsonify({"word": closest_word})
    else:
        return jsonify({"error": "No close match found"}), 404

if __name__ == '__main__':
    app.run()
