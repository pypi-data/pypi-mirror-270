<h1 align="center">PACMAN</h1>

<h4 align="center">

</h4>              

A **P**artial **A**tomic **C**harge Predicter for Porous **Ma**terials based on Graph Convolutional Neural **N**etwork (**PACMAN**)   

[![Requires Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg?logo=python&logoColor=white)](https://python.org/downloads) [![Zenodo](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.10822403-blue)](https://doi.org/10.5281/zenodo.10822403)  [![MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/sxm13/PACMAN/LICENSE.txt) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sxmzhaogb@gmail.com) [![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)]() [![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)]()          


# Usage

```sh      
from PACMANCharge import pmcharge
PACMaN.predict(cif_file="./test/Cu-BTC.cif",model_name="MOF",charge_type="DDEC6",digits=10,atom_type=True,neutral=True)
```

* cif_file: cif file (without partial atomic charges) **[absolute path]**                                          
* model_name: what type of structure is yours **[MOF/COF]**                                           
* charge_type: what type of charge do you want to assignment **[DDEC6/Bader/CM5]**                             
note: for COF, just can use DDEC6 charge
* digits: digits of charge (recommond use 6)
note: ML models were trained on 6 digit dataset
* atom_type: keep the same partial atomic charge for the same atom types (based on the similarity of partial atomic charges) **[True/False]**                             
* neutral: keep the net charge is zero. We use "mean" method to neuralize the system. Please refer to the manuscript about the method **[True/False]**                                                  

# Website & Zenodo
PACMAN-APP[link](https://gcn-charge-predicter-mtap.streamlit.app/)       
DOWNLOAD full code and dataset[link](https://zenodo.org/records/10822403) But we will not update new vesion in Zenodo.            

# Reference
If you use PACMAN Charge, please cite [this paper]:
```
@article{,
    title={PACMAN: A Robust Partial Atomic Charge Predicter for Nanoporous Materials using Crystal Graph Convolution Network},
    journal={Journal of Chemical Theory and Computation},
    author={Zhao, Guobin and Chung, Yongchul},
    year={2024},
}
```

# Bugs

If you encounter any problem during using ***PACMAN***, please email ```sxmzhaogb@gmail.com``` or create "issues".                 

 
 
**Group:**   [Molecular Thermodynamics & Advance Processes Laboratory](https://sites.google.com/view/mtap-lab/home?authuser=0)                                
