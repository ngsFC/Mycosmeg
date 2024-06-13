import re

# Function to compute the reverse complement of a DNA sequence
def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, base) for base in reversed(seq))

def convert_fasta_to_two_line(file_path):
    with open(file_path, 'r') as file:
        sequences = {}
        identifier = ''
        for line in file:
            if line.startswith('>'):
                identifier = line[1:].strip()
                sequences[identifier] = ''
            else:
                sequences[identifier] += line.strip()
    return sequences

def find_pattern(sequences, pattern):
    rev_comp_pattern = reverse_complement(pattern)  # Use reverse complement
    matches = []
    for identifier, sequence in sequences.items():
        for match in re.finditer(pattern, sequence):
            matches.append((identifier, match.start() + 1, match.end(), sequence[match.start():match.end()], "Forward"))
        for match in re.finditer(rev_comp_pattern, sequence):
            matches.append((identifier, match.start() + 1, match.end(), sequence[match.start():match.end()], "Reverse Complement"))
    return matches

def main():
    fasta_file_path = input("Enter the path to your FASTA file: ")
    pattern = input("Enter the DNA sequence pattern (use '.' to represent any nucleotide): ")
    output_file_path = input("Enter the path for the output BED file: ")

    sequences = convert_fasta_to_two_line(fasta_file_path)
    matches = find_pattern(sequences, pattern)

    with open(output_file_path, 'w') as output_file:
        for identifier, start, end, matched_seq, orientation in matches:
            output_file.write(f"{identifier}\t{start}\t{end}\t{matched_seq}\t{orientation}\n")

    print(f"Total number of patterns found: {len(matches)}")

if __name__ == "__main__":
    main()

