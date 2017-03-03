#Hetero-Mark
A Benchmark Suite for Heterogeneous System Computation
Note: This benchmark has been compiled.

## Applications
The suite is in development. All outputs show the time it takes to run
the application without overheads such as data transfer time etc.

* Advanced Encryption Standard (AES) - The program takes plaintext as input and encrypts it using a given
encryption key. Our implementation uses a key size of 256 bits. The
AES algorithm is comprised of many rounds, that ultimately turn
plaintext into cipher-text. Each round has multiple processing steps
that include AddRoundKey, SubBytes, ShiftRows and MixColumns. Key bits
 must be expanded using a precise key expansion schedule.

* Finite Impulse Response (FIR) - FIR filter produces an impulse response of finite duration. The impulse
 response is the response to any finite length input. The FIR filtering
 program is designed to have the host send array data to the FIR kernel
 on the OpenCL device. Then the FIR filter is calculated on the device,
 and the result is transferred back to the host.

* KMeans - k-means clustering is a method of vector quantization, originally from
 signal processing, that is popular for cluster analysis in data mining.
 k-means clustering aims to partition n observations into k clusters in
 which each observation belongs to the cluster with the nearest mean,
 serving as a prototype of the cluster. In this implementation, we have
 varied the number of objects of 34 features and put them into 5 clusters.
 The input file contains features and attributes.

* Page Rank - PageRank is an algorithm used by Google Search to rank websites in their
 search engine results. It is a link analysis algorithm and it assigns a
 numerical weighting to each element of a hyperlinked set of documents,
 such as the World Wide Web, with the purpose of "measuring" its relative
 importance within the set. So the computations are representatives of graph
 based applications.

* Histogram - Computes a moderately large, 2-D saturating histogram with a maximum bin count of 255. Input datasets represent a silicon wafer validation application in which the input points are distributed in a roughly 2-D Gaussian pattern.
