# Python67
For study Python

# Export environment
```shell
conda env export > requirements.yaml
```

# Import environment
```shell
conda env create -f requirements.yaml
```

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

Using as a command line tool.
```shell
jupyter nbconvert --to FORMAT notebook.ipynb
```