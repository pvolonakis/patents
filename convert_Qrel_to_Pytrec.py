import re

def clean_qrels_file(input_path, output_path):
    """
    Καθαρίζει το αρχείο Prior_art_qrels.txt και το αποθηκεύει σε μορφή TREC format
    για χρήση με pytrec_eval: <query_id> 0 <doc_id> <relevance>
    """
    with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue

            parts = re.split(r'[\t\s]+', line)
            if len(parts) == 4:
                query_id, zero, doc_id, relevance = parts
                outfile.write(f"{query_id} {zero} {doc_id} {relevance}\n")
            else:
                print(f"Αγνοείται γραμμή με λάθος μορφή: {line}")

# ---------------------------
# Ρυθμίσεις αρχείων εδώ:
# ---------------------------
input_path = 'WPI_60K/test_topics/Prior_art_qrels.txt'
output_path = 'WPI_60K/test_topics/prior_eval.txt'

# Εκτέλεση μετατροπής
clean_qrels_file(input_path, output_path)