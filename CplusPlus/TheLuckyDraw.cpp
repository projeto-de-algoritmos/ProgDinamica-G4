#include <bits/stdc++.h>
using namespace std;
int lis(int ind,vector<int> &arr,int n )
{
    vector<int> temp;
    for(int i=ind;i<ind+n;i++)
    {
        if(temp.empty() || arr[i]>temp.back())
        {
            temp.push_back(arr[i]);
        }
        else{
            auto it  =lower_bound(temp.begin(),temp.end(),arr[i]);
            *it=arr[i];
        }
    }
    return temp.size();
}
int main() {
	int t;
	cin>>t;
		vector<int> arr;
	while(t--)
	{
	    int n;
	    	cin>>n;
           arr.resize(2*n);
        	for(int i=0;i<n;i++)
        	{
        	    cin>>arr[i];
        	    arr[i+n]=arr[i];
        	}
        	int ans=0;
        	for(int i=0;i<n;i++)
        	{
        	    ans=max(ans,lis(i,arr,n));
        	}
        	cout<<ans<<endl;
	}

	return 0;
}