# Thesaurus Client and Server

>**Note: This project is submitted as part of class projects for CSE 5306 at University of Texas Arlington**

>**This code should not be used for the course CSE 5306 offered at University of Texas Arlington**

### Requirements:

* Python 3.6.2 or later
* AppJar library(Included in the project)

### Download links:

* [Python v3.6.2](https://www.python.org/downloads/)
* [AppJar library](http://appjar.info/)

### Setup:
The project is designed to run in python 3. I recommend to check the library requirements before running the project in later or before versions.

### Project execution:

##### Server
`python Server.py "ip_address" port_number`

To use the default *ip address* and *port number* use the command: 
`python Server.py --default`

Refer **--help** for more information:  
`python Server.py --help`

##### Client
`python Client.py "ip_address" port_number`

To use the default *ip address* and *port number* use the command: 
`python Client.py --default`

Refer **--help** for more information:
`python Client.py --help`

#### Limitations:

* The server and client are designed to run locally. Modifications might be required to run in remote environment.
* The code is designed to handle five clients. (i.e, up to five synonym requests)
    >The server is designed only for five clients as per the project requirement.

#### Additional information:

For additional information refer the project wiki.
