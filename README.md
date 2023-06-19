# Semantic analyzer for a compiler

## Class Definitions:

- BinaryOperation: Represents a binary operation with a left operand, an operator, and a right operand.
- Assignment: Represents an assignment statement with a variable and a value.
Variable: Represents a variable with a name.

## SemanticAnalyzer Class:

- Initializes the symbol_table attribute as an empty dictionary to store variable names and their types.
-The analyze method takes an Abstract Syntax Tree (AST) as input and calls the visit method to start the semantic analysis.
- The visit method dynamically calls the appropriate visitor method based on the type of the node in the AST.
- The generic_visit method raises an exception if there is no specific visitor method defined for a node type.
- The visit_BinaryOperation method visits the left and right nodes of the binary operation and performs semantic checks specific to the binary operation.
- The visit_Assignment method extracts the variable name and visits the value node of the assignment, then adds the variable name and its type to the symbol_table.
- The visit_Variable method retrieves the variable name, checks if it exists in the symbol_table, and returns its type. If the variable is not declared, it prints a warning message and returns None.


## Code Execution:

- An instance of SemanticAnalyzer is created.
- Variables 'x' and 'y' are declared in the symbol_table with the type 'int'.
- An AST is constructed with a binary operation (x + y) and an assignment to variable 'z'.
- The semantic analysis is performed by calling analyze on the SemanticAnalyzer instance.
- After the analysis, the contents of the symbol_table are printed, showing the variables and their types.
- The output of print(analyzer.symbol_table) should be:

`
{'x': 'int', 'y': 'int', 'z': 'int'}
`

indicating that variables 'x', 'y', and 'z' are declared with the type 'int' in the symbol_table.

Note: The code snippet provided only focuses on the semantic analysis part and does not cover the actual evaluation of the binary operations or handling other aspects of a compiler. It serves as a basic example to illustrate the concept of a semantic analyzer.