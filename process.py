from sys import argv
from pathlib import Path
import numpy as np
import pandas as pd
import json

EXAMPLE_FILE = './consumption-well-being.json'

def processJSON(file: str = EXAMPLE_FILE):
    jdata = json.load(open())
    njd = pd.json_normalize(jdata, sep='.').to_dict(orient='records')

    rows = []
    for i, p in enumerate(njd):
        pt = p["text"]
        for r in pt:
            r["page"] = i
            for k in ["number", "pages", "height", "width"]:
                r[k] = p[k]
                rows += [r]
                
    df = pd.DataFrame.from_records(rows)

    pnum = df.page.unique().tolist()
    tops = df.top.unique().tolist()

    prows = []
    for p in pnum:
        for t in tops:
            dfph = df[(df.top == t) & (df.page == p)]
            lefts = sorted(dfph.left.unique().tolist())
            r = []        
            for lf in lefts:
                r += [dfph.loc[dfph.left == lf, 'data'].values.reshape(-1,1)]
            if not r:
                continue
            mr = np.concatenate(r,axis=1)
            prows += mr.tolist()
            
    minlen = lambda rows: min([len(i) for i in rows])
    mindiff = lambda rows: max([abs(len(i) - minL) for i in rows])

    minL = minlen(prows)

    while mindiff(prows) > 0:
        minL = minlen(prows)
        for i, r in enumerate(prows):
            if len(r) > minL:
                r = [" ".join(r[:2]), *r[2:]]
                prows[i] = r

    fdf = pd.DataFrame.from_records(prows)
    fdf.to_csv("consumption-well-being.res.csv", index=False)

