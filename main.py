import pandas as pd
import numpy as np
import itertools
from ast import literal_eval
from chord import Chord

genres = pd.read_csv('AnimeList.csv')['genre']
genres = genres[genres.str.len() > 0]
genres = [list(itertools.combinations(i.split(', '), 2)) for i in genres]
genres = list(itertools.chain.from_iterable((i, i[::-1]) for c_ in genres for i in c_))

matrix = pd.pivot_table(
    pd.DataFrame(genres), index=0, columns=1, aggfunc="size", fill_value=0
).values.tolist()

names = np.unique(genres).tolist()
print(names)
Chord(matrix, names, wrap_labels=False, margin=80, padding=0.018, width=2000).to_html('index.html')