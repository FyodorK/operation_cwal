#include "pch.h"
#include "calcsum.h"
#include <iostream>
#include <assert.h>

void test_cs01() 
{
	int a{ 10 }, b{ 20 }, c{ 30 }, s1{ 0 }, s2{0}, s3{0};

	CalcSum(a, b, c, &s1, &s2, &s3);

	assert(s1 == 60);
	assert(s2 == 1400);
	assert(s3 == 36000);

	std::cout << "Test CalcSum 01 is passed" << std::endl;
}
