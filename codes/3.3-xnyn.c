#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE* fp;

	// create a new file
	fp = fopen("values.dat", "w");

	// to check if file is created or not
	if(fp == NULL)
	{
		printf("Cannot open file\n");
		exit(1);
	}

	// defining array x
	int x[6] = {1, 2, 3, 4, 2, 1};

	// defning array y
	double y[20] = {0};

	y[0] = x[0];
	y[1] = -0.5*y[0]+x[1];

	for(int i=2; i<20; i++)
	{
		if(i < 6)
			y[i] = -0.5*y[i-1]+x[i]+x[i-2];

		else if(i > 5 && i < 8)
			y[i] = -0.5*y[i-1]+x[i-2];

		else
			y[i] = -0.5*y[i-1];
	}

	// To check y[]
	// for(int i=0; i<20; i++)
	// 	printf("%lf ", y[i]);

	// writing data on the file
	for(int i = 0; i<20; i++)
	{
		fprintf(fp, "%lf ", y[i]);
	}

	fclose(fp);

	return 0;
}
