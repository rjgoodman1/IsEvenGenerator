import sys
import subprocess
 
# total arguments
n = len(sys.argv)

# Argument Sanitation
if n > 3: print("Please provide positive integer n to generate IsEvenProgram and integer to test evenness")
if int(sys.argv[1]) < 0: 
    print("Please provide positive integer n to generate IsEvenProgram")
    exit
inverseN = -1 * int(sys.argv[1])
check = sys.argv[2]

# Generate Cmake File
cmake = open("CMakeLists.txt", "w")
cmake.write("cmake_minimum_required (VERSION 2.8.11)\n")
cmake.write("project(IsEven)\n")
cmake.write("add_executable(IsEven IsEven.cpp)\n")
cmake.close()

# Generate IsEven.cpp
cpp = open("IsEven.cpp", "w")
cpp.write("#include <iostream>\n\n")
cpp.write("using namespace std;\n\n")
cpp.write("int main(int argc, char** argv)\n")
cpp.write("{\n")
cpp.write("\tif (argc > 2) cout << \"Please Provide an integer value between " + str(inverseN) + " to " + sys.argv[1] + "\"<< endl;\n")     
cpp.write("\telse\n")
cpp.write("\t{\n")
cpp.write("\t\tint n = atoi(argv[1]);\n")
cpp.write("\t\tswitch (n)\n")
cpp.write("\t\t{\n")

while inverseN <= int(sys.argv[1]):
    if inverseN % 2 == 0:
        cpp.write("\t\t\tcase " + str(inverseN) +":\n")
        cpp.write("\t\t\t\tcout << n << \" is even\" << endl;\n")
        cpp.write("\t\t\t\tbreak;\n")
    else:
        cpp.write("\t\t\tcase " + str(inverseN) +":\n")
        cpp.write("\t\t\t\tcout << n << \" is not even\" << endl;\n")
        cpp.write("\t\t\t\tbreak;\n")
    inverseN += 1

cpp.write("\t\t\tdefault: cout << \"Unknown Value cant determine Evenness\" << endl;\n")
cpp.write("\t\t}\n")
cpp.write("\t}\n")
cpp.write("\treturn 0;\n")
cpp.write("}\n")
cpp.close()

# Compile IsEven.exe
subprocess.call(["cmake"])
subprocess.call(["make"])

