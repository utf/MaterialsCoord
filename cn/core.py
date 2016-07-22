"""
Outline for the benchmarking infrastructure
"""
import abc
import os
import glob
from pymatgen.core.structure import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from collections import OrderedDict
import pandas as pd

module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))


class CNBase:
    __metaclass__ = abc.ABCMeta
    """
    This is an abstract base class for implementation of CN algorithms.
    """

    def __init__(self, params=None):
        """
        :param params: (dict) of parameters to pass to compute method.
        """
        self._params = params if params else {}
        self._cns = {}

    @abc.abstractmethod
    def compute(self, structure, n):
        """
        :param structure: (Structure) a pymatgen Structure
        :param n: (int) index of central atom in structure
        :return: Dict of CN's. e.g. {'O': 4.4, 'F': 2.1}
        """
        pass


class Benchmark(object):
    def __init__(self, methods, structure_groups="elemental", unique_sites=True, round=3):
        """
        Class for performing CN benchmarks on a set of structures

        :param methods: (list) CN methods.
        :param structure_groups: (str) or (list) groups of test structures. Defaults to "elemental"
        :param unique_sites: (bool) Only calculate symmetrically unique sites.

        """
        self.methods = methods
        self.structure_groups = structure_groups if isinstance(structure_groups, list) else [structure_groups]
        self.test_structures = OrderedDict()

        self.unique_sites = unique_sites
        self.round = round

        for g in self.structure_groups:
            self._load_test_structures(g)

        for m in self.methods:
            assert isinstance(m, CNBase)
        print "Initialization successful."

    def _load_test_structures(self, group):
        """
        Loads the structure group from test_structures
        :param group: (str) group name, options: "elemental". Defaults to "elemental"
        """
        p = os.path.join(module_dir, "..", "test_structures", group, "*.cif")
        cif_files = glob.glob(p)
        for s in cif_files:
            name = os.path.basename(s).split(".")[0]
            self.test_structures[name] = Structure.from_file(s)

    def benchmark(self):
        for m in self.methods:
            for k,v in self.test_structures.items():
                cns = []
                if self.unique_sites:
                    es = SpacegroupAnalyzer(v).get_symmetrized_structure().equivalent_sites
                    sites = [v.index(x[0]) for x in es]
                else:
                    sites = range(len(v))
                for j in sites:
                    tmpcn = m.compute(v,j)
                    if self.round:
                        self._roundcns(tmpcn, self.round)
                    cns.append( (v[j].species_string, tmpcn) )
                m._cns[k]=cns

    def report(self):
        data = {}
        for m in self.methods:
            data[m.__class__.__name__] = m._cns
        index = self.test_structures.keys()
        return pd.DataFrame(data=data, index=index)

    @staticmethod
    def _roundcns(d, ndigits):
        """
        rounds all values in a dict to ndigits
        """
        for k,v in d.items():
            d[k]=round(v,ndigits)