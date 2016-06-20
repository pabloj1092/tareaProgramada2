#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define max_rows 100000
#define send_data_tag 2001
#define return_data_tag 2002

int array[max_rows];
int array2[max_rows];

int main(int argc, char **argv){
  int my_id, root_process=0, ierr, num_rows, num_procs,
    an_id, num_rows_to_receive, avg_rows_per_process,
    sender, start_row, start_row_to_receive, end_row, num_rows_to_send;
  ierr = MPI_Init(&argc, &argv);
  clock_t end2, begin, end;
  double timeSpend;
  begin = clock();
  int sum, partial_sum;
  MPI_Status status;
  ierr = MPI_Comm_rank(MPI_COMM_WORLD, &my_id);
  ierr = MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
  int lastPrime=48611, index[lastPrime], numbers[lastPrime],index2[lastPrime], numbers2[lastPrime], prime, searchingPrime;
  num_rows=lastPrime;
  if(my_id == root_process) {
    avg_rows_per_process = lastPrime / num_procs;
    for (int i=0; i<lastPrime; i++){
       index[i] = 1;
       numbers[i] = i;
     }
     for(an_id = 1; an_id < num_procs; an_id++) {
        start_row = an_id*avg_rows_per_process + 1;
        end_row   = (an_id + 1)*avg_rows_per_process;
        if((num_rows - end_row) < avg_rows_per_process)
           end_row = num_rows - 1;
        num_rows_to_send = end_row - start_row + 1;
        ierr = MPI_Send( &num_rows_to_send, 1 , MPI_INT,
              an_id, send_data_tag, MPI_COMM_WORLD);
        ierr = MPI_Send( &index[start_row], num_rows_to_send, MPI_INT,
              an_id, send_data_tag, MPI_COMM_WORLD);
              ierr = MPI_Send( &numbers[start_row], num_rows_to_send, MPI_INT,
                    an_id, send_data_tag, MPI_COMM_WORLD);
   }
   for (int i=2; i<avg_rows_per_process+1; i++){
     if (index[i]==1){
         prime = numbers[i];
         searchingPrime = 0;
         printf("%d\n", prime);
         for(int j = i+1; j < avg_rows_per_process+1; j++) {
           if (numbers[j]%prime==0){
             index[j]=0;
           }
         }
      }
    }
    int beginTime = begin;
    for(an_id = 1; an_id < num_procs; an_id++) {
       ierr = MPI_Recv( &begin, 1, MPI_INT, MPI_ANY_SOURCE,
             return_data_tag, MPI_COMM_WORLD, &status);
       if (begin < beginTime){
         beginTime = begin;
       }
    }
    clock_t endTime = clock();
    for(an_id = 1; an_id < num_procs; an_id++) {
       ierr = MPI_Recv( &end, 1, MPI_INT, MPI_ANY_SOURCE,
             return_data_tag, MPI_COMM_WORLD, &status);
       if (end > endTime){
         endTime = end;
       }
    }
    timeSpend = (double)(endTime - beginTime)/CLOCKS_PER_SEC;
    printf("time %f\n", timeSpend);
  }
  else{
    ierr = MPI_Recv( &num_rows_to_receive, 1, MPI_INT,
          root_process, send_data_tag, MPI_COMM_WORLD, &status);
    ierr = MPI_Recv( &index2, num_rows_to_receive, MPI_INT,
          root_process, send_data_tag, MPI_COMM_WORLD, &status);
    ierr = MPI_Recv( &numbers2, num_rows_to_receive, MPI_INT,
          root_process, send_data_tag, MPI_COMM_WORLD, &status);
    int primeFinded = 0;
    for (int i=0; i<num_rows_to_receive; i++){
      if (index2[i]==1){
        for (int j=2; j<numbers2[i]+1; j++){
          if (numbers2[i]==j){
            printf("%i\n", numbers2[i]);
            for(int k=i+1; k<num_rows_to_receive; k++) {
              if (numbers2[k]%numbers2[i]==0){
                index2[k]=0;
              }
            }
            break;
          }
          if (numbers2[i]%j==0){
            index2[i] = 0;
            break;
          }
        }
      }
    }
    end2 = clock();
    ierr = MPI_Send( &end2, 1, MPI_INT, root_process,
          return_data_tag, MPI_COMM_WORLD);
    ierr = MPI_Send( &begin, 1, MPI_INT, root_process,
          return_data_tag, MPI_COMM_WORLD);
   }
   ierr = MPI_Finalize();
   return 0;
}
