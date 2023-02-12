from typing import List
from DocumentElement import DocumentElement, Variable, Class


class Document:
    element_list: List[DocumentElement]

    def __init__(self):
        self.element_list = []
        css_file = open('style.css', 'w')
        css_file.close()

    def add_child(self, doc_elem: DocumentElement):
        self.element_list.append(doc_elem)


if __name__ == '__main__':
    d = Document()

    d.add_child(Variable('v_1', type('string')))
    d.add_child(Class('c_1', [Variable('v_1', type('string')), Variable('v_1', type('string')),
                              Variable('v_1', type('string'))], []))
    for elem in d.element_list:
        elem.dprint()
        elem.write_html_element()

