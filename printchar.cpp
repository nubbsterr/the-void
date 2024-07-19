#include <iostream>

// from Learncpp 8.8
// i never thought you could loop based off LETTERS like this bruh xD

// Write a program that prints out the letters a through z along with their ASCII codes.
// Use a loop variable of type char.

int main()
{
    char c {'a'};
    while (c <= 'z')
    {
        std::cout << c << " ASCII code: " << static_cast<int>(c) << "\n";
        ++c;
    }


    return 0;
}
