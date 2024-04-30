from comet.multiverse import Multiverse

forking_paths = {
    "num": [1, 2, 3],
    "SW": [
    {
        "name": "SW29",
        "func": "comet.methods.SlidingWindow",
        "args": {
            "Option": "CONT Sliding Window",
            "time_series": "ts",
            "windowsize": 29,
            "shape": "rectangular",
            "std": 10.0,
            "diagonal": 0,
            "standardize": False,
            "fisher_z": False,
            "tril": False
        }
    },
    {
        "name": "SW45",
        "func": "comet.methods.SlidingWindow",
        "args": {
            "Option": "CONT Sliding Window",
            "time_series": "ts",
            "windowsize": 45,
            "shape": "rectangular",
            "std": 10.0,
            "diagonal": 0,
            "standardize": False,
            "fisher_z": False,
            "tril": False
        }
    }
],
    "threshold": [
    {
        "name": "t50",
        "func": "comet.graph.threshold",
        "args": {
            "Option": "PREP Threshold",
            "W": "W",
            "type": "density",
            "threshold": 0.0,
            "density": 0.5
        }
    },
    {
        "name": "t25",
        "func": "comet.graph.threshold",
        "args": {
            "Option": "PREP Threshold",
            "W": "W",
            "type": "density",
            "threshold": 0.0,
            "density": 0.25
        }
    }
],
}

def analysis_template():
    import numpy as np
    import bct
    import comet

    print(f"Decision 1: {{num}}")

    
    # Load example data and calculate dFC + local efficiency
    ts = comet.data.load_example()
    dfc = {{SW}}
    dfc = dfc[0] if isinstance(dfc, tuple) else dfc #required as LeiDA returns multiple outputs
    
    W = dfc[:,:,100]
    W_t = {{threshold}}
    
multiverse = Multiverse(name="example_multiverse")
multiverse.create(analysis_template, forking_paths)
multiverse.summary()
multiverse.visualize(universe=7, node_size=2500, figsize=(10, 5))
multiverse.run()
