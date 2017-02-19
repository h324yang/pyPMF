from core.PMF import PMF

D = "ml-1m/ratings.dat"
model = PMF()
tr_data = model.load_triples(D)
model.fit(tr_data)
