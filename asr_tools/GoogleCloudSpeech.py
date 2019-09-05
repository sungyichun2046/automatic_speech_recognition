from __future__ import absolute_import
from asr_tools.CIV_AsrTool import CIV_AsrTool
import speech_recognition as sr
import json

class GoogleCloudSpeech(CIV_AsrTool):

    def get_transcript(self):
        transcript = None
        passwords = json.load(open("/home/yichun/projects/automatic_speech_recognition/asr_tools/passwords.json", "r"))

        try:
            with open(passwords["google_cloud_speech"], 'r') as f:
                GOOGLE_CLOUD_SPEECH_CREDENTIALS = json.load(f)
            transcript = self.r.recognize_google_cloud(self.audio, credentials_json=json.dumps(GOOGLE_CLOUD_SPEECH_CREDENTIALS), language=self.lang)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
        return transcript

