#Illumio Technical Assessment for Dylan Hu
'''
Used the following documentation
https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html
https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

Assumptions:
1) Following the protocol numbers documentation I found this mapping which will be used when creating the tag counts {6: 'tcp', 17: 'udp', 1: 'icmp'}
'''
import csv
from collections import defaultdict

# Function to parse flow logs
def parse_flow_logs(flow_logs_file):
    flow_logs = []
    with open(flow_logs_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            dstport = int(parts[6])   # 6th column is dstport
            protocol = int(parts[7])  # 7th column is protocol
            flow_logs.append((dstport, protocol))
    return flow_logs

#Function to parse the lookup table
def parse_lookup_table(lookup_table_file):
    lookup = {}
    with open(lookup_table_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            dstport = int(row[0])
            protocol = row[1]
            tag = row[2]
            lookup[(dstport, protocol)] = tag
    return lookup
    
def tag_flow_logs(flow_logs, lookup):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    protocol_map = {6: 'tcp', 17: 'udp', 1: 'icmp'}  # Common protocol number to name mapping

    for dstport, proto_num in flow_logs:
        protocol = protocol_map.get(proto_num, 'unknown')
        tag = lookup.get((dstport, protocol), "Untagged")
        tag_counts[tag] += 1
        port_protocol_counts[(dstport, protocol)] += 1
    print('Tag Counts', tag_counts)
    print('Port Protocol Counts', port_protocol_counts)
    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write("Tag Counts:\nTag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")
        
        file.write("\nPort/Protocol Combination Counts:\nPort,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")

def main(flow_logs_file, lookup_table_file, output_file):
    # Parse input files
    flow_logs = parse_flow_logs(flow_logs_file)
    lookup = parse_lookup_table(lookup_table_file)
    
    # Tag the flow logs
    tag_counts, port_protocol_counts = tag_flow_logs(flow_logs, lookup)
    
    # Write the output
    write_output(tag_counts, port_protocol_counts, output_file)

# Example usage
main('input.txt', 'lookup_table.csv', 'output.csv')
