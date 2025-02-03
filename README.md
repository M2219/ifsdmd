# IFS-DMD

<p align="center">
  <h1 align="center">Dynamic Mode Decomposition and Koopman Operator for Iterated Function Systems</h1>
  <p align="center">
    Ramen Ghosh, Mahmoud Tahmasebi, Marion McAfee
  </p>
  <h3 align="center"><a href="https://ieeexplore.ieee.org/document/10284085">Paper</a>
  <div align="center"></div>
</p>

This repository contains predicting an iterated function system generated by the following logistic maps on [0, 1] and probabilities using Higher Order Dynamic Mode Decomposition:

![alt text](ifs.png)

# Requirements

* pydmd
* numpy 
* scipy

# Run

Set initial condition inside onedim_dmd.py and

python onedim_dmd.py


Results for initial condition, x=0.5

<img
  src="resutls.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
