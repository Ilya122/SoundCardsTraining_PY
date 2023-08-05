import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFormLayout, QLineEdit, QFileDialog, QLabel, QListWidget, QMessageBox
from PyQt6.QtCore import Qt
from AudioCreator import Word, CreateAudio


class AudioCreatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Audio Creator')

        self.layout = QVBoxLayout()

        self.form_layout = QFormLayout()
        self.original_lang_input = QLineEdit()
        self.translated_lang_input = QLineEdit()
        self.original_word_input = QLineEdit()
        self.translated_word_input = QLineEdit()
        self.form_layout.addRow('Original Language:', self.original_lang_input)
        self.form_layout.addRow('Translated Language:',
                                self.translated_lang_input)
        self.form_layout.addRow('Original Word:', self.original_word_input)
        self.form_layout.addRow('Translated Word:', self.translated_word_input)

        self.add_word_button = QPushButton('Add Word')
        self.add_word_button.clicked.connect(self.add_word)

        self.word_list_label = QLabel('Word List:')
        self.word_list = QListWidget()

        self.remove_word_button = QPushButton('Remove Word')
        self.remove_word_button.clicked.connect(self.remove_word)

        self.select_folder_button = QPushButton('Select Folder')
        self.select_folder_button.clicked.connect(self.select_folder)
        self.folder_label = QLabel('No folder selected')

        self.create_audio_button = QPushButton('Create Audio')
        self.create_audio_button.clicked.connect(self.create_audio)

        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.add_word_button)
        self.layout.addWidget(self.word_list_label)
        self.layout.addWidget(self.word_list)
        self.layout.addWidget(self.remove_word_button)
        self.layout.addWidget(self.select_folder_button)
        self.layout.addWidget(self.folder_label)
        self.layout.addWidget(self.create_audio_button)

        self.setLayout(self.layout)

        self.words = []
        self.folder = None

    def add_word(self):
        original_word = self.original_word_input.text()
        original_lang = self.original_lang_input.text()
        translated_word = self.translated_word_input.text()
        translated_lang = self.translated_lang_input.text()

        if original_word and original_lang and translated_word and translated_lang:
            word = Word(original_word, original_lang,
                        translated_word, translated_lang)
            self.words.append(word)
            self.word_list.addItem(
                f'{original_word} ({original_lang}) -> {translated_word} ({translated_lang})')
            self.original_word_input.clear()
            self.translated_word_input.clear()
        else:
            QMessageBox.warning(self, 'Input Error',
                                'Please fill in all fields.')

    def remove_word(self):
        selected_index = self.word_list.currentRow()
        if selected_index >= 0:
            del self.words[selected_index]
            self.word_list.takeItem(selected_index)
        else:
            QMessageBox.warning(self, 'Selection Error',
                                'Please select a word to remove.')

    def select_folder(self):
        self.folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if self.folder:
            self.folder_label.setText(f'Selected Folder: {self.folder}')
        else:
            self.folder_label.setText('No folder selected')

    def create_audio(self):
        if self.words and self.folder:
            CreateAudio(self.words, self.folder)
            QMessageBox.information(
                self, 'Success', 'Audio files created successfully.')
        else:
            QMessageBox.warning(
                self, 'Input Error', 'Please add at least one word and select a folder.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AudioCreatorApp()
    ex.show()
    sys.exit(app.exec())
