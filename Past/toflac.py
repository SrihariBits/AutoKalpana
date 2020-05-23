import soundfile as sf
from os import path
from pydub import AudioSegment

# files                                                                         
src = "Sila.mp3"
dst = "Sila.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

data, samplerate = sf.read('Sila.wav')
sf.write('Sila.flac', data, samplerate)
