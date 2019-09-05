from abc import ABC, abstractclassmethod
import speech_recognition as sr

class CIV_AsrTool(ABC):

    def __init__(self, lang=None, audio_file=None):
        self.lang = lang
        self.r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            self.audio = self.r.record(source)  # read the entire audio file

    @abstractclassmethod
    def get_transcript(self):
        pass

    def store_transcript_in_file(self, id=None, transcipt=None, file=None):
        result = "{} {}\n".format(id, transcipt)
        with open(file, "a") as f:
            f.write(result)

