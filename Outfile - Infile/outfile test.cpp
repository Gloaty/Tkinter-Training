#include <iostream>
#include <fstream>

using std::ofstream;

int main() {
    ofstream outfile("test.txt");
    outfile << "If this is present in the file, the program works!" << std::endl;
    outfile.close();
}