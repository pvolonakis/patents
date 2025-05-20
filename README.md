Project Summary: Information Retrieval with Pyserini (BM25) and pytrec_eval.
This project focuses on building an information retrieval system using the WPI 60K dataset, the Pyserini toolkit for indexing and retrieval, and pytrec_eval for evaluating search performance.

Indexing Phase:
The first step involves processing the WPI 60K dataset to extract relevant fields required for indexing. After reading the documentation, Pyserini is installed and used to create indexes from the cleaned and structured data. These indexes enable efficient document retrieval based on user queries.

Retrieval Phase:
Test topics are processed to formulate search queries. These queries are executed against the previously built indexes using Pyserini's retrieval methods. The results from each query are stored in a standard TREC format for later evaluation.

Evaluation Phase:
To assess the quality of the search results, the pytrec_eval library is installed and used. It computes standard information retrieval metrics such as Precision, Recall, F1-score, MAP, and nDCG. The final step involves analyzing and reporting the performance of the retrieval system based on these metrics.
