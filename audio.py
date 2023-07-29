
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

language = "en"


def speak(text):
    speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
    audio_data = BytesIO()
    speech.write_to_fp(audio_data)
    audio_data.seek(0)
    audio_segment = AudioSegment.from_file(audio_data, format="mp3")
    play(audio_segment)

