#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool compare(string &s1,string &s2)  {
    return s1.size() < s2.size(); 
}

//for (int i = 0; i < strings.size(); i++)
//printf("%s\n",strings[i].c_str());

unsigned int cultivandoStrings(vector<string> strings) {
    sort(strings.begin(), strings.end(), compare);

    int resposta = 1;
    
    for (int i = 1; i < strings.size(); i++) {
        if (strings[i].find(strings[i-1]) != -1) {
            resposta++;
        }
    }

    return resposta;
}
