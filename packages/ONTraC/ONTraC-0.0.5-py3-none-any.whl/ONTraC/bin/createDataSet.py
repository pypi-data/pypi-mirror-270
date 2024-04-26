#!/usr/bin/env python

import sys

from ONTraC.log import *
from ONTraC.optparser import (opt_create_ds_validate, prepare_create_ds_optparser)
from ONTraC.utils.niche_net_constr import load_original_data, construct_niche_network, gen_samples_yaml


# ------------------------------------
# Main Function
# ------------------------------------
def main() -> None:
    """
    main function
    Input data files information should be stored in a YAML file.
    """

    # prepare options
    options = opt_create_ds_validate(prepare_create_ds_optparser())

    # load original data
    ori_data_df = load_original_data(options=options, data_file=options.dataset)

    # define edges for each sample
    construct_niche_network(options=options, ori_data_df=ori_data_df)

    # save samples.yaml
    gen_samples_yaml(options=options, ori_data_df=ori_data_df)


# ------------------------------------
# Program running
# ------------------------------------
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("User interrupts me! ;-) See you ^.^!\n")
        sys.exit(0)
