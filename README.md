# Non Uniform Influence Maximisation

Research code for studying influence maximisation in social networks under non uniform node costs. The project compares several seed selection heuristics (random, degree, single discount, degree discount) against multiple diffusion models (Linear Threshold, Independent Cascade, Weighted Cascade) on three real world network datasets (Amazon, GitHub, Arxiv), under both uniform and non uniform cost assumptions.

This README documents the project layout only. No source code logic was changed during this reorganisation, files were only moved into clearer locations.

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

`networks/` holds the raw downloaded network files (edge lists and feature files) from SNAP and similar sources.

`pickles/` holds NetworkX graph objects built from the raw files by `src/networks.py`, so the rest of the pipeline does not need to reparse text files every run.

`costs/` holds precomputed per node cost dictionaries (random, degree, pagerank based) used for the non uniform cost experiments, organised per dataset.

`graphs/` and `results/` hold output artefacts from experiment runs (plots and text logs), kept separate from source code.

## Known quirks carried over from the original layout

These were present before the reorganisation and were left untouched since no code was edited:

The `src/__init__.py` file imports heuristic names (`degreeDiscount`, `singleDegreeDiscount`, etc.) that no longer match the names actually exported from `src/heuristics/__init__.py` (`degreeDiscountUniform`, `degreeDiscountNonUniform`, etc.). This file appears unused by the rest of the pipeline.

`src/main.py` writes its results log to a relative path such as `results non-uniform.txt` at the repository root, while the `results/` folder already contains a similarly named file from a previous run. Running `main.py` again will create a new file at the root rather than updating the one inside `results/`.

`src/experimental/newHeuristics.py` and `src/experimental/testedHeurstics.py` are not imported anywhere else in the codebase. They appear to be scratch work from heuristic development and were grouped under `experimental/` for clarity.
