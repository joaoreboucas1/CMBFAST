"""
    A Python wrapper around CMBFAST
    Author: João Rebouças, January 2026
"""

from dataclasses import dataclass
import subprocess
import numpy as np
import matplotlib.pyplot as plt

from time import perf_counter

@dataclass
class Config():
    mode: int = 0 # CMB (0), transfer functions (1) or lensed Cls (2)
    lmax: int = 2500
    ketamax: int = 3000
    w: float = -1
    Omega_b: float = 0.049
    Omega_c: float = 0.27
    Omega_de: float = 0.681
    Omega_nu: float = 0
    H0: float = 67
    TCMB: float = 2.7255
    YHE: float = 0.24
    N_nu_ur: float = 3.04
    N_nu_mass: int = 0
    g_star: float = 10.75
    recomb_mode: int = 1 # 0 for Peebles, 1 for RECFAST
    reion_mode: int = 0
    dofs: int = 0
    ns: float = 0.96
    out_file: str = "cls.dat"
    ic_type: int = 1
    jl_file: str = "jl.dat"

    def format(self):
        return f"""{self.mode}
{self.lmax} {self.ketamax}
1
{self.w}
{self.Omega_b} {self.Omega_c} {self.Omega_de} {self.Omega_nu}
{self.H0} {self.TCMB} {self.YHE} {self.N_nu_ur} {self.N_nu_mass} {self.g_star}
{self.recomb_mode}
{self.reion_mode}
{self.dofs}
1 {self.ns} 0
{self.out_file} 
{self.ic_type}
./cmbfast4.5.1/{self.jl_file}

"""
    
    def run(self):
        start = perf_counter()
        subprocess.run(
            ["./cmbfast4.5.1/cmb"],
            input=self.format().encode(),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"CMBFAST took {perf_counter()-start} seconds")

if __name__ == "__main__":
    c = Config()
    c.run()

    ell, cl_tt, cl_ee, cl_te = np.loadtxt(c.out_file, unpack=True)

    fig, ax = plt.subplots()
    ax.plot(ell, cl_tt)
    fig.canvas.manager.set_window_title("Hello from CMBFAST!")
    fig.text(
        0.5, 0.5,                    # Center
        "CMBFAST EXAMPLE",
        fontsize=40,
        fontweight="bold",
        color="gray",
        alpha=0.3,
        ha="center",
        va="center",
        rotation=30
    )
    ax.set_xlabel("$\\ell$", fontsize=20)
    ax.set_ylabel("$C_\\ell^{TT}$", fontsize=20)
    plt.show()
