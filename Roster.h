#pragma once
#include<iostream>
#include<string>
#include"Student.h"
#include <string>
using std::string;

const int numStudents = 5;



class Roster {
public:
	int lastIndex;
	int capacity;
	Student** roster;
	Roster();
	Roster(int capacity);
	void parseAdd(string datarow);
	void print_All();
	void remove(string StudentID);
	void printAveragedIC(string StudentID);
	void printInvalidEmail();
	void printByDegreeProgram(DegreeProgram b);
	~Roster();
};

