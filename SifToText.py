
node_index = 1
protein_enum = {}
edges = []

with open(sys.argv[1]) as fs:
  lines = fs.readlines()
  for line in lines:
    # format is PROT1, pp, PROT2 
    [prot1, pp, prot2] = line.split()
    x1 = node_index
    if prot1 in protein_enum:
      x1 = protein_enum[prot1]
    else:
      protein_enum[prot1] = x1 
      node_index = node_index + 1

    x2 = node_index
    if prot2 in protein_enum:
      x2 = protein_enum[prot2]
    else:
      protein_enum[prot2] = x2 
      node_index = node_index + 1

    edges.append("{0}\t{1}\t{2}".format(x1, x2, 1))

with open(sys.argv[2], "wt") as fs:
  for edge in edges:
    fs.write(edge + "\n")
