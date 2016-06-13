#include<stdio.h>
#include<time.h>

int main(){
   clock_t begin, end;
   double timeSpend;
   begin = clock();

   int n=5,lastPrime=48611, index[lastPrime], numbers[lastPrime], prime, searchingPrime;
   for (int i=0; i<lastPrime; i++){
     index[i] = 1;
     numbers[i] = i+1;
   }
   for (int c=0; c<n; c++){
     searchingPrime = 1;
     for (int i=1; i<=lastPrime; i++){
       if (index[i]==1){
         if (searchingPrime==1){
           prime = numbers[i];
           index[i] = 0;
           searchingPrime = 0;
           printf("%d\n", prime);
         }
         if (numbers[i]%prime==0){
           index[i]=0;
         }
       }
     }
   }

   end = clock();
   timeSpend = (double)(end - begin)/CLOCKS_PER_SEC;
   printf("%f\n", timeSpend);
   return 0;
}
