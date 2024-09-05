def count_lines(file_path):
    with open(file_path, 'r', encoding='CP949') as f:
        return sum(1 for _ in f)

file_path = 'C:/Users/User/PycharmProjects/kospeach_Project/kospeech/dataset/kspon/transcripts.txt'
print(f"Total lines: {count_lines(file_path)}")

import re


def detect_delimiter(file_path):
    with open(file_path, 'r', encoding='CP949') as f:
        sample_line = f.readline()

    # 구분자 패턴을 정규 표현식으로 감지
    if ',' in sample_line:
        return ','
    elif '\t' in sample_line:
        return '\t'
    elif ';' in sample_line:
        return ';'
    else:
        return None


def process_file(file_path):
    delimiter = detect_delimiter(file_path)
    if delimiter is None:
        print("구분자를 찾을 수 없습니다.")
        return

    print(f"Detected delimiter: {delimiter}")
    with open(file_path, 'r', encoding='CP949') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.split(delimiter)
        print(parts)


file_path = 'C:/Users/User/PycharmProjects/kospeach_Project/kospeech/dataset/kspon/transcripts.txt'
process_file(file_path)


