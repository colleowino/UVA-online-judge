#include <iostream>
#include <string>

using namespace std;

int main(){
    
   string line;
   while(getline (cin,line)) {
            int tam = line.size();
            char c;
            int num;      
            for(int i=0;i<tam;i++){
                 num=line[i];
                 c=num-7;   
                 cout<<c;   
            }      
            cout<<endl;  
   }

return 0;
} 
