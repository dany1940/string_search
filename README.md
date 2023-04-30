#### Table of Contents
- [Table of Contents](#table-of-contents)
- [Thechnologies](#thechnologies)
- [Instalation](#instalation)
- [Structure and Usage](#structure-and-usage)
- [Suport](#suport)
- [License](#license)

&nbsp;&nbsp;&nbsp;&nbsp;The project aims to find patterns in a file based on the last line in the file beeing the pattern, a single word.<br />


 #### Thechnologies

&nbsp;&nbsp;&nbsp;&nbsp;Python  version 3.10

#### Instalation

 &nbsp;&nbsp;&nbsp;&nbsp;The Code will run only with Python 3.10 or newer version.<br />


#### Structure and Usage

&nbsp;&nbsp;&nbsp;&nbsp;The project has one branch Master.<br />
&nbsp;&nbsp;&nbsp;&nbsp;1.Master branch has 1 package: string_search<br />
&nbsp;&nbsp;&nbsp;&nbsp;2.Inside this package you have the following python files: main.py, pattern.py, get_file_path.py, arguments.py, test.txt file and a  shell script file: solution <br />
&nbsp;&nbsp;&nbsp;&nbsp;3.Read the coments on the top of each file for details on the code functionality <br />
&nbsp;&nbsp;&nbsp;&nbsp;4.The code uses only build in packages such as Path, re and argparse and is written in python and assume that you are ussing a UNIX / Linux enviroment <br />
&nbsp;&nbsp;&nbsp;&nbsp;5.You need to use the command 'cd' to change directory The code is runned from inside the folder string_search <br />
&nbsp;&nbsp;&nbsp;&nbsp;6.You need to give the file 'solution' executable permisions, mainly using the command 'chmod 755' or similar<br />
&nbsp;&nbsp;&nbsp;&nbsp;7.The code is runned using defaults cli rguments implemented with argparse and using the command './solution path'  where path is the path of the file<br />
&nbsp;&nbsp;&nbsp;&nbsp;8.Assuming that searched term is a word with at least on e letter and it can have both capital and lower case letter, that is possible to pass an ampty file with tabs / or empty spaces which once removed would raise an index error, that exist the possibility to have a greater pattern than every single line<br />






#### Suport

   For any help please email:<br />
      gsecomerce@gmail.com

#### License

   MIT LICENSE





