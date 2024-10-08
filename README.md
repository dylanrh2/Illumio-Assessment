# Illumio-Assessment

## Overview

This project is a Python program designed to parse a file containing flow log data and maps each row to a tag based on a lookup table. The lookup table is defined as a csv file, and it has 3 columns, `dstport, protocol, tag`. The dstport and protocol combination decide what tag can be applied. The program outputs a count of matches for each tag and a count of occurrences for each port/protocol combination.

## Features

- **Flow Log Parsing**: Reads a flow log file and extracts the destination port and protocol from each entry.
- **Tag Mapping**: Uses a lookup table to map each `(dstport, protocol)` combination to a tag.
- **Counting Occurrences**: Outputs the number of occurrences for each tag and the number of occurrences for each `(dstport, protocol)` combination.
- **Untagged Logs**: Logs that do not match any entry in the lookup table are counted as "Untagged."

## Requirements

- Python 3.x
- The following Python modules:
  - `csv`
  - `collections` from `defaultdict`

## Files

- `input.txt`: A file containing flow log data (version 2 only).
- `lookup_table.csv`: A CSV file defining the `dstport`, `protocol`, and `tag` mappings.
- `main.py`: The main Python script that runs the program.

## Usage

1. **Prepare the input files**:
   - Ensure `input.txt` contains your flow logs in the specified format.
   - Ensure `lookup_table.csv` contains the correct mappings for `dstport`, `protocol`, and `tag`.
   - Compare this example with `example_output.csv` to ensure it looks the same.

2. **Run the Program**:
   - Execute the `main.py` script:
     ```bash
     python main.py
     ```
   - The program will output the count of matches for each tag and the count of occurrences for each port/protocol combination.

3. **Output Example**:
   - The output will be stored in an output file `output.csv`:
     ```
     sv_P1: 2
     sv_P2: 2
     sv_P4: 1
     sv_P5: 2
     email: 3
     Untagged: 9
     ```

## Assumptions

- The flow log data is version 2 and follows the specified format.
- The lookup table is a CSV file with the columns `dstport`, `protocol`, and `tag`.
- The protocol numbers are mapped as follows from [AWS](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml):
  - `6` → `tcp`
  - `17` → `udp`
  - `1` → `icmp`
- Logs that do not match any entry in the lookup table are considered "Untagged".

