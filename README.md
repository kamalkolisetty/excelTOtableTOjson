
# Flask Excel to JSON Uploader

This is a simple Flask application that allows users to upload an Excel file and saves its content as a JSON file on the server.

## Requirements

- Python 3.x
- Flask
- pandas
- openpyxl

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kamalkolisetty/excel.git
   cd flask-excel-to-json-uploader
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install Flask pandas openpyxl
   ```

## Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

2. **Open your web browser and go to:**

   ```
   http://127.0.0.1:5000/
   ```

3. **Upload an Excel file:**

   - Click the "Choose File" button.
   - Select an Excel file from your computer.
   - Click the "Upload" button.

4. **Check the success page:**

   - You will be redirected to a success page confirming that the file has been successfully uploaded and saved as `data.json`.

5. **Check the JSON file:**

   - The uploaded data will be saved in a file named `data.json` in the same directory as `app.py`.

## Project Structure

```
flask_excel_app/
├── app.py
├── data.json
└── README.md
```

- `app.py`: The main Flask application.
- `data.json`: The JSON file where the uploaded Excel data will be saved (created after the first upload).
- `README.md`: This README file.

## Code Explanation

- **app.py**:
  - Initializes the Flask application.
  - Defines routes for the home page (`/`) and the success page (`/success`).
  - Handles file upload, reads the Excel file using pandas, converts it to JSON, and saves it to `data.json`.
  - Uses `render_template_string` to render HTML directly from strings for simplicity.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
