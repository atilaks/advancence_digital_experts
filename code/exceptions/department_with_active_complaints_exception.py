""""No puede borrar un departamento que contenga quejas:
        -Test: l74(code_department_test)
        -Código: l51(code_department)"""


class DepartmentWithActiveComplaintsException(Exception):
    pass
