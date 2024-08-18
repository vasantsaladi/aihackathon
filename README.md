# Voice Command App

This Voice Command App is a web-based application that captures voice input, transcribes it into text, and generates a response using an AI model. The application uses Flask for the backend, Google Cloud Speech-to-Text API for transcription, and OpenAI's GPT model for generating responses.

## Features

- **Voice Recording:** Record audio using the browser.
- **Transcription:** Convert recorded audio into text.
- **AI Response:** Generate responses to transcribed text using OpenAI's GPT model.

## Requirements

### Frontend

- Basic HTML and CSS
- Google Fonts (Roboto)

### Backend

- Python 3.x
- Flask
- PyAudio
- Google Cloud Speech-to-Text API
- OpenAI API
- dotenv for environment variable management

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/voice-command-app.git
cd voice-command-app
```

### 2. Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your API keys:

```bash
OPENAI_API_KEY=your-openai-api-key
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/google-cloud-credentials.json
```

### 5. Run the Application
```bash
python app.py
```

Navigate to `http://127.0.0.1:5000/` in your browser to use the app.

## Usage

1. Click the "Start Recording" button on the webpage to begin recording.
2. The app will capture your voice, transcribe it, and display the transcribed text.
3. An AI-generated response will be displayed based on the transcribed text.

## File Structure

- **index.html:** The front-end of the application.
- **app.py:** The Flask backend managing routes and API calls.
- **voice_recognition.py:** Handles recording audio, transcribing it using Google Cloud Speech-to-Text, and generating responses using OpenAI's GPT model.

## License

This project is licensed under the MIT License.

## Credits

- **Frontend:** Styled with custom CSS and Google Fonts.
- **Backend:** Built using Flask, Google Cloud Speech-to-Text, and OpenAI GPT-3.5.
