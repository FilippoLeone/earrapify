from pydub import AudioSegment

def boost_track(filepath, filename, dB):
    try:
        song = AudioSegment.from_mp3(filepath)
        song = song + dB
        song.export(filepath, format='mp3')
        return True
    except:
        return False