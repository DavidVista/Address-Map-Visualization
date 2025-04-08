from flask import Flask, request, render_template, jsonify
from collections import deque
import logging

app = Flask(__name__)
logging.basicConfig(
    filename='record.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
)
records_queue = deque()


@app.route('/upload', methods=['POST'])
def upload_record():
    global records_queue
    record = request.json
    records_queue.append(record)
    return "200"


@app.route('/load', methods=['GET'])
def load_records():
    global records_queue
    records = []
    while len(records_queue) > 0:
        records.append(records_queue.popleft())
    return jsonify({'records': records})


@app.route('/app', methods=['GET'])
def index():
    return render_template('table.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
