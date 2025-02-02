import argparse
import subprocess


def main(args):

    file = args.file

    subprocess.run(["iverilog", "-o", f"{file}.vvp", f"{file}.v"])
    subprocess.run(["vvp", f"{file}.vvp"])
    subprocess.run(["gtkwave", "-f", f"{file}.vcd"])


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Runs commands to run testbench and generate .vcd file")
    parser.add_argument(
        '-f',
        '--file',
        help="verilog testbench file to run, without extension"
    )
    args = parser.parse_args()
    main(args)

