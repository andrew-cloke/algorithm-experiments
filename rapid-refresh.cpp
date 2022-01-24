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

class Node
{
public:
    Node(int a)
    {
        data=a;
        iLeft=NULL;
        iRight=NULL;
    }

    int data;
    Node* iLeft;
    Node* iRight;
};

void printNode(Node* a) {
    cout << " " << a->data << " ";
    if(a->iLeft) {
        cout << "Left";
        printNode(a->iLeft);
    } else {
        cout << endl;
    }
    if(a->iRight) {
        cout << "Right";
        printNode(a->iRight);
    } else {
        cout << endl;
    }
}

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

    Node* root=new Node(2);
    root->iLeft=new Node(4);
    root->iRight=new Node(7);
    root->iRight->iLeft=new Node(9);
    root->iRight->iRight=new Node(10);

    printNode(root);
    cout << endl;

    return 0;
}