import argparse


def fractional_to_integer(value: int):
    return float(value) / (2 ** 32)

parser = argparse.ArgumentParser()
parser.add_argument("fractional", help="a fractional part of number", type=int)
args = parser.parse_args()

print(fractional_to_integer(args.fractional))
