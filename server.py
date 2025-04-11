from flask import Flask, request, render_template, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(
    filename='record.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
)
records_list = []


@app.route('/upload', methods=['POST'])
def upload_record():
    global records_list
    record = request.json
    records_list.append(record)
    return "200"


@app.route('/load', methods=['GET'])
def load_records():
    global records_list
    records = []
    idx = request.args.get('idx', default=0, type=int)
    for i in range(idx, len(records_list)):
        records.append(records_list[i])
    return jsonify({'records': records})


@app.route('/app', methods=['GET'])
def index():
    return render_template('table.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
