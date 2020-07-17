import argparse
import os
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
    parser.add_argument("--result_b1", help="result_b1 path")
    parser.add_argument("--result_b2", help="result_b2 path")
    args = parser.parse_args()

    print(f'result_b1 path = {args.result_b1}')
    print(f'result_b2 path = {args.result_b2}')

    if os.path.exists(args.result_b1):
        print(f'result_b1 = {Path(args.result_b1).read_text()}')

    if os.path.exists(args.result_b2):
        print(f'result_b2 = {Path(args.result_b2).read_text()}')
