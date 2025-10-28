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

- N-gram overlap: A method for finding a set of terms that are likely to have a small edit distance from a misspelled query term. (Trigram)
- Soundex: algorithm for indexing terms that sound the same.

- Suffix Arrays: a sorted array of all suffixes of a given string. allows us to search for a given substring.

- Permuterm Indexes: variouis rotations of each term all link to an original vocabulary term in the dictionary.
- Wildcards: special characters used to represent unknown characters in search queries.

- Burrows-Wheeler Transform (BWT): an algorithm that transform and compresses a given string to group similar chars togheter. ("banana" -> "annbaa")

- Edit Tables: a data structure that stores the amount of instructions of every prefix of two string to make string a into string b (edit distance).
- Edit Distances: Given two s trings, the minimum number of operations to convert one to the other (insert, delete, replace, transpose).
- Weight in distance: A weight assigned to each operation for editing distance to reflect real world errors.

- Tries: a type of graph that uses the prefix of previously entered terms to store new ones.
- Aho-Corasick Algorithm: an algorithm that finds all terms within a given buffer using links between internal nodes.

TOPIC: Classification

- Support Vector Machines: a machine learning algorithm used in classification and regression tasks. Finds the best hyperplane that seperates the data into classes.
- Margin, Embedding Vectors, Supporting Vectors, Features, Hyperplane, Desicion Boundries

- Linear SVM: uses a straight decision boundry (line/hyperplane)
- Kernels: functions that compute similarity between data points and lets SVM's separate data with curves (non-linear).
- Non-Linear SVM: uses kernels to create curved decision boundries. Used with data classes that cant be separated with a straight line.

- Ad-hoc Query: Traditional query for search engines.
- Standing Query: continous query that are stored and automatically executed against new incoming documents.

- Classification: assigning data to predefined categories based on their features. Supervised learning from labeled training data, then predict the category for new items.
- Text Classification: classification applied specifically to text documents, used for spam detection, topic categorization, language detection, etc.

- Filtering: classification based on binary decisions (true/false)
Vertical Search Engine
- Labeling: assigning categories' names/tags to training data so that the supervised learning algorithms can learn from examples.
- Feature Selection: the process of choosing the most relevant and informative features from the data while removing irrelevant ones.

- Supervised Learning Algorithm: machine learning algorith that learns from labeled training data (input-output pairs) to preict outputs for new data.

- Statistical Test Classification: uses statistical and probabilistic models to categorize text based on patterns learned from training data (Naive bayes, SVM, Logistic regression).
- Naive Bayes: assumes features are independent of each other and calculates the probability of each class given the features and assignes the highest probability class to the dataset.

- Vector Space Classifiers: classification methods that represent documents as vectors in a multi dimentional space and classifies based on distance/similarity between vectors.
- Rocchio Classifier: creates a centroid for each class by averaging all training vectors in that class, then classifies new documents by finding the nearest centroid.
- k-Nearest Neighbors (k-NN): finds the k closest training examples to the new document, then classifies based on majority vote of those k neighbors.

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

- Bloom Filters: a probabilistic data structure for checking set membership (var "in"/"not in" set), very space efficient.

- Neural Networks: Interconnected neurons organized in layers (input -> hidden -> output layer)each connection between neurons (nodes) has an independent weight, the strength of the connection.

- Embeddig Vectors: the vectors for numerical representations of data points in a multi-dimentional space where similar items are positioned close togheter. Converting data to vectors via vectorization and Mapping. ex: Embedding vectors = [[1,5,3,6,3]] where [1,5,3,6,3] is the embedding vector.

