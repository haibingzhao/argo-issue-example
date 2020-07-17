from pathlib import Path
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
    parser.add_argument("--type_b", help="type_b")
    parser.add_argument("--result_b", help="result_b path")
    args = parser.parse_args()

    Path(args.result_b).parent.mkdir(parents=True, exist_ok=True)
    Path(args.result_b).write_text(args.type_b)
