# FlaskAPI-SquareCalculator
_FlaskAPI-SquareCalculator is a simple Flask-based REST API project that provides two endpoints. One endpoint returns data sent through GET or POST requests, and the other calculates the square of a number sent via a GET request._

## Getting Started
_These instructions will help you get the FlaskAPI-SquareCalculator up and running on your local machine._

### Prerequisites
  - Python 3.x
  - Flask

## Installation
  - **Clone the repository:**

```bash
###
git clone https://github.com/your-username/FlaskAPI-SquareCalculator.git
```
  - **Change to the project directory:**

```bash
###
cd FlaskAPI-SquareCalculator
```

  - **Create a virtual environment (optional but recommended):**

```bash
###
python -m venv venv
```
- 1.1 **Activate the virtual environment:**
  - On Windows:
```bash
###
venv\Scripts\activate
```
- 1.2
  - On macOS and Linux:
```bash
###
source venv/bin/activate
```

- **Install the required dependencies:**
```bash
###
pip install -r requirements.txt
```

## Running the Application
To run the Flask API, use the following command:

```bash
###
python app.py
```
The API will start and be accessible at
  - `http://localhost:5000/.`

## API Endpoints
  - `GET /:`
    - Returns: `{'data': 'Hello Melinda'}` for a GET request.
    - Accepts data and returns it for a POST request.
  - `GET /square/<int:num>`:
    - Calculates the square of the provided integer (num).
    - Returns: {'square': result}.
## Example Usage
_You can use tools like `curl` or your preferred REST client to interact with the API._
  - Sending a GET request to the root URL:

```bash
###
curl http://localhost:5000/
```

- **Sending a POST request with data to the root URL:**
```bash
###
curl -X POST -d "Some data" http://localhost:5000/
```
- **Calculating the square of a number (e.g., 3):**
```bash
###
curl http://localhost:5000/square/3
```
  
## Contributing
_Contributions are welcome. Feel free to open issues or submit pull requests if you have any suggestions or improvements._
Created By [Saumyadeep Mitra](https://in.linkedin.com/in/saumyadeep-mitra-a64030236)


## License
_This game is open-source and released under the_ [MIT License](https://opensource.org/licenses/MIT)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
