import os

# Add FFmpeg to PATH for this Python process
FFMPEG_PATH = r"C:\Users\ankit\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin"

os.environ["PATH"] += os.pathsep + FFMPEG_PATH

import whisper
import sounddevice as sd
from scipy.io.wavfile import write


SAMPLE_RATE = 16000
RECORD_SECONDS = 5


print("Loading Whisper model...")
model = whisper.load_model("base")
print("Whisper loaded!")


def record_audio():
    print("\nSpeak now...")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(
        "input.wav",
        SAMPLE_RATE,
        audio
    )

    print("Recording complete.")


def speech_to_text():
    result = model.transcribe("input.wav")

    return result["text"].strip()