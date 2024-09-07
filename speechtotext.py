import azure.cognitiveservices.speech as speechsdk

# Initialize the speech recognizer
def initialize_speech_recognizer(api_key, region):
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    return speech_recognizer

# Function to convert speech to text
def speech_to_text(speech_recognizer):
    print("Listening... Please speak into your microphone.")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Recognized: {result.text}")
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech Recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")
    return None

# Example usage
api_key = "99e288a8e7eb48fc91de6cc1f8e991d2"
region = "southindia"

speech_recognizer = initialize_speech_recognizer(api_key, region)
text_input = speech_to_text(speech_recognizer)

# You can now pass 'text_input' to your bot for processing
