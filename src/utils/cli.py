import argparse as argp
import pandas as pd
import sys

from pathlib import Path
from src.data.transform import (
    clean_html_tags,
    clean_text_basic,
    clean
)

sys.path.append(str(Path(__file__).parent.parent))
_input_dir = "data/raw/"
_output_dir = "data/processed/"
_input_file = "ml_ozon_counter_test.csv"
_output_file = "ml_ozon_counter_test_processed.csv"


class CLI:
    def __init__(self):
        self.parser = argp.ArgumentParser(description="Текстовые утилиты очистки")
        self.subparsers = self.parser.add_subparsers(dest="command", help="Команды")

        self.COMMANDS = {
            "clean-html": self._clean_html_tags,
            "clean-text": self._clean_text_basic,
            "clean": self._clean
        }
        self.init_commands()

    def init_commands(self):
        #---------------------------------------------
        self.clean_parser = self.subparsers.add_parser(
            "clean", 
            help="Полная очистка от HTML тегов и базовая очистка"
        )
        self.clean_parser.add_argument(
            "--input-file",
            default=_input_file,
            help="Файл с исходными данными"
        )
        self.clean_parser.add_argument(
            "--output-file",
            default=_output_file,
            help="Файл для обработанных данных"
        )

        #---------------------------------------------
        self.html_parser = self.subparsers.add_parser(
            "clean-html", 
            help="Очистить HTML теги из текста"
        )
        self.html_parser.add_argument(
            "--input-file",
            default=_input_file,
            help="Файл с исходными данными"
        )
        self.html_parser.add_argument(
            "--output-file",
            default=_output_file,
            help="Файл для обработанных данных"
        )
        
        #---------------------------------------------
        self.text_parser = self.subparsers.add_parser(
            "clean-text", 
            help="Базовая очистка текста"
        )
        self.text_parser.add_argument(
            "--input-file",
            default=_input_file,
            help="Файл с исходными данными"
        )
        self.text_parser.add_argument(
            "--output-file",
            default=_output_file,
            help="Файл для обработанных данных"
        )

    def parse_command(self):
        return self.parser.parse_args()

    def handle_command(self, args):
        try:
            result = self.COMMANDS[args.command]
        except:
            self.parser.print_help()
            sys.exit(1)
        else:
            result(args)

    def _clean_html_tags(self, args):
        input_path = Path(_input_dir) / args.input_file
        output_path = Path(_output_dir) / args.output_file
        
        print(f"Загрузка файла: {input_path}")
        dataframe = pd.read_csv(input_path)
        
        text_columns = dataframe.select_dtypes(include=['object', 'string']).columns.tolist()
        
        print("Очистка HTML тегов во всех текстовых колонках...")
        for column in text_columns:
            dataframe[column] = dataframe[column].apply(clean_html_tags)
            print(f"{column} - очищена")
        
        dataframe.to_csv(output_path, index=False)
        print(f"Файл сохранен: {output_path}")
        print(f"Обработано колонок: {len(text_columns)}")

    def _clean_text_basic(self, args):
        ...

    def _clean(self, args):
        ...

    def run(self):
        args = self.parse_command()
        self.handle_command(args)


def main():
    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main()
