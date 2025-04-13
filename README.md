# Address-Map-Visualization
A public client-server application for visual analysis of incoming IP address queries.

First, the `scraper.py` script is used to fetch the incoming IP address information. At the same time, the HTTP server receives passed information records and provide the real-time asynchronous view for a client.

## Installation

### Manual Setup

#### Requirements
- Python version >= 3.11

1. Virtual Environment Setup:
```bash
python -m venv venv
```

2. <a href="https://docs.python.org/3/library/venv.html">Activate</a> virtual environment.

3. Install necessary requirements:
```bash
pip install -r req.txt
```

4. Start the server:
```bash
python server/server.py
```

5. Start the scraper:
```bash
python scraper/scraper.py
```

6. Use browser to see the client-side of the application by visiting <a href="http://127.0.0.1:8080">http://127.0.0.1:8080</a>.

### Docker Compose

#### Requirements
- Docker

1. Run the single command:
```bash
docker compose up -d
```

2. Use browser to see the client-side of the application by visiting <a href="http://127.0.0.1:8080">http://127.0.0.1:8080</a>.

3. Use the following command to stop the applications:
```bash
docker compose down
```
