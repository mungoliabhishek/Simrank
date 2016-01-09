#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin>>n;
	int i,a[n][2];
	double mymin=INT_MAX,mymax=INT_MIN;
	double t,b[n];
	for(i=0;i<n;i++)
	{
		cin>>a[i][0]>>a[i][1]>>b[i];
		mymin=min(mymin,b[i]);
		mymax=max(mymax,b[i]);
	}
	for(i=0;i<n;i++)
	{
		cout<<a[i][0]<<" "<<a[i][1]<<" ";
		t=((b[i]-mymin)/(mymax-mymin));
		cout<<t<<endl;
	}
	return 0;
}
