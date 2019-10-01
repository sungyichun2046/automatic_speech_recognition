from __future__ import absolute_import
import os.path
import sys
sys.path.insert(0, os.path.dirname(__file__))
import json
from asr_tools.AsrToolFactory import AsrToolFactory

config = json.load(open("automatic_speech_recognition/config.json"))
#Get all audio files
audios = []
for root, dirs, files in os.walk(os.path.abspath(config["audio_dir_fr"])):
    for file in files:
        if "wav" in file: audios.append(os.path.join(root, file))
#Generate and store transcriptions
audios = sorted(audios)
asrtool = AsrToolFactory(lang=config["lang"], asr_tool=config["asr_tool"], audios=audios)
asrtool.store_transciptions()



