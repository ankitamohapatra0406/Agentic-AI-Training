from speech_to_text import record_audio, speech_to_text
from llm import get_response
from text_to_speech import speak

print("=" * 60)
print("VOICE ASSISTANT")
print("=" * 60)
print("\nVoice Assistant is ready!")
print("Speak for 5 seconds after the prompt.")
print("Say 'exit' to stop.\n")


while True:
    record_audio()
    user_text=speech_to_text()
    print("\nYou:", user_text)

    if user_text.lower() in ["exit", "quit", "stop"]:
        print("Goodbye!")
        speak("Goodbye!")
        break

    if not user_text:
        print("I couldn't hear anything. Try again.")
        continue

    print("\nThinking...")
    response=get_response(user_text)

    print("\nAI:", response)
    speak(response)