def freq(npattern, dpattern):
  
  #placeholder that assumes that all letters are equally probable.
  nfreq = 1
  dfreq = 1
  for i in npattern:
    nfreq *= len(i)
  for i in dpattern:
    dfreq *= len(i)

  return nfreq/dfreq
