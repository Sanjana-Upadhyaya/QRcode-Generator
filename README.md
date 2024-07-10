# QRcode-Generator
This is a simple web-based application that generates QR codes based on user input. The generated QR codes can be downloaded in PNG or JPG format and shared via a link.

## Features

- Generate QR codes from user input.
- Download QR codes as PNG or JPG.
- Share QR codes via a link.

## Screenshots

![Main Page](screenshots/Screenshot 2024-07-10 162557.png)
![QR Code Generated](screenshots/Screenshot 2024-07-10 162629.png)
![Share](screenshots/Screenshot 2024-07-10 162707.png)

  ### Prerequisites

- Python 3.12 or later
- Django 5.0.6 or later

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Sanjana-Upadhyaya/QRcode-Generator.git
    cd QRcode-Generator
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv Env
    source Env/bin/activate  # On Windows use `Env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

5. Open your web browser and navigate to `http://127.0.0.1:8000/` to use the application.

## Usage

1. Enter the text you want to encode in the QR code.
2. Click "Generate QR Code" to generate the QR code.
3. Use the buttons to share the QR code or download it in PNG or JPG format.

## Project Structure

- `qrcode_project/` - Main project directory.
- `qrgenerator/` - App directory containing the main QR code generation logic.
- `static/` - Directory for static files (CSS, JavaScript).
- `templates/` - Directory for HTML templates.
- `.gitignore` - Specifies which files and directories to ignore in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
