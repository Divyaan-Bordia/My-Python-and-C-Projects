#include <iostream>
#include <string>

using namespace std;

int  main() {
    srand(time(0));
    int PC;
    int CC;
    cout << "Enter 0 Rock, 1 Paper, 2 for Scissor: ";
    cin >> PC;
    CC = rand()%3;

    if (PC == 0)
        cout << "Your Choice: Rock" << endl;
    else if (PC == 1)
        cout << "Your Choice: Paper" << endl;
    else
        cout << "Your Choice: Scissor" << endl;

    if (CC == 0)
        cout << "Computer Choice: Rock" << endl;
    else if (CC == 1)
        cout << "Computer Choice: Paper" << endl;
    else 
        cout << "Computer Choice: Scissor" << endl;
    
    if (PC == CC)
        cout << "Draw";
    else if (PC == 1 && CC == 2)
        cout << "You Win";
    else if (PC == 1 && CC == 0)
        cout << "You Win!!!";
    else
        cout << "You Lose🥺";
        
    return 0;
}
