import os
import numpy as np
import librosa


assert librosa.core._HAS_SAMPLERATE

ANALYZE_PATH = os.environ['analyze_file']
CALIBRATE_PATH = os.environ['calibrate_file']
CALIBRATE_DB = float(os.environ['calibrate_db'])
MAX_DURATION = os.environ.get('analyze_max_duration', None)


def amplitude_for_file(audio_path):
    y, sr = librosa.load(audio_path)
    # from http://bmcfee.github.io/librosa/librosa.html#librosa.core.logamplitude
    # Get a power spectrogram from a waveform y
    S = np.abs(librosa.stft(y)) ** 2
    log_S = librosa.logamplitude(S)
    return log_S

def db_for_file(audio_path):
    return np.mean(amplitude_for_file(audio_path))


db_offset = CALIBRATE_DB - db_for_file(CALIBRATE_PATH)
print db_for_file(ANALYZE_PATH) + db_offset
