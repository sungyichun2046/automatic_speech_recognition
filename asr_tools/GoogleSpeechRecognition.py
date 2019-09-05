from __future__ import absolute_import
from asr_tools.CIV_AsrTool import CIV_AsrTool
import speech_recognition as sr

class GoogleSpeechRecognition(CIV_AsrTool):

    def get_transcript(self):
        transcript = None
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            #print("Google Speech Recognition thinks you said " + self.r.recognize_google(self.audio, language=self.lang))
            transcript = self.r.recognize_google(self.audio, language=self.lang)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return transcript
