from flask import Flask, jsonify, request
import difflib

app = Flask(__name__)

breeds = [
    "Andalusian",
    "Arabian",
    "Clydesdale",
    "Irish Sport Horse",
    "Quarter Horse",
    "Standardbred",
    "Tennessee Walker",
    "Thoroughbred"
]


@app.route('/closest-breed', methods=['GET'])
def get_closest_breed():
    query_breed = request.args.get('breed', None)

    if not query_breed:
        return jsonify({"error": "No breed provided"}), 400

    closest_matches = difflib.get_close_matches(query_breed, breeds, n=1, cutoff=0.0)

    if closest_matches:
        closest_breed = closest_matches[0]
        return jsonify({"breed": closest_breed})
    else:
        return jsonify({"error": "No close match found"}), 404


if __name__ == '__main__':
    app.run()
