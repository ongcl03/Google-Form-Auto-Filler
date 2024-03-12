# Google Form Filler

This Python script automates the process of filling Google Forms programmatically. It can be used to submit responses to a Google Form without manual intervention.

## Prerequisites

Before using this script, ensure you have the following:

- Python 3 installed on your system.
- The `requests` library installed. You can install it using pip:

```bash
pip install requests
```

## Usage

1. Clone or download this repository to your local machine.

2. Open the `google_form_filler.py` file and modify the `url` and `form_data` variables according to your Google Form. Replace the `url` variable with the URL of your Google Form and provide the necessary form data in the `form_data` dictionary.

3. Run the script using the following command:

```bash
python google_form_filler.py
```

4. The script will submit the form data to the specified Google Form URL.

## Note

- If your Google Form has multiple pages, ensure to include the `pageHistory` field in the `form_data` dictionary with the appropriate value.

- This script assumes that the form fields are identified by their entry IDs. You need to inspect the HTML of your Google Form to find the correct entry IDs for your form fields.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
