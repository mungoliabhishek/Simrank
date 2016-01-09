import networkx as nx
import sqlite3
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
print "Enter input"
flag=1
while flag==1:
	x=raw_input()
	x=x.split();
	x[0]=long(x[0])
	x[1]=long(x[1])
	if(x[0]==-1 and x[1]==-1):
		flag=0;
		continue;
	print simrank(x[0],x[1],0)
