import sys

args = sys.argv[1:]
if len(args) != 1:
    print("Write the filename at the end of the call. Example:\npython main.py audio.mp3")
    exit()

import transcription

transcription.load_model()
file = args[1]
output = transcription.transcribe(file)

for segment in output["segments"]:
    print(f"{segment['start']:.1f}s", "\t", segment["text"])
    
transcription.save_ass_file(output)