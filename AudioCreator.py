from dataclasses import dataclass
from io import BytesIO
from gtts import gTTS
from pydub import AudioSegment


@dataclass
class Word:
    Original: str = ''
    OriginalLang: str = ''
    Translated: str = ''
    TranslatedLang: str = ''


def create_combined_audio(word: Word):

    # Function to convert text to AudioSegment using gTTS
    def text_to_audio(text, lang):
        mp3_fp = BytesIO()
        tts = gTTS(text=text, lang=lang)
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        audio_segment = AudioSegment.from_mp3(mp3_fp)
        return audio_segment

    # Generate Japanese word audio
    japanese_audio = text_to_audio(word.Original, word.OriginalLang)

    # Generate English word audio
    english_audio = text_to_audio(word.Translated, word.TranslatedLang)

    # Generate countdown audio
    silence_3_sec = AudioSegment.silent(duration=1500)
    silence_2_sec = AudioSegment.silent(duration=1500)

    # Combine the three parts
    combined_audio = japanese_audio + silence_3_sec + english_audio + silence_2_sec

    # Apply a 2-second fade-out
    fade_out_duration = 2000  # in milliseconds
    combined_audio_with_fade = combined_audio.fade_out(fade_out_duration)

    return combined_audio_with_fade


def CreateAudio(words: list[Word], parentFolder='Words'):
    for word in words:
        combined_audio = create_combined_audio(word)
        combined_audio.export(
            f'{parentFolder}\\{word.Original}_{word.Translated}.mp3', format="mp3")
