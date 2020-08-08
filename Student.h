#pragma once
#pragma once
#include<string>
#include"Degree.h"
#include<iostream>
using std::string;

class Student {
	protected:
		string StudentID;
		string firstName;
		string lastName;
		string emailAddress;
		string age;
		int* dIC;
		DegreeProgram type;

	public:
		const static int daysINCourse = 3;
		Student();
		Student(string ID, string fName, string lName, string email, string age, int dIC[], DegreeProgram type);

	//Getters
		string getID();
		string getfName();
		string getlName();
		string getemail();
		string getage();
		int* getdIC();
		virtual DegreeProgram getDegreeProgram() = 0;

	//Setters
		void setID(string ID);
		void setfName(string fName);
		void setlName(string lName);
		void setemail(string email);
		void setage(string age);
		void setdIC(int dIC[]);
		virtual void setDegreeProgram (DegreeProgram b) = 0;
		
		virtual void print() = 0;

	//Destructor
		~Student();
};