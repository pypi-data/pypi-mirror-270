import os
import argparse
import requests
from bs4 import BeautifulSoup

class NCBIGeneInfo:
    def __init__(self):
        pass

    def fetch_gene_info(self, gene_list):
        geneids = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        gene_dict_path = os.path.join(current_dir, "NCBI_gene_dict")
        with open(gene_dict_path) as ncbi_genes:
            for line in ncbi_genes:
                line = line.strip().split(":")
                for gene in gene_list:
                    if line[0] == gene:
                        geneids.append(line[1])
        for item in geneids:
            url = f"https://www.ncbi.nlm.nih.gov/gene/{item}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            symbol = soup.find("dt", text=' Official\n                         Symbol')
            if symbol:
                symbol = symbol.find_next_sibling("dd").text.strip()
            summary = soup.find("dt", text="Summary")
            if summary:
                summary = summary.find_next_sibling("dd").text.strip()
            gene_type = soup.find("dt", text="Gene type")
            if gene_type:
                gene_type = gene_type.find_next_sibling("dd").text.strip()
            official_full_name = soup.find('dt', text=' Official\n                         Full Name')
            if official_full_name:
                official_full_name = official_full_name.find_next_sibling("dd").text.strip()
            location = soup.find('dt', text='Location: ').find_next_sibling('dd').text.strip()
            print("Gene Symbol: ", "\t","\t", symbol[:-16])
            print("Gene ID: ", "\t","\t", item)
            print("Gene Type: ", "\t","\t", gene_type)
            print("Official Full Name: ", "\t", official_full_name[:-16])
            print("Location: ", "\t","\t",location)
            print("Summary: ","\t","\t", summary)
            print("------------------------------ \n")

def main():
    parser = argparse.ArgumentParser(description="Retrieve information about genes from NCBI.")
    parser.add_argument("genes", nargs="+", help="List of gene symbols separated by spaces")
    args = parser.parse_args()
    ncbi = NCBIGeneInfo()
    ncbi.fetch_gene_info(args.genes)

if __name__ == "__main__":
    main()

