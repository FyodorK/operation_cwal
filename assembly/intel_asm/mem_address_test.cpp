#include "mem_addr.h"
#include "pch.h"
#include <iostream>

int test_mem_addr_01();

int test_mem_addr_01()
{
	for (int i = -1; i < NumFibVals_ + 1; i++)
	{
		int v1 = -1, v2 = -1, v3 = -1, v4 = -1;
		int rc = MemAddr(i, &v1, &v2, &v3, &v4);
		printf("i: %2d rc: %2d - ", i, rc);
		printf("v1: %5d v2: %5d v3: %5d v4: %5d\n", v1, v2, v3, v4);
	}
	return 0;
}