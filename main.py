"""
===============================================================================
E. COLI K-12 WHOLE-GENOME BIOINFORMATICS ANALYSIS PIPELINE
Description: Simple, clean Python script for sequence loading, nucleotide 
             counting, GC calculation, transcription, reverse complementation, 
             and codon slicing.
===============================================================================
"""

import collections


# -----------------------------------------------------------------------------
# 1. Genome File Read Karne Ka Function (FASTA Header Skip Functionality)
# -----------------------------------------------------------------------------
def readgenome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            # Lines starting with '>' are FASTA headers; skip them
            if not line[0] == ">":
                genome += line.rstrip().upper()
    return genome


# -----------------------------------------------------------------------------
# 2. File Load Karein Aur Basic Output Print Karein
# -----------------------------------------------------------------------------
file_path = r"C:\Users\Hp\Downloads\sequence.fasta"
genome = readgenome(file_path)

print("=" * 70)
print("       ESCHERICHIA COLI K-12 FULL GENOME BIOINFORMATICS REPORT       ")
print("=" * 70)
print("Genome Length:", len(genome), "base pairs")
print("First 100 bases:", genome[:100])
print("\n")


# -----------------------------------------------------------------------------
# STEP 1: Nucleotide Counting (Dictionary Method & Counter Method)
# -----------------------------------------------------------------------------
print("-" * 70)
print("STEP 1: NUCLEOTIDE COUNTING")
print("-" * 70)

# Dictionary Method
counts = {"A": 0, "C": 0, "G": 0, "T": 0}
for base in genome:
    if base in counts:
        counts[base] += 1

print("Counts Dictionary:", counts)

# Counter Method
counter_results = collections.Counter(genome)
print("Counter Result   :", counter_results)
print("\n")


# -----------------------------------------------------------------------------
# STEP 2: GC Content Calculation (%)
# -----------------------------------------------------------------------------
print("-" * 70)
print("STEP 2: GC CONTENT ANALYSIS")
print("-" * 70)

gc_count = counts["G"] + counts["C"]
total_bases = len(genome)
gc_content = (gc_count / total_bases) * 100

print("GC Base Count :", gc_count)
print("GC Content    :", round(gc_content, 2), "%")
print("\n")


# -----------------------------------------------------------------------------
# STEP 3: Full Genome Transcription (DNA -> mRNA)
# -----------------------------------------------------------------------------
print("-" * 70)
print("STEP 3: FULL TRANSCRIPTION (DNA -> mRNA)")
print("-" * 70)

# Replacing Thymine (T) with Uracil (U) across the full sequence
mrna = genome.replace("T", "U")

print("Total Uracil (U) bases in mRNA:", mrna.count("U"))
print("mRNA Sequence Length          :", len(mrna))
print("mRNA Sample (First 30 bases)  :", mrna[:30])
print("\n")


# -----------------------------------------------------------------------------
# STEP 4: Full Reverse Complement Strand Generation (3' -> 5')
# -----------------------------------------------------------------------------
print("-" * 70)
print("STEP 4: FULL REVERSE COMPLEMENT STRAND (3' -> 5')")
print("-" * 70)

# Watson-Crick Base Pairing rules
complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"}

# Fast Execution using list comprehension and .join()
rev_complement = "".join(
    [complement_map.get(base, base) for base in reversed(genome)]
)

print("Reverse Complement Length         :", len(rev_complement))
print("Reverse Complement (First 30 bases):", rev_complement[:30])
print("\n")


# -----------------------------------------------------------------------------
# STEP 5: Full Genome Codon Slicing (Triplets)
# -----------------------------------------------------------------------------
print("-" * 70)
print("STEP 5: FULL CODON SLICING (Whole Genome)")
print("-" * 70)

# Slicing the genome string into groups of 3 bases
codons = [genome[i : i + 3] for i in range(0, len(genome) - 2, 3)]

print("Total Codons Generated:", len(codons))
print("First 5 Codons Sample :", codons[:5])
print("Last 5 Codons Sample  :", codons[-5:])
print("=" * 70)