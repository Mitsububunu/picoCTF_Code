#include <stdio.h>
#include <stdlib.h>

#define ROULETTE_SIZE (36)
#define NUM_RAND_NAMBERS (10)

int main (int argc, char* argv[]) {
   int i;

   srand(atoi(argv[1]));

   for( i = 0 ; i < NUM_RAND_NAMBERS ; i++ ) {
      printf("%d\n", (rand() % ROULETTE_SIZE) + 1);
   }
   
   return 0 ;
}
