from __future__ import absolute_import
from asr_tools.CIV_AsrTool import CIV_AsrTool
import speech_recognition as sr

class Sphinx(CIV_AsrTool):

    def get_transcript(self):
        transcript = None
        try:
            transcript = self.r.recognize_sphinx(self.audio, language="fr-FR")
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        return transcript
