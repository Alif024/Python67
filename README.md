# Python67
For study Python

# Getting started with conda
Miniconda is a free minimal installer for conda. It is a small bootstrap version of Anaconda that includes only conda, Python, the packages they both depend on, and a small number of other useful packages (like pip, zlib, and a few others). [Go to download...](https://docs.anaconda.com/miniconda/) 

### Examples:
Install the package 'scipy' into the currently-active environment:
```shell
conda install scipy
```
Install a list of packages into an environment, myenv:
```shell
conda install -n myenv scipy curl wheel
```
Install a specific version of 'python' into an environment, myenv:
```shell
conda install -p path/to/myenv python=3.11
```

### Export environment
```shell
conda env export > requirements.yaml
```
or
```shell
pip list --format=freeze > requirements.txt
```

### Import environment
```shell
conda env create --prefix D:\ProgramData\miniconda3\envs\Compro67 -f requirements.yaml
```
or
```shell
pip install -r requirements.txt
```
### Update environment
```shell
conda env update -n basicPython -f requirements.yaml
```
[read more...](https://docs.conda.io/projects/conda/en/stable/commands/index.html) 

# How to use nbconvert
Supported output formats [read more...](https://nbconvert.readthedocs.io/en/latest/usage.html)
- HTML
- LaTeX
- PDF
- WebPDF
- Reveal.js HTML slideshow
- Markdown
- Ascii
- reStructuredText
- executable script
- notebook

### Getting MiKTeX.
To install a basic TeX/LaTeX system on Windows, download and run this installer. [downlaod...](https://miktex.org/download)
### Using as a command line tool.
```shell
jupyter nbconvert --to FORMAT notebook.ipynb
```
