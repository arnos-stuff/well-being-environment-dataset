# Open-sourcing PDF-format stored datasets

## Scripts and processing

The scripts allowing this can be downloaded using python 11 using

```bash
pip install pdfdataprocess
```
This is not meant to be perfect, just a quickly hacked through solution.

## Goal

The goal of this was to opensource the dataset behind the article [Meta-Analytic evidence for positive association between pro-environmental behavior and wellbeing](https://iopscience.iop.org/article/10.1088/1748-9326/abc4ae/data).

The paper itself is also in this repository but is much more easy to grab, just go to the [IOP website here](https://iopscience.iop.org/article/10.1088/1748-9326/abc4ae/pdf).


## Data

The data is stored in a single PDF file we retrieved from the additional data and is called `consumption-well-being.pdf`


## Processing

The processing is done using the `pdfdataprocess` package which can be installed using

```bash
pip install pdfdataprocess
```

The tool is a CLI so you can just call

```bash
pdfdtp mkjson
```
and 

```bash
pdfdtp pjson
```

which are shorthands foor `pdfdataprocess make-json` and `pdfdataprocess process-json`

This should yield roughly the results of the [following CSV file](./consumption-well-being.res.csv), except the headers will be a bit nasty.

You can remove them manually, I do not have the time to add this feature for now.

# Features


- [x] Extract tables from PDF
- [x] Convert tables to JSON
- [x] Process JSON to CSV
- [ ] Add headers to CSV
- [ ] Add other format output
- [ ] Add proper documentation
- [ ] Add license


