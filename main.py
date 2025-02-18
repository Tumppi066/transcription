import sys

args = sys.argv[1:]
if len(args) != 1:
    print("Write the filename at the end of the call. Example:\npython main.py audio.mp3")
    exit()

file = args[0]

import transcription
transcription.load_model()
output = transcription.transcribe(file)

for segment in output["segments"]:
    print(f"{segment['start']:.1f}s", "\t", segment["text"])
    
transcription.save_txt_file(output)
transcription.save_ass_file(output)