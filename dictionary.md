TOPIC: Strings Galore

- Precision and Recall: "Of all the documents I got back, how many were actually useful?" and "Of all the useful documents that exist, how many did I get back?"

- Inverted Index: For each term t, store a list of all documents that contain t.

- Biword Index: A type of inverted index that treats every consecutive pair of terms like a single term.
- Positional Index: An enhanced inverted index that stores the position of the term within a document as well as the doc id.

- Tokenization: Cut character sequence into word tokens
- Normalization: Map text and query term to same form
- Stemming: We may wish different forms of a root to match ("authorization" -> "authorize")
- Lemmatization: Reduce inflectional forms to base form ("car, cars car's, cars'" -> "car")
- Porter's Algorithm: Commonest algorithm for stemming in English, includes a variety of rules.

- Query optimization: the process of choosing the most efficient execution plan for a search query.
- Proximity Queries: allowes for related terms to appear in results by prioritizing documents and checking mathematical difference to determine wether terms are close.
- Combination Schemes: A mix of indexes to achieve the best trade off between query speed and index size.

- Merging: Intersection finds the commond documents for all terms in the query.
- Skip Pointers: An optimization technique applied to postingslist to speed up merging

- Edit Distances: Given two s trings, the minimum number of operations to convert one to the other (insert, delete, replace, transpose).
- Weight in distance: A weight assigned to each operation for editing distance to reflect real world errors.

- N-gram overlap: A method for finding a set of terms that are likely to have a small edit distance from a misspelled query term. (Trigram)
- Soundex: algorithm for indexing terms that sound the same.

Suffix Arrays
Permuterm Indexes
Wildcards
Burrows-Wheeler Transform
Edit Tables
Tries
Aho-Corasick Algorithm

TOPIC: Classification

Support Vector Machines
Linear SVM
Kernels and Non-Linear SVM
Standing Query
Classification
Text Classification
Filtering
Vertical Search Engine
Statistical Test Classification
Labeling
Feature Selection
Supervised Learning Algorithm
Naive Bayes
Vector Space Classifiers (Rocchio, k-nn)
Evaluation Metrics (Precision and Recall)

TOPIC: Approximate Nearest Neighbours

Voronoi Diagrams
Brute Force
Tree-Based Algorithms
Locality-Sensitive Hashing
Quantization or Clustering-Based Algorithms
Graph-Based Methods
Selection

TOPIC: Compression

Search Engine Query Processing
Chunked Compression
Index Structure Layout
Inverted List Compression Techniques
Var-byte Compression
Rice Coding
Golomb Coding
Gamma and Delta Coding
Simple9 Coding
PFOR-DELTA
Decompression
Index Caching Algorithms

TOPIC: Embedding Techniques

Natural Language Processing
Word Vectors
Singular Value Decomposition
Context Windows
Regularization

TOPIC: Gradient Descent

Loss Functions
Gradient Descent
Parameters/Hyperparameters
Regularization