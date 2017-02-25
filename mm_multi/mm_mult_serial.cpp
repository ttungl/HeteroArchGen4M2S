/******************************************************************/
/* Matrix Matrix Multiplication Program Example -- serial version */
/* September 2010 -- B. Earl Wells -- University of Alabama       */
/*                                    in Huntsville               */
/******************************************************************/
// mm_mult_serial.c
// compilation:
//   gcc mm_mult_serial.c -o mm_mult_serial
/*
   This program is designed to perform matrix matrix multiplication
   A x B = C, where A is an lxm matrix, B is a m x n matrix and
   C is a l x n matrix. The program is designed to be a template 
   serial program that can be expanded into a parallel multiprocess
   and/or a multi-threaded program.

   The program randomly assigns the elements of the A and B matrix
   with values between 0 and a MAX_VALUE. It then multiples the
   two matrices with the result being placed in the C matrix.
   The program prints out the A, B, and C matrices.

   The program is executed using one or three command line parameters.
   These parameters represent the dimension of the matrices. If only
   one parameter is used then then it is assumed that square matrices are
   to be created and multiplied together that have the specified 
   dimension. In cases where three command line parameters are entered
   then the first parameter is the l dimension, the second the m, and
   the third is the n dimension.

   To execute:
   mm_mult_serial [l_parameter] <m_parameter n_parameter] 
*/

using namespace std;
#include <iostream>
#include <iomanip>
#include <sstream>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>

#define MX_SZ 320
#define SEED 2397           /* random number seed */
#define MAX_VALUE  100.0    /* maximum size of array elements A, and B */

/* copied from mpbench */
#define TIMER_CLEAR     (tv1.tv_sec = tv1.tv_usec = tv2.tv_sec = tv2.tv_usec = 0)
#define TIMER_START     gettimeofday(&tv1, (struct timezone*)0)
#define TIMER_ELAPSED   ((tv2.tv_usec-tv1.tv_usec)+((tv2.tv_sec-tv1.tv_sec)*1000000))
#define TIMER_STOP      gettimeofday(&tv2, (struct timezone*)0)
struct timeval tv1,tv2;

/*
This declaration facilitates the creation of a two dimensional 
dynamically allocated arrays (i.e. the lxm A array, the mxn B
array, and the lxn C array).  It allows pointer arithmetic to 
be applied to a single data stream that can be dynamically allocated.
To address the element at row x, and column y you would use the
following notation:  A(x,y),B(x,y), or C(x,y), respectively.
Note that this differs from the normal C notation if A were a
two dimensional array of A[x][y] but is still very descriptive
of the data structure.
*/
#define A(i,j) *(a+i*dim_m+j)
#define B(i,j) *(b+i*dim_n+j)
#define C(i,j) *(c+i*dim_n+j)

/*
   Routine to retrieve the data size of the numbers array from the 
   command line or by prompting the user for the information
*/
void get_index_size(int argc,char *argv[],int *dim_l,int *dim_m,int *dim_n) {
   if(argc!=2 && argc!=4) {
      cout<<"usage:  mm_mult_serial [l_dimension] <m_dimension n_dimmension>"
           << endl;
      exit(1);
   }
   else {
      if (argc == 2) {
         *dim_l = *dim_n = *dim_m = atoi(argv[1]);
      }
      else {
         *dim_l = atoi(argv[1]);
         *dim_m = atoi(argv[2]);
         *dim_n = atoi(argv[3]);
      }
   }
   if (*dim_l<=0 || dim_n<=0 || dim_m<=0) {
      cout<<"Error: number of rows and/or columns must be greater than 0"
          << endl;
      exit(1);
   }
}

/*
   Routine that fills the number matrix with Random Data with values
   between 0 and MAX_VALUE
   This simulates in some way what might happen if there was a 
   single sequential data acquisition source such as a single file
*/
void fill_matrix(float *array,int dim_n,int dim_m)
{
#define M(i,j) *(array+i*dim_m+j)
   int i,j;
   for(i=0;i<dim_m;i++) {
      for (j=0;j<dim_n;j++) {
         array[i*dim_n+j]=drand48()*MAX_VALUE;
         M(i,j) = (i+1)*(j+2);
      }
   }
#undef M
}

/*
   Routine that outputs the matrices to the screen 
*/
void print_matrix(float *array,int dim_m,int dim_n)
{
   int i,j;
   for(i=0;i<dim_m;i++) {
      for (j=0;j<dim_n;j++) {
         cout << array[i*dim_n+j] << " ";
      }
      cout << endl;
   }
}

/*
   MAIN ROUTINE: summation of a number list
*/

int main( int argc, char *argv[])
{
   bool verbose = false;
   bool report_time = true;
   float *a,*b,*c,dot_prod;
   int dim_l,dim_n,dim_m;
   int i,j,k;

   /* 
   get matrix sizes
   */
   get_index_size(argc,argv,&dim_l,&dim_m,&dim_n);
  
   // dynamically allocate from heap the numbers in the memory space
   // for the a,b, and c matrices 
   a = new (nothrow) float[dim_l*dim_m];
   b = new (nothrow) float[dim_m*dim_n];
   c = new (nothrow) float[dim_l*dim_n];
   if(a==0 || b==0 || c==0) {
     cout <<"ERROR:  Insufficient Memory" << endl;
     exit(1);
   }
   
   /*
      initialize numbers matrix with random data
   */ 
   srand48(SEED);
   fill_matrix(a,dim_l,dim_m);
   fill_matrix(b,dim_m,dim_n);

   /*
     output numbers matrix
   */
   if (verbose) {
      cout << "A matrix =" << endl;
      print_matrix(a,dim_l,dim_m);
      cout << endl;

      cout << "B matrix =" << endl;
      print_matrix(b,dim_m,dim_n);
      cout << endl;
   }

   /*
   Start recording the execution time
   */
   TIMER_CLEAR;
   TIMER_START;

   // multiply local part of matrix
   for (i=0;i<dim_l;i++) {
      for (j=0;j<dim_n;j++) {
         dot_prod = 0.0;
         for (k=0;k<dim_m;k++) {
            dot_prod += A(i,k)*B(k,j);
         }
         C(i,j) = dot_prod;
      }
   }
   
   /*
      stop recording the execution time
   */ 
   TIMER_STOP;

   if (verbose) {
      cout << "C matrix =" << endl;
      print_matrix(c,dim_l,dim_n);
      cout << endl;
   }

   if (report_time) {
      cout << "time = " << setprecision(8) 
           << TIMER_ELAPSED/1000000.0 
           << " seconds" << endl;
   }
}

