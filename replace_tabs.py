import argparse


parser = argparse.ArgumentParser()
parser.add_argument("path", help="a path to file for replacing tabs by spaces", type=str)
args = parser.parse_args()


def read_file(path: str):
    try:
        with open(path, "r") as file_handler:
            return file_handler.readlines()
    except IOError as err:
        print(err)


def replace_tabs(file: str):
    new_text = str()

    for line in file:
        new_text += line.replace("\t", (" " * 4))

    return new_text


def write_file(path: str, text: str):
    try:
        with open(path, "w") as file_handler:
            file_handler.write(text)
    except IOError as err:
        print(err)


old_file = read_file(args.path)
new_file = replace_tabs(old_file)

write_file(args.path, new_file)
