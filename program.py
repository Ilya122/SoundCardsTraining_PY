import AudioCreator

originalLang = ''
translatedLang = ''
words = {
    'word': 'word2'
}
folderToSaveTo = 'SoundCards'

words_list: list[AudioCreator.Word] = [AudioCreator.Word(Original=k, OriginalLang=originalLang,
                                                         Translated=v, TranslatedLang=translatedLang) for k, v in words.items()]

AudioCreator.CreateAudio(words_list, folderToSaveTo)
