#!/usr/bin/python3
import os
from pathlib import Path
import re
import sys

args = sys.argv


def is_colour(s):
  return True if s[0:7] == '"Colour' else False


def conv_dict(arr):
  d = {}
  for e in arr:
    kp = e.split("=")
    k = int(kp[0][6:9])
    d[k] = kp[1]
  return d


def main():
  if len(sys.argv) != 2:
    print("Usage: conv.py directory")
    sys.exit(1)

  if not os.path.isdir(sys.argv[1]):
    print("{file} not found.".format(file=sys.argv[1]))
    sys.exit(1)

  if not os.path.isdir("tt_theme"):
    os.makedirs("tt_theme")

  target_dir = Path(sys.argv[1])
  output_dir = Path("tt_theme")

  # Use .iterdir() to get everything in the folder
  pattern = re.compile(r"^\d{2}\.\s+([a-zA-Z0-9_\s-]+)\.reg$")

  for file_path in target_dir.iterdir():
    if file_path.is_file():
      match = pattern.match(file_path.name)
      if match:
        script_name = match.group(1).strip()
        print(script_name)

        # Added encoding safeguards for reading Windows .reg files
        with open(
            file_path, "r"
        ) as f:
          elems = [
              s.strip().replace('"', "") for s in f.readlines() if is_colour(s)
          ]

        d = conv_dict(elems)
        arr = [
            d[3],
            d[9],
            d[11],
            d[13],
            d[15],
            d[17],
            d[19],
            d[21],
            d[4],
            d[8],
            d[10],
            d[12],
            d[14],
            d[16],
            d[18],
            d[20],
        ]

        # Use pathlib for cross-platform file paths safely
        output_file =( output_dir / script_name).with_suffix(".ini")
        with open(output_file, "w", encoding="utf-8") as f:
          f.write("[Color Theme]\n")
          f.write("Theme = {}\n".format(script_name))

          f.write("VTColor = 1,1,{0},{1}\n".format(d[0], d[2]))
          f.write("BoldColor = 1,1,{0},{1}\n".format(d[1], d[3]))
          f.write("BlinkColor = 0,0\n")
          f.write("ReverseColor = 0,0\n")
          f.write("URLColor = 0,0\n")
          f.write("ANSIColor = 1,1,{0}\n".format(",".join(arr)))


if __name__ == "__main__":
  main()