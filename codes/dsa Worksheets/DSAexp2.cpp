#include<iostream>
#include<string>
using namespace std;

int main(){
	
 char x,y;
 string str;

 int c;
    // Asking user to Enter a sstring  
 cout<<"\n  --  Enter a String  ->: ";
getline(cin,str);


// Asking what user wants to Search.
 cout<<"\n  --  Enter the character that you want to Search for : ";
cin>>x;

getchar();
// Getting a new Character to replace

 cout<<"\n -- Enter the new Character you want to replace : ";
 cin>>y;

for(int i=0 ; i<= str.size() ; i++)
 {
	if(str[i] == x)
	{
		str[i] = y;
    }

 }


cout<<"\n Final String after replacing All occurrences of char1 with char2 : "<<y<<endl<< str<<endl;

return 0;
}
