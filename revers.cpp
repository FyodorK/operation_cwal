/* crakme first trial implementation*/

#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

int main() {

  int sum = 0;
  string s;

  cout << "Insert a string of chars only: ";
  cin >> s;
  
  for (int i = 0; i < s.length(); i++) {
      if (s[i] <'A'){
         cout << "It is not work in that way. Use characters not numbers" << endl;
         return 1;      
      }else if (s[i] >= 'Z') {
         s[i] -= 0x20;
      }
      sum += s[i];
  }
  
  sum ^= 0x5678;
  sum ^= 0x1234;

  cout << "Krya-Krya: " << s << "\n" << "Serial key: " << sum << endl;
  return 0;
}
