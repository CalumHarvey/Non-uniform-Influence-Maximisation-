# Non Uniform Influence Maximisation

Research code for studying influence maximisation in social networks under non uniform node costs. The project compares several seed selection heuristics (random, degree, single discount, degree discount) against multiple diffusion models (Linear Threshold, Independent Cascade, Weighted Cascade) on three real world network datasets (Amazon, GitHub, Arxiv), under both uniform and non uniform cost assumptions.

## Dissertation

This repository is the codebase for Calum Harvey's CS913 master's dissertation, "Budgeted Influence Maximisation in Social Networks," completed in the Department of Computer Science at the University of Warwick (September 2021), supervised by Dr James Archbold.

The full write up is included in this repository at [`docs/Budgeted Influence Maximisation in Social Networks - Dissertation.pdf`](docs/Budgeted%20Influence%20Maximisation%20in%20Social%20Networks%20-%20Dissertation.pdf).

The dissertation extends the influence maximisation problem to the budgeted setting, where every node in a network has an arbitrary cost rather than a uniform cost, and a seed set must be chosen without exceeding a fixed budget. It proposes and evaluates several novel heuristics, including Lowest Cost, Highest Cost, Average Cost, and two ratio based heuristics named PICR and PICRnp, which weigh a node's potential influence against its cost. It also proposes PageRank as a new node costing function, alongside the more standard random and degree based costing approaches.

Experiments were run across three real world networks (Amazon, GitHub, Arxiv), three diffusion models (Linear Threshold, Independent Cascade, Weighted Cascade), and three costing functions (random, degree, PageRank). The headline finding was that the Lowest Cost and PICR heuristics consistently outperformed previously developed heuristics across nearly every combination tested, with Lowest Cost showing the most consistent performance overall, and PageRank based costing revealing weaknesses in degree only costing that the newer heuristics were able to exploit.

## Folder structure

```
.
├── src/                  All Python source code
│   ├── main.py           Entry point: runs the full experiment sweep
│   ├── networks.py       Loads raw network files and builds NetworkX pickles
│   ├── DiffusionModels.py  Loads pickled networks and runs diffusion models
│   ├── costFunctions.py  Generates node cost labels (random, degree, pagerank)
│   ├── heuristics/       Seed set selection heuristics package
│   ├── models/           Custom diffusion model implementations
│   └── experimental/     Exploratory scripts not used by the main pipeline
│       ├── newHeuristics.py
│       ├── testedHeurstics.py
│       └── makegraphs.py
├── networks/             Raw network edge list files (input data)
├── pickles/              Preprocessed NetworkX graph objects (.pickle)
├── costs/                Precomputed per node cost labels (.p) per dataset
├── graphs/               Output plots from experiment runs (.png)
├── results/              Output text logs from experiment runs
├── docs/                 Dissertation write up (PDF)
└── .vscode/              Editor settings
```

## Important: how to run scripts

The code reads and writes data using paths that are relative to the current working directory, for example `costs/amazon/pagerank.p` or `pickles/github.pickle`. These paths are not relative to where the `.py` file lives.

Because of this, scripts must always be run from the repository root, not from inside `src/`. For example:

```
cd Non-uniform-Influence-Maximisation-
python src/main.py
```

Running `cd src && python main.py` will fail, since the data folders (`networks/`, `pickles/`, `costs/`, `graphs/`, `results/`) live one level above `src/`.

## Data folders

`