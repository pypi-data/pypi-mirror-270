import os
import urllib.request
import gzip
import py3Dmol

class PDBViewer:
    def __init__(self):
        pass

    def fetch_pdb(self, pdb_id):
        pdb_id = str(pdb_id).lower()
        cwd = os.getcwd()
        pdb_file = os.path.join(cwd, f'{pdb_id}.pdb')
        url = f'ftp://ftp.rcsb.org/pub/pdb/data/structures/all/pdb/pdb{pdb_id}.ent.gz'
        if not os.path.exists(pdb_file):
            urllib.request.urlretrieve(url, f'{pdb_file}.gz')
            with gzip.open(f'{pdb_file}.gz', 'rb') as f_in:
                with open(pdb_file, 'wb') as f_out:
                    f_out.write(f_in.read())

    def view(self, pdb_id):
        self.fetch_pdb(pdb_id)
        pdb_id = str(pdb_id).lower()
        pdb_file = os.path.join(os.getcwd(), f'{pdb_id}.pdb')
        with open(pdb_file, 'r') as f:
            pdb_data = f.read()
        view = py3Dmol.view(width=600, height=400)
        view.addModel(pdb_data, 'pdb')
        view.setStyle({'cartoon': {'color': 'spectrum'}})
        view.zoomTo()
        view.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py pdb_id")
        sys.exit(1)
    pdb_id = sys.argv[1]
    viewer = PDBViewer()
    viewer.view(pdb_id)

