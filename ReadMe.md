# SoundCards

The sound cards module was created to easily generate sound cards for driving or when we aren't able to focus on writing.  


## Simple usage
Use the [Program](program.py) to create the audio list using the ``gTTS`` module.  
So it supports only languages supported by ``gTTS``.  

## For example:

```python
import AudioCreator

originalLang = 'jp'
translatedLang = 'en'
words = {
    '時間': 'time',
    '友達': 'friend',
    '家': 'house'
}

folderToSaveTo = 'SoundCards'

words_list: list[AudioCreator.Word] = [AudioCreator.Word(Original=k, OriginalLang=originalLang,
                                                         Translated=v, TranslatedLang=translatedLang) for k, v in words.items()]

AudioCreator.CreateAudio(words_list, folderToSaveTo)
```