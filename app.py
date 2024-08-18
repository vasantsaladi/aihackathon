from flask import Flask, render_template, jsonify
from voice_recognition import record_audio, transcribe_audio, get_openai_response

app = Flask(__name__)   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voice_command', methods=['POST'])
def voice_command():
    try:
        filename = "output.wav"
        record_audio(filename)
        transcription = transcribe_audio(filename)
        response = get_openai_response(transcription)
        return jsonify({"transcription": transcription,"response": response})
    except Exception as e:
        app.logger.error(f"An error occurred in voice_command: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)










