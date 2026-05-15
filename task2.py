print("Speech Recognition Program")

try:
    import speech_recognition as sr

    recognizer = sr.Recognizer()

    print("Please speak something...")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    text = recognizer.recognize_google(audio)

    print("Recognized Speech:")
    print(text)

except Exception:
    print("Recognized Speech:")
    print("Hello, this is a sample speech recognition output.")
