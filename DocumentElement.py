from typing import List


class DocumentElement:
    document_name: str

    def __init__(self):
        pass

    def dprint(self):
        pass

    def write_html_element(self):
        pass


class Variable(DocumentElement):
    variable_name: str
    variable_type: str

    def __init__(self, v_name: str = '', v_type: type = None):
        super().__init__()
        self.variable_name = v_name
        self.variable_type = v_type

    def dprint(self):
        super().dprint()
        print(self.variable_name, ':', self.variable_type)

    def write_html_element(self):
        file = open(f'.\\{self.variable_name}_var.html', 'w')
        file.write(f'<!DOCTYPE html>' +
                   f'<html>' +
                   f'<body>' +
                   f'<h1>{self.variable_name}</h1>' +
                   f'<p>{self.variable_type.__name__}</p>' +
                   f'<p>Insert Variable Description Here</p>' +
                   f'</body>' +
                   f'</html>')
        file.close()


class Function(DocumentElement):
    function_name: str
    function_parameters: List[Variable]
    function_return_type: type

    def __init__(self, f_name: str = '', f_parameters: List[Variable] = [], f_return_type: type = None):
        super().__init__()
        self.function_name = f_name
        self.function_parameters = f_parameters
        self.function_return_type = f_return_type

    def dprint(self):
        super().dprint()
        print(self.function_name, ':', self.function_parameters, ':', self.function_return_type)

    def write_html_element(self):
        file = open(f'.\\{self.function_name}_func.html', 'w')
        file.write(f'<!DOCTYPE html>' +
                   f'<html>' +
                   f'<body>' +
                   f'<h1>{self.function_name} : {self.function_return_type.__name__}</h1>' +
                   f'<h2>Parameters: {self.function_parameters}</h2>' +
                   f'<p>Insert Function Description Here</p>' +  # needs to detect python comments for this
                   f'</body>' +
                   f'</html>')
        file.close()


class Class(DocumentElement):
    class_name: str
    class_objects: List[Variable]
    class_functions: List[Function]

    def __init__(self, c_name: str = '', c_objects: List[Variable] = [], c_functions: List[Function] = []):
        super().__init__()
        self.class_name = c_name
        self.class_objects = c_objects
        self.class_functions = c_functions

    def add_object(self, c_object: Variable):
        self.class_objects.append(c_object)

    def add_function(self, c_function: Function):
        self.class_functions.append(c_function)

    def dprint(self):
        super().dprint()
        print(self.class_name, ':', self.class_objects, ':', self.class_functions)

    def write_html_element(self):
        file = open(f'.\\{self.class_name}_class.html', 'w')
        file.write(f'<!DOCTYPE html>' +
                   f'<html>' +
                   f'<body>' +
                   f'<h1>{self.class_name}</h1>' +
                   f'<p>Insert Class Description Here<p>'
                   f'<h2>Instance Variables: </h2>' +
                   f'<p>{self.class_objects}</p>' +  # will use recursion eventuall
                   f'<h2>Instance Functions</h2>' +
                   f'<p>{self.class_functions}</p>' +  # will use recursion eventuall
                   f'</body>' +
                   f'</html>')
        file.close()
