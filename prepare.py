#%%
import pandas as pd
import json

#%%
d = pd.read_excel('pokuty_cizp.xlsx')

#%%
d.pravni_moc = d.pravni_moc.astype('str')

#%%
with open('pokuty.js', 'w', encoding='utf-8') as f:
    f.write('pok = ' + json.dumps(list(d.to_dict(orient='index').values())) + ';')
