import time, math, string
def getAllNodes(a, b):
	return set(a.keys() + b.keys())

def createGraph():
	outgoing = dict()
	incoming = dict()
	myfile = open("graph.txt","r")
	for line in myfile:
		line_split = line.split(" ")
		seg1 = line_split[1]
		seg2 = line_split[2][0:-1]
		if seg1 != seg2:
			if seg1 not in outgoing:
				outgoing[seg1] = {}
				outgoing[seg1]["sum"] = 0
			try:
				outgoing[seg1][seg2] += 1 
				outgoing[seg1]["sum"] += 1 
			except KeyError:
				outgoing[seg1][seg2] = 1
				outgoing[seg1]["sum"] += 1 
			if seg2 not in incoming:
				incoming[seg2] = {}
				incoming[seg2]["sum"] = 0
			try:
				incoming[seg2][seg1] += 1 
				incoming[seg2]["sum"] += 1 
			except KeyError:
				incoming[seg2][seg1] = 1
				incoming[seg2]["sum"] += 1 
	myfile.close()
	return (incoming, outgoing)
	
def hits():
	k = 10
	G = createGraph()
	incoming = G[0]
	outgoing = G[1]
	P = getAllNodes(incoming, outgoing)
	initValue = 1/float(math.sqrt(len(P)))
	auth = dict()
	hub = dict()
	for page in P:
		auth[page] = initValue
		hub[page] = initValue

	for step in range(k):
		print "Iteration ", step+1
		norm = 0	
		for page in incoming:
			for element in incoming[page]:
				if element != "sum" :					
					auth[page] += hub[element] * incoming[page][element]
			norm += auth[page] * auth[page]
		norm = math.sqrt(norm)
		for page in P:
			auth[page] = auth[page]/float(norm)
		norm = 0
		for page in outgoing:
			for element in outgoing[page]:
				if element != "sum" :	
					hub[page] += auth[element] * outgoing[page][element]
			norm += hub[page] * hub[page]
		norm = math.sqrt(norm)
		for page in P:
			hub[page] = hub[page]/float(norm)
	return (hub, auth)
	

if __name__ == "__main__":
	print "Working..."
	t1 = time.time()
	res = hits()
	hubs = res[0]
	auth = res[1]
	print "Hubs score for jeff.dasovich@enron.com: ", round(hubs['jeff.dasovich@enron.com'],8)
	print "Auth score for jeff.dasovich@enron.com: ", round(auth['jeff.dasovich@enron.com'],8)
	output = ""
	b = hubs.items()
	b.sort( key=lambda hubs:(-hubs[1],hubs[0]) )
	print "Hubs: "
	for k in range (10):
		output += str(round(b[k][1],8)) + " " + str(b[k][0]) + "\n"
	print output
	myfile = open("hubs.txt","w")
	myfile.write(output)
	myfile.close()
	output = ""
	b = auth.items()
	b.sort( key=lambda auth:(-auth[1],auth[0]) )
	print "Auth: "
	for k in range (10):
		output += str(round(b[k][1],8)) + " " + str(b[k][0]) + "\n"
	print output
	myfile = open("auth.txt","w")
	myfile.write(output)
	myfile.close()
	t2 = time.time()
	print "running time ", t2-t1
