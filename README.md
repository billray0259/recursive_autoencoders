# Read the paper inside 682_Final_report.pdf

# Abstract
Our Project improves upon the quality and clarity of images created by autoencoders by training them in a novel
recursive manner. The model is built out of smaller
stacked models that share layers. The clarity of these images was also slightly improved using batch normalization, where batch normalization layers were shared between corresponding encoder and decoder layers. These
training methods produced models that recreated clearer
images with a slightly lower reconstruction error than an
autoencoder trained end to end with the same architecture
but failed to produce new face images when used on a
variational autoencoder.

<p align="center">
  <img src="https://github.com/billray0259/recursive_autoencoders/blob/main/figures/7_384.png?raw=true" alt="Stacked vs Recursive autoencoders"/>
</p>

# This is just projects notes we wrote to each other that I'm leaving here for some reason


Need to do:
* Make recursive autoencoder variational


No Batch norm
Shared Batch norm
Non-shared Batch norm

Non-Variational
Variational

Stacked
Recursive


Things that already work:
* Stacked
* Recursive
* Shared batch norm recursive
* Shared batch norm stacked
* Stacked Variational

Easy
* Non-shared batch norm recursive
* Non-shared batch norm stacked
* Testing suite

Medium
* Recursive Variational
* Inception Score

Get data on:
* Stacked
* Stacked with non-shared batch norm

Data
* Parameter usage
* Train time
* Reconstruction error
* (Inception score eventually)

Namimg Schema:
* V - variational
* SB - Shared Batch Norm, NB - Normal Batch Norm
* S - Stacked, R - Recursive
* \# - layers
* \# - coding size
