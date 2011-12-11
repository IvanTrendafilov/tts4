def convert(email):
	emails={'klay@enron.com':['kenneth.l.lay@enron.com','klay.enron@enron.com','kenlay@enron.net','kenlay@enron.com','ken.lay@enron.com','kennethlay@enron.net','kennethlay@enron.com','kenneth.lay@enron.com'],'jeff.skilling@enron.com':['jeffskilling@enron.com','skillingj@enron.com','jeffrey.skilling@enron.com'],'louise.kitchen@enron.com':['lkitchen@enron.com','lkitchen@enron.co.uk'],'jeff.dasovich@enron.com':['dasovich@haas.berkeley.edu','jeffdasovich@enron.com','jeffdasovich@ees.enron.com','dasovich.jeff@enron.com','dasovich@inhale.com','dasovich@wco.com'],'sally.beck@enron.com':['sallybeck@enron.com'],'vince.kaminski@enron.com':['vince.j.kaminski@enron.com','vkaminski@aol.com','vincejkaminski@enron.com','vincejkaminski@ei.enron.com','kaminski@aol.com','j..kaminski@enron.com'],'john.lavorato@enron.com':['lavorato@enron.com','john.j.lavorato@enron.com','jlavorato.hba1989@ivey.ca'],'jeffrey.shankman@enron.com':['jeff.shankman@enron.com','jeffrey.a.shankman@enron.com','jeffshankman@hotmail.com'],'steven.kean@enron.com':['skean@enron.com','steven.j.kean@enron.com','kean@rice.edu'],'richard.shapiro@enron.com':['rshapiro@enron.com','shapiro@haas.berkeley.edu','rickshapiro@hotmail.com'],'rod.hayslett@enron.com':['rod.hayslett@enron.c','hayslett.rod@enron.com'],'rick.buy@enron.com':['rbuy@enron.com','rbuy@ect.enron.com'],'david.delainey@enron.com':['w..delainey@enron.com','delainey.david@enron.com'],'sara.shackleton@enron.com':['shackleton@enron.com'],'tana.jones@enron.com':['tanajones@enron.com','tanajones@enron.com.enron.net'],'gerald.nemec@enron.com':['gnemec@ect.enron.com','gnemec@enron.com','gnemec@houston.rr.com']}
	for key in emails:
		if email in emails[key]:
			print key
			return key
	return email	

			
nodes = ['klay@enron.com', 'jeff.skilling@enron.com', 'mark.taylor@enron.com', 'kenneth.lay@enron.com', 'louise.kitchen@enron.com',
'jeff.dasovich@enron.com', 'sally.beck@enron.com', 'vince.kaminski@enron.com', 'john.lavorato@enron.com', 'jeffrey.shankman@enron.com',
'steven.kean@enron.com', 'richard.shapiro@enron.com', 'rod.hayslett@enron.com', 'rick.buy@enron.com', 
'david.delainey@enron.com','sara.shackleton@enron.com','tana.jones@enron.com','gerald.nemec@enron.com']
myfile = open('../graph.txt','r')
graph = dict()
count = 0
for line in myfile:
        count += 1
        print count
        line_split = line.split(" ")
        seg1 = convert(line_split[1])
        seg2 = convert(line_split[2][0:-1])
	if (seg1 in nodes) and (seg2 in nodes):
		if seg1 != seg2:
			if seg1 in graph:
				graph[seg1].append(seg2)
			else:
				graph[seg1] = [seg2]
output = "digraph G {\n"
for node in graph:
        for element in graph[node]:
                if (graph[node].count(element) > 10) and (element in nodes):
                        output += "\t\"" + str(node) + "\" -> \"" + str(element) + "\";\n"
output += "}\n"
result = open("graph.dot","w")
result.write(output)
