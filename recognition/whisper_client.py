import whisper

model = whisper.load_model("base")
result = model.transcribe(r"media/recorded_audio.wav")
print(result["text"])
