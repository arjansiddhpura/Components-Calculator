# Components Calculator

A small project I worked on as a contract for a Swiss company developing a calculator to build topologically sorted trees out of an excel data sheet, such that the parts of the machines are connected as children to their parent nodes, repeatedly until all parts that are necessary for the machine are included. Data set included roughly 200,000 lines, each line providing a machine, its details and its respective parts. Lines below would go on to list details about the parts, their details, and their respective parts. Work done in Python. Code was gradually optimized to be done in less than 10 seconds from taking an hour. Output was a csv file with all the required data and a terminal output showing the structure of trees with additional calculation of requirements. Fun project!

A screenshot of some small trees:  

<img width="227" alt="image" src="https://user-images.githubusercontent.com/75858676/226181089-314df3c0-a67b-4845-9bb2-7b1a63b27428.png">
