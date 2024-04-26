#!/usr/bin/env python

import sys

import numpy as np

from ONTraC.data import load_dataset
from ONTraC.optparser import opt_NT_validate, prepare_NT_optparser
from ONTraC.run.processes import *


# ------------------------------------
# Main Function
# ------------------------------------
def main() -> None:
    """
    Main function
    :return: None
    """

    # ----- prepare -----
    # --- load parameters ---
    options = load_parameters(opt_validate_func=opt_NT_validate, prepare_optparser_func=prepare_NT_optparser)
    # --- load data ---
    dataset, _ = load_dataset(options=options)
    # load consolidated s_array and out_adj_array
    consolidate_s_array = np.loadtxt(fname=f'{options.GNN_dir}/consolidate_s.csv.gz', delimiter=',')
    consolidate_out_adj_array = np.loadtxt(fname=f'{options.GNN_dir}/consolidate_out_adj.csv.gz', delimiter=',')

    # ----- Pseudotime -----
    if consolidate_s_array is not None and consolidate_out_adj_array is not None:
        NTScore(options=options,
                dataset=dataset,
                consolidate_s_array=consolidate_s_array,
                consolidate_out_adj_array=consolidate_out_adj_array)


# ------------------------------------
# Program running
# ------------------------------------
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("User interrupts me! ;-) See you ^.^!\n")
        sys.exit(0)
