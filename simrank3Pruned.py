import networkx as nx
import sqlite3
import sys
db=sqlite3.connect('../Downloads/Paper_db')
cur=db.cursor()
G=nx.DiGraph()
c=50
radius=3
neighbours=30
def simrank(u,v,r):
	global c,radius,G,neighbours;
	#~ print u,v,r
	if(r>radius):
		return 0.0
	if(u==v):
		return 1.0;
	temp=0.0;
	nu=min(len(G.neighbors(u)),neighbours);
	nv=min(len(G.neighbors(v)),neighbours);
	if(nu==0 or nv==0):
		return 0.0;
	l1=G.neighbors(u);
	l2=G.neighbors(v)
	for i in l1[:nu]:
		for j in l2[:nv]:
			if(r<radius):
				temp=temp+simrank(i,j,r+1);
	return c/(nu*nv*1.0) * temp;
cur.execute("select count(*) from papers")
record=cur.fetchone()
n=long(record[0]);
#Add nodes to Graph
for i in range(n):
	G.add_node(i);
cur.execute("select id,ref_id from papers")
record=cur.fetchall()
for i in record:
	j=i[0];
	k=i[1];
	if(k.strip()==""):
		continue;
	k=k.split(";");
	if(len(k)==0):
		continue;
	else:
		for l in k:
			G.add_edge(long(l),long(j))
print "Done loading Database"
mc=0
try:
	flag=1;
	while flag==1:
		x=raw_input()
		y=x.split();
		for i in range(0,len(y)):
			mc2=0;
			for j in range(i+1,len(y)):
				t1=long(y[i])
				t2=long(y[j])
				print t1,t2
				print simrank(t1,t2,0)
				mc+=1
				mc2+=1;
				if(mc2>=5):
					break;
				if(mc>=230):
					sys.exit(0);
except Exception as e:
	sys.exit(0);
