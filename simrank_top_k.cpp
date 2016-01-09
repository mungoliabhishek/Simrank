#include <bits/stdc++.h>
#define ll long long
using namespace std;
typedef struct node
{
	ll int x,y;
	double score;
}node;
struct my
{
	bool operator()(const node &a,const node &b)
	{
		if(a.score<b.score)
		return false;
		return true;
	}
};
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll int n;
	cin>>n;
	ll int i;
	node t1,t2;
	priority_queue<node,vector<node>,my> p;
	for(i=0;i<n;i++)
	{
		cin>>t1.x>>t1.y>>t1.score;
		if(p.empty()||p.size()<8)
		{
			p.push(t1);
		}
		else
		{
			t2=p.top();
			if(t2.score<t1.score)
			{
				p.pop();
				p.push(t1);
			}
		}
	}
	while(!p.empty())
	{
		t1=p.top();
		p.pop();
		cout<<t1.x<<" "<<t1.y<<" "<<t1.score<<endl;
	}
	return 0;
}
