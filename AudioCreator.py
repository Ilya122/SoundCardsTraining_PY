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


def __CreateCombinedAudio(word: Word):

    def text_to_audio(text, lang):
        mp3_fp = BytesIO()
        tts = gTTS(text=text, lang=lang)
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        audio_segment = AudioSegment.from_mp3(mp3_fp)
        return audio_segment

    originalAudio = text_to_audio(word.Original, word.OriginalLang)

    englishAudio = text_to_audio(word.Translated, word.TranslatedLang)

    silence1500sec = AudioSegment.silent(duration=1500)
    silence1500sec2 = AudioSegment.silent(duration=1500)

    combined_audio = originalAudio + silence1500sec + englishAudio + silence1500sec2

    fadeOutDur = 2000  # in milliseconds
    combinedSound = combined_audio.fade_out(fadeOutDur)

    return combinedSound


def CreateAudio(words: list[Word], parentFolder='Words'):
    for word in words:
        combined_audio = __CreateCombinedAudio(word)
        combined_audio.export(
            f'{parentFolder}\\{word.Original}_{word.Translated}.mp3', format="mp3")
