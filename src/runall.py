#!/usr/bin/env python
"""Script to run entire SN analysis."""

import os

import data_utils
import fitting

DATA_URL = ("http://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/"
            "fits?J%2FA%2BA%2F523%2FA7")

data_fname = os.path.join("..", "data", "sndata.fits")
plot_fname = os.path.join("..", "plots", "cosmofit.png")
results_fname = os.path.join("..", "results", "results.txt")

# download the data if we haven't already done so.
if not os.path.exists(data_fname):
    print("downloading data...")
    data_utils.download_file(DATA_URL, data_fname)
