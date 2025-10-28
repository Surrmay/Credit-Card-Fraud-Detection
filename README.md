# Credit-Card-Fraud-Detection 🛡️

[![License](https://img.shields.io/badge/License-None-brightgreen.svg)](https://github.com/Surrmay/Credit-Card-Fraud-Detection)
[![Stars](https://img.shields.io/github/stars/Surrmay/Credit-Card-Fraud-Detection?style=social)](https://github.com/Surrmay/Credit-Card-Fraud-Detection)
[![Forks](https://img.shields.io/github/forks/Surrmay/Credit-Card-Fraud-Detection?style=social)](https://github.com/Surrmay/Credit-Card-Fraud-Detection)

## Description 📝

This project provides a simple Flask-based backend and an HTML frontend for simulating credit card fraud detection. The backend exposes an API endpoint `/api/predict` that takes transaction data as input and returns a fraud probability score, a boolean indicating whether the transaction is fraudulent, and a risk level (HIGH, MEDIUM, or LOW). The frontend allows users to input transaction details and view the analysis results. It's important to note that the current frontend uses simulated ML model predictions for demonstration purposes.

## Table of Contents 🗂️

1.  [Features](#features-sparkles)
2.  [Tech Stack](#tech-stack-computer)
3.  [Installation](#installation-gear)
4.  [Usage](#usage-rocket)
5.  [Project Structure](#project-structure-file_folder)
6.  [API Reference](#api-reference-gear)
7.  [Contributing](#contributing-handshake)
8.  [License](#license-scroll)
9.  [Important Links](#important-links-link)
10. [Footer](#footer-arrow_down)

## Features ✨

*   **Transaction Analysis**: Simulates credit card fraud detection based on transaction details.
*   **Risk Level Assessment**: Determines the risk level (HIGH, MEDIUM, LOW) of a transaction.
*   **Flask Backend**: Provides a REST API for receiving transaction data and returning predictions.
*   **HTML Frontend**: User-friendly interface for inputting transaction details and viewing results.
*   **Simulated ML Model**: Uses simulated ML model predictions for demonstration purposes.
*   **Quick Fill Examples**: Provides quick fill buttons for normal, suspicious, and high-risk transactions.

## Tech Stack 💻

*   **Backend**: Python, Flask
*   **Frontend**: HTML, CSS, JavaScript
*   **Model**: Python (Joblib for model loading)

## Installation ⚙️

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Surrmay/Credit-Card-Fraud-Detection.git
    cd Credit-Card-Fraud-Detection
    ```

2.  **Set up a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.  **Install Flask:**

    ```bash
    pip install Flask joblib numpy
    ```

    *Note: The provided code does not explicitly list dependencies in a `requirements.txt` file. The above command installs Flask and necessary packages based on the `app.py` file.* 

## Usage 🚀

1.  **Run the Flask backend:**

    ```bash
    python app.py
    ```

    This will start the Flask development server.

2.  **Open the `fraud_detection_frontend.html` file in your browser.** This file provides a user interface to input transaction details and get fraud predictions.

3.  **Interact with the Frontend:**

    *   Enter the transaction details like amount, time and merchant category in the respective fields.
    *   Click the "Analyze Transaction" button to submit the data to the backend and receive a fraud prediction.
    *   The results will be displayed on the right side of the screen, showing the fraud probability, risk level, and other details.
    *   Use the Quick Fill buttons for example transactions.

### API Endpoint

The Flask backend exposes a single API endpoint:

*   **`/api/predict`** (POST):
    *   Accepts a JSON payload containing transaction data.
    *   Returns a JSON response with the fraud probability, isFraud boolean, and riskLevel.

    Example Request:

    ```json
    {
      "amount": 100.00,
      "time": 3600,
      "merchant_category": "retail",
       "v1": 0,
       "v2": 0,
       "v3": 0,
       "v4": 0
    }
    ```

    Example Response:

    ```json
    {
      "fraudProbability": 0.25,
      "isFraud": false,
      "riskLevel": "LOW"
    }
    ```

### Use Case
This project simulates a basic fraud detection system. It can be used for educational purposes to understand how a fraud detection system works or as a starting point for building a more sophisticated system.

## Project Structure 📂

```
Credit-Card-Fraud-Detection/
├── app.py                         # Flask backend application
├── fraud_detection_frontend.html  # HTML frontend for user interaction
├── fraud_detection_model.pkl      # Serialized fraud detection model (dummy file)
├── creditcard.csv                 # CSV file with credit card transaction data (empty file)
├── feature_names.pkl              # Serialized feature names (dummy file)
├── fraud_detection_report.txt   # Text file containing a fraud detection report
├── model_1.ipynb                  # Jupyter notebook for model development (dummy file)
├── scaler.pkl                     # Serialized scaler object (dummy file)
└── README.md                      # Project documentation
```

## API Reference ⚙️

### `POST /api/predict`

*   **Description:** Predicts the probability of a transaction being fraudulent.
*   **Request Body:** A JSON object containing transaction details. Required fields include:
    *   `amount` (number): Transaction amount.
    *   `time` (number): Time elapsed since the first transaction.
    *   `merchant_category` (string): Merchant category.
    *   `v1`, `v2`, `v3`, `v4` (number): PCA features
*   **Response:** A JSON object containing the prediction results:
    *   `fraudProbability` (number): The probability of the transaction being fraudulent (0 to 1).
    *   `isFraud` (boolean): Indicates whether the transaction is predicted to be fraudulent.
    *   `riskLevel` (string): The risk level associated with the transaction (HIGH, MEDIUM, or LOW).

## Contributing 👋

Contributions are welcome! Here's how you can contribute:

*   Fork the repository.
*   Create a new branch for your feature or bug fix.
*   Make your changes and commit them with descriptive messages.
*   Submit a pull request.

## License 📜

This project has no specified license.

## Important Links 🔗

*   **Repository:** [https://github.com/Surrmay/Credit-Card-Fraud-Detection](https://github.com/Surrmay/Credit-Card-Fraud-Detection)

## Footer 👇

[Credit-Card-Fraud-Detection](https://github.com/Surrmay/Credit-Card-Fraud-Detection) by [Surrmay](https://github.com/Surrmay). Feel free to fork, star, and open issues!


---
**<p align="center">Generated by [ReadmeCodeGen](https://www.readmecodegen.com/)</p>**