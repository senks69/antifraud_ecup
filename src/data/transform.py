from pathlib import Path
import pandas as pd
import re


def clean_html_tags(text):
    # Удаляем HTML-теги
    if pd.isna(text):
        return 'text'
    clean_text = re.sub(r'<[^>]+>', ' ', text)
    clean_text = re.sub(r'[\r\n]+', ' ',clean_text)
    clean_text = re.sub(r'/', ' ', clean_text)

    # Заменяем множественные пробелы на одинарные
    clean_text = re.sub(r'\s+', ' ', clean_text)

    # Убираем пробелы в начале и конце
    clean_text = clean_text.strip()   

    return clean_text


def clean_text_basic(text):
    return text


def clean(text):
    text = clean_text_basic(text)
    text = clean_html_tags(text)
    return text
