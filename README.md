Play with DuckDB using data in Azure.

# Getting Started

## VSCode

Install:
- [Miniconda](https://docs.anaconda.com/free/miniconda/)
- [VSCode](https://code.visualstudio.com/Download)
  - Extensions [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

Open a shell and run:
```bash
conda env create -f env.yaml
conda activate az-duckdb
code .
```
Then open the notebooks.

## Docker

Build the Docker image:
```bash
docker build -t az-duckdb:latest .
```

Run the Docker container:
```bash
docker run -it --rm -p 8888:8888 az-duckdb:latest
```

Then find the URL that looks like http://127.0.0.1:8888/tree?token=xxx at the command prompt and open it in a browser.

# References

- Sample data: [HuggingFaceFW/fineweb](https://huggingface.co/datasets/HuggingFaceFW/fineweb/tree/main/data/CC-MAIN-2013-20)
