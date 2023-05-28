for i,r in enumerate(rows):
    if len(r) > l:
        r = [' '.join(r[:2]), *r[2:] ]
    rows[i] = r


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
        rows += mr.tolist()for i,p in enumerate(njd):
    pt = p['text']
    for r in pt:
        r['page'] = i
        for k in ['number', 'pages', 'height', 'width']:
            r[k] = p[k]
            rows += [r]



njd = pd.json_normalize(jdata, sep='.').to_dict(orient='records')


jdata = json.load(open('./consumption-well-being.json'))

