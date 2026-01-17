"""
    A wrapper around CMBFAST
"""

from dataclasses import dataclass
import subprocess
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class Config():
    mode: int = 0 # CMB (0), transfer functions (1) or lensed Cls (2)
    lmax: int = 1500
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
{self.jl_file}"""
    
    def run(self):
        subprocess.run(
            ["./cmb"],
            input=self.format().encode(),
        )

if __name__ == "__main__":
    c = Config()
    c.run()

    ell, cl_tt, cl_ee, cl_te = np.loadtxt(c.out_file, unpack=True)

    plt.plot(ell, cl_tt)
    plt.show()
