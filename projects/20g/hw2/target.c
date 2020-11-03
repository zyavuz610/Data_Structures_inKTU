#include <stdio.h>
int main(void) 
{
  printf("Data Structures\n");
  int i,n;
  i=0;
  for(i=2;i<5;i++)
  {
    n = i*i;
    if(n%2==0)
    {
      for(int j=0;j<n;j++)
      {
        printf("%d",i);
      }
      printf("%d",n);
    }
    else
    {
      printf("\n");
    }
  }
  return 0;
}