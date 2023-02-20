#include <iostream>
#include <stack>
using namespace std;

int precedence(char c)
{
    if(c == '^')
        return 3;
    else if(c == '/' || c=='*')
        return 2;
    else if(c == '+' || c == '-')
        return 1;
    else
        return -1;
}

int main()
{
    string x = "abcd^e-fgh*+^*+i-";
    stack<char> s;
    string postfix;
    char c;
    for(int i=0; i<x.length(); i++)
    {
        c = x[i];
        if((c>='a' && c<='z') || (c>='A' && c<='Z')) {postfix += c;}
        else if (c=='(') {s.push('(');}
        else if (c==')') 
        {
            while (s.top() != '(')
            {
                postfix += s.top();
                s.pop();
            }
            s.pop();
        }
        else
        {
            while (!s.empty() && precedence(x[i]) <= precedence(s.top()))
            {
                postfix += s.top();
                s.pop();
            }
            s.push(c);
        }
    }
    while(!s.empty())
    {
        postfix += s.top();
        s.pop();
    }
    cout << "\nInfix Expression: " << x;
    cout << "\nPostfix Expression: " << postfix;
    return 0;
}