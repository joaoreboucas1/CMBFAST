# CMBFAST

> [!Note]
> This repository contains the `CMBFAST` code version 4.5.1, written by Uros Seljak and Matias Zaldarriaga. The code was obtained from a repository from Floor Terra, a project to implemnt a Python 2 wrapper for CMBFAST. I do not claim any ownership of the code in this repository. All rights are reserved to the original authors, see `LICENSE`.

CMBFAST is an implementation of the algorithm from [Seljak & Zaldarriaga 1996](https://arxiv.org/abs/astro-ph/9603033) to compute the CMB angular power spectra. The advantage of this algorithm over direct integration is that the power spectra can be predicted with great precision even truncating the neutrino and photon hierarchy at low multipoles. This avoids the numerical integration of thousands (of the order of $\ell_max$, the maximum desired multipole) of differential equations. This algorithm has made possible to extract cosmological information from CMB maps, which by the 1990's were becoming increasinglly precise to subdegree scales. In 1996, CMBFAST was the basis for [CAMB](https://github.com/cmbant/CAMB), one of the current state-of-the-art Einstein-Boltzmann solvers, written by Antony Lewis. Therefore, CMBFAST code has historical importance in cosmology.

Furthermore, the CAMB code consists of approximately 30k lines of modern Fortran code. Much of the code deals with Python interfacing and parallelism. While 30k lines may not be a big amount by the software engineering standards, it is a huge amount for physicists, which mostly do not have experience in Fortran, may lack expertise in programming, and are also involved in scientific research and academic activities. CAMB is the culmination of 30 years of hard maintenance work, and it has the most varied use cases in astrophysics and cosmology. Even advanced users with expertise in cosmological perturbation theory may not understand all of CAMB's inner workings. Older and simpler codes, such as CMBFAST, are more direct in their purposes, and have significantly less lines of code. Because of this, CMBFAST can serve as a reference on the implementation of Einstein-Boltzmann solvers, making the code's functionality more transparent.

CMBFAST has an [official website](https://lambda.gsfc.nasa.gov/toolbox/cmbfast_overview.html) hosted by NASA. However, the source code cannot be downloaded, and the website prompts users to "investigate CAMB in its place." I could only find the original source code from a [repository from Floor Terra](https://github.com/floort/py-cmbfast) implementing a Python 2 wrapper for CMBFAST. I thought that maintaining some repository would make it easier to reference and research the source code as a didactical tool.

## Compilation

The user can compile the code with `./configure` and `make` (after adjusting the `Makefile` as described below). The code contains very small changes in order to make it compile properly in modern computers. These changes are the following:
- `configure`: remove the fortran compiler check: it used to check for the existence of `g77`, but it was superseded by `gfortran`;
- `Makefile`: add `gfortran` as the fortran compiler and `-std=legacy` to its flags;
- `jlgen.F`: in line 116, the main subroutine was unnamed, I set it to `main`;
- `recfast.f`: in line 500, there are declarations of many `double` variables. However, in the Fortran 77 standard, the source code could only be contained between columns 7-72. The declaration in line 500, however, used to overflow the upper limit, so I just moved `d_PPB` to the following line.

## Usage

Before running CMBFAST for the first time, the user needs to generate Bessel function tables with the binaries `jlgen` and `jlens`. The output paths are conventionally `jl.dat` and `jlens.dat` respectively, but this can be modified by the user.

After compilation, the user can run the binary with `./cmb`, where cosmological parameters are input manually. These can also be input from a formatted file, see `example.in`