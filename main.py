import os
from typing import List

from docxcompose.composer import Composer
from docx import Document


def get_all_word_files() -> List[str]:
    files = os.listdir()
    files = [
        file for file in files if file.endswith('.docx')
    ]
    files.sort()
    return files


def merge(filenames_list):
    docs = [
        Document(filename) for filename in filenames_list
    ]
    composer = Composer(docs[0])
    for doc in docs[1:]:
        doc.add_page_break()
        composer.append(doc)
    composer.save('output.docx')


def main():
    filenames_list = get_all_word_files()
    merge(filenames_list)


if __name__ == '__main__':
    main()
