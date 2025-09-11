# Flask Hello

This project is a simple Flask application. It includes the following files:

- `application.py`: The main Flask application file.
- `requirements.txt`: Lists the Python dependencies required to run the app.
- `Dockerfile`: Used to build a Docker image for the application.
- `.github/workflows/main_flask_hello-aws.yml`: GitHub Actions workflow for CI/CD, possibly for AWS deployment.

## Getting Started

### Prerequisites
- Python 3.x
- pip
- (Optional) Docker

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd flask-hello
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application
To start the Flask app locally:
```sh
python application.py
```

The app will be available at `http://localhost:5000` by default.

### Using Docker
To build and run the app with Docker:
```sh
docker build -t flask-hello .
docker run -p 5000:5000 flask-hello
```

### GitHub Actions CI/CD
This project includes a GitHub Actions workflow in `.github/workflows/main_flask_hello-aws.yml` for automated testing and deployment (e.g., to AWS). The workflow will run on every push or pull request.

## Project Structure
```
application.py
Dockerfile
requirements.txt
.github/
  workflows/
    main_flask_hello-aws.yml
```

