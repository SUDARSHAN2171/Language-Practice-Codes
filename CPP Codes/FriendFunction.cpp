#include<iostream>
#include<iomanip>
using namespace std;
class Complex
{
    int a,b;

    public :
    void setdata(int x,int y)
    {
        a=x;
        b=y;
    }

    friend Complex setDataBySum(Complex a1,Complex b1);//non member function but still allow to do anything by declearing 
    
    void printNumber()
    {
        cout<<"Your Complex : "<<a<<" + "<<b<<"i"<<endl;
    }
};
Complex setDataBySum(Complex a1,Complex b1)
    {
        Complex c;
        c.setdata((a1.a+b1.a),(a1.b+b1.b));
        return c;
    }
int main()
{
    Complex c1,c2,c3;
    c1.setdata(1,3);
    c1.printNumber();

    c2.setdata(5,6);
    c2.printNumber();

    c3= setDataBySum(c1,c2);
    c3.printNumber();
    return 0;
}