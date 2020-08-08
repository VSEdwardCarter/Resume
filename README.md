# Resume
Given the following scenario, I was tasked to create a repository for a school concerng students and their degree paths:

You are hired as a contractor to help a university migrate an existing student system to a new platform using C++ language. Since the application already exists, its requirements exist as well, and they are outlined in the next section. You are responsible for implementing the part of the system based on these requirements. A list of data is provided as part of these requirements. This part of the system is responsible for reading and manipulating the provided data.



You must write a program containing five classes (i.e.,  Student , SecurityStudent , NetworkStudent , SoftwareStudent , and  Roster ). The program will maintain a current roster of students within a given course. Student data for the program includes student ID, first name, last name, email address, age, an array of the number of days to complete each course, and degree. This information can be found in the studentData table below. The program will read a list of five students and use function calls to manipulate data (see part F4 in the requirements below). While parsing the list of data, the program should create student objects using the appropriate subclasses indicated by the degree program. The entire student list will be stored in one array of students called  classRosterArray Specific data-related output will be directed to the console. 


F.  Demonstrate the program’s required functionality by adding a void main() function to roster.cpp, which will contain the required function calls to achieve the following results:

4.  Convert the following pseudo code to complete the rest of the main() function:
classRoster.printAll();
classRoster.printInvalidEmails();
//loop through classRosterArray and for each element:
classRoster.printAverageDaysInCourse(/*current_object's student id*/);
classRoster.printByDegreeProgram(SOFTWARE);
classRoster.remove("A3");
classRoster.remove("A3");
 //expected: the above line should print a message saying such a student with this ID was not found.
