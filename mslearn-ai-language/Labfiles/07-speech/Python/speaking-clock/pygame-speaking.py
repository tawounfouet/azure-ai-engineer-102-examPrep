from dotenv import load_dotenv
from datetime import datetime
import pygame
import os

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk


def main():
    try:
        global speech_config

        # Get Configuration Settings
        load_dotenv()
        ai_key = os.getenv("SPEECH_KEY")
        ai_region = os.getenv("SPEECH_REGION")

        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
        print("Ready to use speech service in:", speech_config.region)

        # Get spoken input
        command = TranscribeCommand()
        if command.lower() == "what time is it? I want to go to the gym":
            TellTime()

    except Exception as ex:
        print(ex)


def TranscribeCommand():
    command = ""

    # Configure speech recognition
    current_dir = os.getcwd()
    audioFile = os.path.join(current_dir, "time.wav")

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(audioFile)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    audio_config = speech_sdk.AudioConfig(filename=audioFile)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    print("Speak now...")

    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command


def TellTime():
    now = datetime.now()
    response_text = "The time is {}:{:02d}".format(now.hour, now.minute)

    # Configure speech synthesis
    #speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    speech_config.speech_synthesis_voice_name = 'en-GB-LibbyNeural' # change this

    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

    # Print the response
    print(response_text)


if __name__ == "__main__":
    main()
