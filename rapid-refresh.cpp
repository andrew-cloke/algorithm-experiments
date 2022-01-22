// Hello world

#include <iostream>
#include <list>
#include <map>
#include <string>
#include <stack>

using namespace std;

class pet
{
public:
    virtual void makeNoise()=0;
};

class dog : public pet
{
public:
    virtual void makeNoise()
    {
        cout << "Woof\n";
    };
};

class cat : public pet
{
public:
    virtual void makeNoise()
    {
        cout << "Meoow\n";
    };
};

int main()
{
    cout << "Hello World\n";
    cat aPet;
    aPet.makeNoise();

    list<int> li;
    li.push_back(1);
    li.push_back(2);
    li.push_front(3);
    li.push_front(4);

    list<int>::iterator i; 
    for(i=li.begin();i!=li.end();i++)
    {
        cout << *i << " ";
    }
    cout << endl;

    map<char,string> a;
    a['a']="Hello";
    a['b']="World";

    map<char,string>::iterator j;
    for(j=a.begin();j!=a.end();j++)
    {
        cout << j->second << " ";
    }
    cout << endl;

    stack<string> b;
    b.push("Hello");
    b.push("World");
    b.push("Goodbye");
    b.push("Evil");

    while(!b.empty())
    {
        cout << b.top() << " ";
        b.pop();
    }
    cout << endl;

    return 0;
}