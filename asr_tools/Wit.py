from __future__ import absolute_import
from asr_tools.CIV_AsrTool import CIV_AsrTool
import speech_recognition as sr
import json

class Wit(CIV_AsrTool):

    def get_transcript(self):
        transcript = None
        passwords = json.load(open("/home/yichun/projects/automatic_speech_recognition/asr_tools/passwords.json", "r"))
        try:
            WIT_AI_KEY = passwords["WIT_AI_KEY"]  # Wit.ai keys are 32-character uppercase alphanumeric strings
            transcript = self.r.recognize_wit(self.audio, key=WIT_AI_KEY)
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0}".format(e))
        return transcript

