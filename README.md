# Address-Map-Visualization
A public client-server application for visual analysis of incoming IP address queries.

First, the `scraper/scraper.py` script is used to fetch the incoming IP address information. At the same time, the HTTP server receives passed information records and provide the real-time asynchronous view for a client. The `server/server.py` contains the implementation of the server code using Flask framework. Three routes are used: `/upload` for loading record information, `/download` for requesting already fetched records, and `/` for `server/templates/index.html`. Finally, the javascript application on the page performs ajax requests to the server using `/download` route, and automatically fetches upcoming records.

The visualization part is implemented in the same `index.html` file using Three.js framework. The framework allows to create 3D interractive visual applications. In this project, I used a 3D earth model to visualize points representing individual records. The visualization includes the following interractive features:
- List of recently fetched records;
- Information about each point by mouse hover;
- Highlighting point by click on the button;
- List of highlighted points;
- Map rotaion;
- Zoom in and out with scaling size of points.

## Installation

### Manual Setup

#### Requirements
- Python version >= 3.11

#### Steps
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

#### Steps
1. Run the single command:
```bash
docker compose up -d
```

2. Use browser to see the client-side of the application by visiting <a href="http://127.0.0.1:8080">http://127.0.0.1:8080</a>.

3. Use the following command to stop the applications:
```bash
docker compose down
```
