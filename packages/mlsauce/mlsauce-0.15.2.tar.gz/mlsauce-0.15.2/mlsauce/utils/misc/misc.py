# Authors: Thierry Moudiki
#
# License: BSD 3
import os 
import re
import subprocess
import numpy as np
from Cython.Build import cythonize
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture


def cluster(
    X,
    n_clusters=None,
    method="kmeans",
    type_scaling="standard",
    training=True,
    scaler=None,
    label_encoder=None,
    clusterer=None,
    seed=123,
):

    assert method in ("kmeans", "gmm"), "method must be in ('kmeans', 'gmm')"
    assert type_scaling in (
        "standard",
        "minmax",
        "robust",
    ), "type_scaling must be in ('standard', 'minmax', 'robust')"

    if training:
        assert (
            n_clusters is not None
        ), "n_clusters must be provided at training time"
        if type_scaling == "standard":
            scaler = StandardScaler()
        elif type_scaling == "minmax":
            scaler = MinMaxScaler()
        elif type_scaling == "robust":
            scaler = RobustScaler()
        else:
            raise ValueError(
                "type_scaling must be in ('standard', 'minmax', 'robust')"
            )

        scaled_X = scaler.fit_transform(X)
        label_encoder = OneHotEncoder(handle_unknown="ignore")

        if method == "kmeans":
            clusterer = KMeans(
                n_clusters=n_clusters, random_state=seed, n_init="auto"
            ).fit(scaled_X)
            res = label_encoder.fit_transform(
                clusterer.labels_.reshape(-1, 1)
            ).toarray()
        elif method == "gmm":
            clusterer = GaussianMixture(
                n_components=n_clusters, random_state=seed
            ).fit(scaled_X)
            res = label_encoder.fit_transform(
                clusterer.predict(scaled_X).reshape(-1, 1)
            ).toarray()
        else:
            raise ValueError("method must be in ('kmeans', 'gmm')")

        return res, scaler, label_encoder, clusterer

    else:  # @ inference time

        assert (
            scaler is not None
        ), "scaler must be provided at inferlabel_encodere time"
        assert (
            label_encoder is not None
        ), "label_encoder must be provided at inferlabel_encodere time"
        assert (
            clusterer is not None
        ), "clusterer must be provided at inferlabel_encodere time"
        scaled_X = scaler.transform(X)

        return label_encoder.transform(
            clusterer.predict(scaled_X).reshape(-1, 1)
        ).toarray()


def cythonize_file(filename):
    """
    Cythonize a given .pyx file and compile it if it doesn't exist already.
    
    Args:
    filename (str): Name of the .pyx file to cythonize.
    """
    # Define a generic regex pattern to match compiled files
    compiled_pattern = re.compile(r"\.cpython-\d+\.\d+-[^-]+-(?:x86|x64)_\w+\.so$")
    
    # Check if any matching compiled files already exist
    compiled_files = [f for f in os.listdir() if compiled_pattern.search(f)]
    if compiled_files:
        # Compiled file(s) already exist, so we skip silently
        return
    
    # Get a list of all .pyx files in the current directory
    pyx_files = [file for file in os.listdir() if file.endswith(".pyx")]
    
    if not pyx_files:
        print("No .pyx files found in the current directory.")
        return
    
    for pyx_file in pyx_files:
        # Cythonize the .pyx file
        cythonized_modules = cythonize(pyx_file)
        
        # Compile the generated C code using a C compiler (GCC for Unix-like systems)
        for extension in cythonized_modules:
            setup_args = extension.get_metadata('setup_args')
            # Extract the module name from setup_args
            module_name = setup_args['ext_modules'][0].name
            
            # Compile the C code into a Python extension module (.so file)
            compile_command = f"gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing \
                                -I/usr/include/python3.x -o {module_name}.so {module_name}.c"
            
            os.system(compile_command)
            
            print(f"Compiled {module_name}.so")
            
# merge two dictionaries
def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


# check if x is int
def is_int(x):
    try:
        return int(x) == x
    except:
        return False


# check if x is float
def is_float(x):
    return isinstance(x, float)


# check if the response contains only integers
def is_factor(y):
    n = len(y)
    ans = True
    idx = 0

    while idx < n:
        if is_int(y[idx]) & (is_float(y[idx]) == False):
            idx += 1
        else:
            ans = False
            break

    return ans


# flatten list of lists
def flatten(l):
    return [item for sublist in l for item in sublist]
