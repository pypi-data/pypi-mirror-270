import argparse
import json
import logging
import os
from typing import Tuple, Union

import numpy as np
import pandas as pd
from anndata import AnnData
from scipy.sparse import csr_matrix

def diffusion_step(
    coords: np.ndarray,
    diffusion_coefficient: Union[float, int] = 1,
    time_steps: int = 1,
    inplace=False,
    **kwargs,
):
    logging.info(f"Running diffusion step{' not ' if not inplace else ' '}inplace")
    _coords = coords.copy() if not inplace else coords
    walks = np.array([[-1, 1], [-1, 0], [1, 0], [1, 1], [0, 1], [0, -1], [-1, -1], [1, -1]])
    # Run diffusion step on the two dimensional lattice
    logging.info("T = " + str(time_steps) + ", D = " + str(diffusion_coefficient))
    for _ in range(time_steps):
        _coords[:] = _coords[:] + walks[np.random.choice(8, (len(_coords)))] * diffusion_coefficient

    logging.info(
        f"MSD for X and Y {np.mean((_coords - coords)**2, axis=0)/(diffusion_coefficient**2)} (standardized by diffusion units)"
    )
    return _coords


def diffusion_adata(adata: AnnData, *args, **kwargs) -> Tuple[AnnData, Union[csr_matrix, np.ndarray]]:

    if "total_counts" not in adata.obs:
        raise ValueError("Could not find 'total_counts' in adata")

    if "spatial" not in adata.obsm:
        raise ValueError("The adata object does not contain spatial information")

    all_coordinates = adata.obsm["spatial"]

    # Compute the expressed genes
    X_nonzero_loc, X_nonzero = adata.X.nonzero()
    X_nonzero_counts = adata.X.data
    all_coordinates_with_transcripts = all_coordinates[X_nonzero_loc]

    # Detect and remove duplicates
    index_nonzero = np.unique(
        np.array(
            [
                all_coordinates_with_transcripts[:, 0],
                all_coordinates_with_transcripts[:, 1],
                X_nonzero,
            ]
        ).T,
        axis=0,
        return_index=True,
    )[1]
    X_nonzero_loc = X_nonzero_loc[index_nonzero]
    X_nonzero = X_nonzero[index_nonzero]
    X_nonzero_counts = X_nonzero_counts[index_nonzero]

    # Unravel the counts (for genes with more than one UMI per spot).
    X_nonzero_unravel_counts = np.repeat(X_nonzero, X_nonzero_counts.astype(np.int32))

    # Coordinates of spots, per gene. Only those that have counts.
    all_coordinates_with_transcripts = all_coordinates[X_nonzero_loc]

    # Coordinates, one per 'molecule'
    coord_per_molecule = np.repeat(all_coordinates_with_transcripts, X_nonzero_counts.astype(np.int32), axis=0)

    # Run the diffusion step
    _diffused = diffusion_step(coord_per_molecule, **kwargs)

    indptr = np.arange(len(X_nonzero_unravel_counts))
    indices = X_nonzero_unravel_counts
    data = np.ones(len(X_nonzero_unravel_counts))

    # Efficiently create a csr_matrix from the assignment of genes
    X_diff = csr_matrix((data, indices, indptr))
    return _diffused, X_diff


def create_adata_from_diffusion_with_metrics(coords: np.ndarray, X: Union[np.ndarray, csr_matrix], vars):
    adata_diffusion = AnnData(
        X.astype(np.float32), obs=pd.DataFrame(index=pd.RangeIndex(0, X.shape[0]).astype(str)), var=vars
    )

    # Populate metrics and coordinates into adata
    calculate_adata_metrics(adata_diffusion)
    adata_diffusion.obsm["spatial"] = coords[:-1]
    adata_diffusion.obs["x_pos"] = coords[:-1, 0]
    adata_diffusion.obs["y_pos"] = coords[:-1, 1]
    return adata_diffusion