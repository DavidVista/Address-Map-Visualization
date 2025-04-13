from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
records_list = []


@app.route('/upload', methods=['POST'])
def upload_record():
    global records_list
    record = request.json
    records_list.append(record)
    return jsonify({"status": "success"}), 201


@app.route('/download', methods=['GET'])
def load_records():
    global records_list
    records = []
    idx = request.args.get('idx', default=0, type=int)
    for i in range(idx, len(records_list)):
        records.append(records_list[i])
    return jsonify({'records': records})


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=True)
