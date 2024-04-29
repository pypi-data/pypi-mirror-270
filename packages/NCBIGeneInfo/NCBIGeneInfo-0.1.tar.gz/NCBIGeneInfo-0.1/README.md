**Retrieve information about genes from NCBI.**

# Installation

```r{}
pip install NCBIGeneInfo
```
# Running

```r{}
from NCBIGeneInfo.gene_info import NCBIGeneInfo
ncbi = NCBIGeneInfo()
ncbi.fetch_gene_info(["SLC8A1", "MEIS1", "ASCL2"])

```
