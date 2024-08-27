# Illumio-Assessment

## Overview

This project is a Python program designed to parse flow logs and map each log entry to a tag based on a lookup table. The lookup table specifies the `(dstport, protocol)` combinations that determine the appropriate tag. The program outputs a count of matches for each tag and a count of occurrences for each port/protocol combination.

## Features

- **Flow Log Parsing**: Reads a flow log file and extracts the destination port and protocol from each entry.
- **Tag Mapping**: Uses a lookup table to map each `(dstport, protocol)` combination to a tag.
- **Counting Occurrences**: Outputs the number of occurrences for each tag and the number of occurrences for each `(dstport, protocol)` combination.
- **Untagged Logs**: Logs that do not match any entry in the lookup table are counted as "Untagged."

## Requirements

- Python 3.x
- The following Python modules:
  - `csv`
  - `collections`

## Files

- `input.csv`: A file containing flow log data (version 2 only).
- `lookup_table.csv`: A CSV file defining the `dstport`, `protocol`, and `tag` mappings.
- `main.py`: The main Python script that runs the program.

## Usage

1. **Prepare the input files**:
   - Ensure `input.csv` contains your flow logs in the specified format.
   - Ensure `lookup_table.csv` contains the correct mappings for `dstport`, `protocol`, and `tag`.

2. **Run the Program**:
   - Execute the `main.py` script:
     ```bash
     python main.py
     ```
   - The program will output the count of matches for each tag and the count of occurrences for each port/protocol combination.

3. **Output Example**:
   - The output will be printed in the terminal:
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
- The protocol numbers are mapped as follows:
  - `6` → `tcp`
  - `17` → `udp`
  - `1` → `icmp`
- Logs that do not match any entry in the lookup table are considered "Untagged."

## Customization

- **Adding New Tags**: Update the `lookup_table.csv` file with new `(dstport, protocol)` combinations and their corresponding tags.
- **Changing Input Files**: Modify the file paths in the `main.py` script to use different input files if necessary.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or support, please reach out to [Your Name] at [Your Email].
