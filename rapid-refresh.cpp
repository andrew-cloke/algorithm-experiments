// Hello world

#include <iostream>

class pet
{
public:
    virtual void makeNoise()=0;
};

class dog : public pet
{
    virtual void makeNoise()
    {
        std::cout << "Woof\n";
    };
};

class cat : public pet
{
    virtual void makeNoise()
    {
        std::cout << "Meoow\n";
    };
};

int main()
{
    std::cout << "Hello World\n";
    pet* aPet=new cat;
    aPet->makeNoise();
    return 0;
}