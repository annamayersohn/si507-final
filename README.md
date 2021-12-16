# Instructions

This program produces tables and graphs showing the evolution of related names through different languages. The code requires the plotly and Beautiful Soup (bs4) packages to run. To run the program, simply open and run the main.py file. Each prompt consists of a list of options printed to the command line. The user can select an option by typing the number that corresponds to their choice and pressing enter. Each table or graph generated will open in a new tab in the user's default browser.

In the first part of this program, the user is given a list of seven names and enters a number corresponding to the name whose ancestry they wish to see. A table will open in which each row describes a step in the chosen name's evolution, starting with the chosen name and working backwards. After the table is generated, the user can choose either to see the list again and choose another name to generate another table, or to move on to the second part. In the second part, the user will progressively narrow down the full family tree. Once a sufficiently narrow sub-section has been chosen, a treemmap will be generated showing only the chosen branch of the tree. Then the user has the option of repeating this part of the program or ending the program.

# Data Structure

The data structure is a tree, in which each node may have any number of children. The root node of the tree is the word _chanan_, from which all the names in the tree are derived. Each node is the tree represents a step in the evolution of this word into other forms. The source of the data is behindthename.com, mainly behindthename.com/name/anna/tree. The file tree_json.json contains the data from the website; main.py reads this JSON data into a tree.

Each object in the tree is an instance of the Node class (defined in class_constructor.py), and most of them are instances of the Name subclass. One of the properties of a Node/Name is **children**, the value of which is a list of the Nodes/Names that are children of the current Node/Name. This property establishes the edges amongst the nodes in the tree.