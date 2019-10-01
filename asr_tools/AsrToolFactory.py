import os
from asr_tools.GoogleSpeechRecognition import GoogleSpeechRecognition
from asr_tools.Sphinx import Sphinx
from asr_tools.GoogleCloudSpeech import GoogleCloudSpeech

class AsrToolFactory():
    def __init__(self, lang=None, asr_tool=None, audios=None):
        self.asr_tool = asr_tool
        self.audios = audios
        self.lang = lang

    def store_transciptions(self):
        for i in range(len(self.audios)):
            if self.asr_tool == "google_cloud_speech":
                tool = GoogleCloudSpeech(lang=self.lang, audio_file=self.audios[i])
            elif self.asr_tool == "google_speech_recognition":
                tool = GoogleSpeechRecognition(lang=self.lang, audio_file=self.audios[i])
            elif self.asr_tool == "sphinx":
                tool = Sphinx(lang=self.lang, audio_file=self.audios[i])

            id = self.audios[i].split("/")[-1].replace(".wav","")
            transcript = tool.get_transcript()
            file = "/home/yichun/projects/automatic_speech_recognition/results/{}".format(self.asr_tool)
            #tool = google_speech_recognition, sphinx, google_cloud_speech, wit
            if not os.path.exists(file):
                os.mknod(file)
            tool.store_transcript_in_file(id=id, transcipt=transcript, file=file)
