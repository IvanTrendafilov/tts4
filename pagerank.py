import copy, time
def createGraph(): 
	G = dict()
	incoming = dict()
	myfile = open("graph.txt","r")
	for line in myfile:
		line_split = line.split(" ")
		seg1 = line_split[1]
		seg2 = line_split[2][0:-1]
		if (seg1 != seg2):
			if seg1 in G:
				G[seg1].append(seg2)
			else:
				G[seg1] = [seg2]
			if seg2 in incoming:
				incoming[seg2].append(seg1)
			else:
				incoming[seg2] = [seg1]
	myfile.close()
	return (G, incoming)

def setOfNodes(graph3):
	nodeList = []
	for node in graph3:
		nodeList.extend(graph3[node])
	return set(graph3.keys() + nodeList)

def PageRank():
	print "Working..."
	k = 10
	graphTuple = createGraph()
	graph = graphTuple[0]
	incoming = graphTuple[1]
	I,R,lam = dict(), dict(), 0.80
	P = setOfNodes(graph)
	for node in P:
		I[node] = 1/float(len(P))
		R[node] = 1/float(len(P))
	for step in range(k):
		print "Iteration", step+1
		for page in P:
			mysum = 0
			if page in incoming:
				for element in incoming[page]:
					mysum += I[element] / float(len(graph[element])) 
			R[page] = ((1 - lam) / float(len(P))) + (lam * mysum)
		I = copy.copy(R)
	return R
	
if __name__ == "__main__":
	t1 = time.time()
	res = PageRank()
	b = res.items()
	b.sort( key=lambda res:(-res[1],res[0]) )
	output = ""
	for k in range(10):
		output += str(round(b[k][1],8)) + " " + str(b[k][0]) + "\n"
	t2 = time.time()
	print output
	myfile = open("pr.txt","w")
	myfile.write(output)
	myfile.close()
	print "running time ", t2-t1
