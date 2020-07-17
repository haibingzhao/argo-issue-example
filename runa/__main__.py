import argparse
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
    parser.add_argument("--condition_b1", help="condition_b1 path")
    parser.add_argument("--condition_b2", help="condition_b2 path")
    args = parser.parse_args()

    Path(args.condition_b1).parent.mkdir(parents=True, exist_ok=True)
    Path(args.condition_b1).write_text('true')

    Path(args.condition_b2).parent.mkdir(parents=True, exist_ok=True)
    Path(args.condition_b2).write_text('false')
