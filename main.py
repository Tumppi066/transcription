import transcription

transcription.load_model()
file = "samir.mp3"
output = transcription.transcribe(file)

for segment in output["segments"]:
    print(f"{segment['start']:.1f}s", "\t", segment["text"])
    
transcription.save_ass_file(output)