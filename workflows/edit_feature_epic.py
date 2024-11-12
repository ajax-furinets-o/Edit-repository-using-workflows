import re
import argparse


def main(epic_name: str):
    file_path = "/home/runner/work/Edit-repository-using-workflows/Edit-repository-using-workflows/workflows/feature_file.feature"

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    modified_content = re.sub(r'@epic:\w+', f"@epic:{epic_name}", content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--epic-name", type=str)
    main(parser.parse_args().epic_name)
