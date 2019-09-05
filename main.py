from __future__ import absolute_import
import os.path
import sys
sys.path.insert(0, os.path.dirname(__file__))
from asr_tools.GoogleSpeechRecognition import GoogleSpeechRecognition
import json

config = json.load(open("automatic_speech_recognition/config.json"))
lang = "fr"
audios = []
for root, dirs, files in os.walk(os.path.abspath(config["audio_dir_fr"])):
    for file in files:
        if "wav" in file: audios.append(os.path.join(root, file))

audios = sorted(audios)
for i in range(len(audios)):
    test = GoogleSpeechRecognition(lang=lang, audio_file=audios[i])
    id = audios[i].split("/")[-1].replace(".wav","")
    transcript = test.get_transcript()
    file = "/home/yichun/projects/automatic_speech_recognition/results/{}".format(config["tool"])
    if not os.path.exists(file):
        os.mknod(file)
    test.store_transcript_in_file(id=id, transcipt=transcript, file=file)
