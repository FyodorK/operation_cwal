#include "pch.h"
#include "divmul.h"
#include <iostream>
#include <assert.h>


void test1()
{
	int a{ 10 }, b{ 2 }, mult{ 0 }, div{ 0 }, res{ 0 }, ret{ 0 };

	ret = DivMul(a, b, &mult, &div, &res);

	assert(mult == 20);
	assert(div == 5);
	assert(res == 0);
	assert(ret == 0);

	std::cout << "Test 1 passed" << std::endl;
}


void test2()
{
	int a{ 0 }, b{ 10 }, mult{ 0 }, div{ 0 }, res{ 0 }, ret{ 0 };

	ret = DivMul(a, b, &mult, &div, &res);

	assert(mult == 0);
	assert(div == 0);
	assert(res == 0);
	assert(ret == 0);

	std::cout << "Test 2 passed" << std::endl;
}

void test3()
{
	int a{ 0 }, b{ -10 }, mult{ 0 }, div{ 0 }, res{ 0 }, ret{ 0 };

	ret = DivMul(a, b, &mult, &div, &res);

	assert(mult == 0);
	assert(div == 0);
	assert(res == 0);
	assert(ret == 0);

	std::cout << "Test 3 passed" << std::endl;
}


void test4()
{
	int a{ -10 }, b{ -10 }, mult{ 0 }, div{ 0 }, res{ 0 }, ret{ 0 };

	ret = DivMul(a, b, &mult, &div, &res);

	assert(mult == 100);
	assert(div == 1);
	assert(res == 0);
	assert(ret == 0);

	std::cout << "Test 4 passed" << std::endl;
}

void test5()
{
	int a{ 10 }, b{ -10 }, mult{ 0 }, div{ 0 }, res{ 0 }, ret{ 0 };

	ret = DivMul(a, b, &mult, &div, &res);

	assert(mult == -100);
	assert(div == -1);
	assert(res == 0);
	assert(ret == 0);

	std::cout << "Test 5 passed" << std::endl;
}

void test6()
{
	int a{ 10 }, b{ 3 }, mult{ 0 }, div{ 0 }, res{ 0 }, ret{ 0 };

	ret = DivMul(a, b, &mult, &div, &res);

	assert(mult == 30);
	assert(div == 3);
	assert(res == 1);
	assert(ret == 0);

	std::cout << "Test 6 passed" << std::endl;
}

void test7()
{
	int a{ 10 }, b{ 0 }, mult{ 0 }, div{ 0 }, res{ 0 }, ret{ 0 };

	ret = DivMul(a, b, &mult, &div, &res);

	assert(mult == 0);
	assert(div == 0);
	assert(res == 0);
	assert(ret == 1);

	std::cout << "Test 7 passed" << std::endl;
}

void test8()
{
	int a{ 10 }, b{ -0 }, mult{ 0 }, div{ 0 }, res{ 0 }, ret{ 0 };

	ret = DivMul(a, b, &mult, &div, &res);

	assert(mult == 0);
	assert(div == 0);
	assert(res == 0);
	assert(ret == 1);

	std::cout << "Test 8 passed" << std::endl;
}