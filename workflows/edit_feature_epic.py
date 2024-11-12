import re
import argparse

from pathlib import Path


def main(epic_name: str):
    file_path = "feature_file.feature"

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    modified_content = re.sub(r'@epic:\w+', f"@epic:{epic_name}", content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--epic-name", type=str)
    main(parser.parse_args().epic_name)
