## Branch master ##

### Description : ###
 - Tests and evaluations of automatic speech recognition tools on 104 french sentences
   (https://mega.nz/#F!oMp3xAqY!7fiwn30szuTpIDy6eLhJcw)
 - Improvements by grammar, spelling checkers (in progress)

### Table of Contents: ###


| File                                     | Description                                                |
| -----------------------------------------| ---------------------------------------------------------- |
| main.py                                  | main script to generate transciptions for input audio files|
| config.json                              | asr tool used, language and input audio files in main.py   |
| data/audio_files                         | audio files + correct transcriptions                       |
| asr_tools/AsrToolFactory                 | called in main.py, translation of audio files into text    |
| asr_tools/CIV_AsrTool.py                 | 1) generate transciption (abstract fonction get_transcript)|
|                                          | 2) store transcriptions(fonction store_transcript_in_file) |
| asr/passwords_example.json               | example passwords.json(TO CREATE)                          |



### Installation: ###

 - Create a environment of python3 : `mkvirtualenv -p python3 nlp`
 - `pip install --upgrade pip`
 - Install packages we need (in production env): `pip install -r requirements.txt`
 - Install evaluation tool : `pip install asr-evaluation`

### Usage: ###

 - Go up to the directory above `NLP chain` folder and run `python -m automatic_speech_recognition.main`
 - Commands for evaluation: `https://github.com/belambert/asr-evaluation`

### Generate a requirements.txt file ###

   - Run `pip install pipreqs`
   - Run `pipreqs /path/to/project`

### Results ###

| Tool                           | WER    | WRR    | SER    |
| ------------------------------ | ------------------------ |
| Google Speech Recognition      | 26.79% | 76.36% | 99.12% |
| Sphinx                         | 59.04% | 44.04% | 100%   |
| Google Cloud Speech            | 27.65% | 75.60% | 99.12% |

 - WER:Word Error Rate
 - WRR:Word Right Rate
 - Ser:Sentence Error Rate

### To improve ###

  - Take account of french liaison
  - Slow down the end of audio files
  - Improvement by syntax tree
