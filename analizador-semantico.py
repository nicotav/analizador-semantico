class BinaryOperation:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Assignment:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

class Variable:
    def __init__(self, name):
        self.name = name

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, ast):
        self.visit(ast)

    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise NotImplementedError(f"No visit_{type(node).__name__} method defined")

    def visit_BinaryOperation(self, node):
        self.visit(node.left)
        self.visit(node.right)
        # Perform semantic checks for binary operation

    def visit_Assignment(self, node):
        variable_name = node.variable.name
        variable_type = self.visit(node.value)
        self.symbol_table[variable_name] = variable_type

    def visit_Variable(self, node):
        variable_name = node.name
        if variable_name not in self.symbol_table:
            print(f"Warning: Variable '{variable_name}' has not been declared")
            return None  # Return None for undeclared variables
        return self.symbol_table[variable_name]


# Create the semantic analyzer
analyzer = SemanticAnalyzer()

# Declare variables
analyzer.symbol_table['x'] = 'int'
analyzer.symbol_table['y'] = 'int'

# Construct an AST representing an operation and an assignment
ast = BinaryOperation(
    left=Variable("x"),
    operator="+",
    right=Variable("y")
)
assignment = Assignment(
    variable=Variable("z"),
    value=ast
)

# Perform the analysis
results = analyzer.analyze(assignment)

print(analyzer.symbol_table)
# {'x': 'int', 'y': 'int', 'z': 'int'}

