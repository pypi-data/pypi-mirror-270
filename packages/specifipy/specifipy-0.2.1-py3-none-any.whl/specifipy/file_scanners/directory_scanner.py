import os

from py_d2 import D2Diagram

from specifipy.diagram_engines.hashable_connection import D2HashableConnection
from specifipy.parsers.diagram_generator_d2 import DiagramGenerator


class DirectoryScanner:
    scan_path: str = None
    full_dir_paths: list[str] = []
    full_file_paths: list[str] = []

    def __matches_file_classification(self, full_file_path) -> bool:
        file_name = full_file_path.split("/")[-1]
        return (
            os.path.isfile(full_file_path)
            and file_name[0] != "."
            and file_name[-3:] == ".py"
        )

    def __matches_directory_classification(self, full_dir_path) -> bool:
        dir_name: str = full_dir_path.split("/")[-1]
        return (
            os.path.isdir(full_dir_path)
            and dir_name[0] != "."
            and not "venv" in dir_name
            and not "virtualenv" in dir_name
        )

    def __init__(self, base_path: str):
        self.scan_path = os.path.abspath(base_path)
        for obj in os.listdir(self.scan_path):
            os.path.join(self.scan_path, obj)
        file_system_element: str

        # Perform initial directories scanning
        self.full_dir_paths = [
            os.path.join(self.scan_path, file_system_element)
            for file_system_element in os.listdir(self.scan_path)
            if self.__matches_directory_classification(
                os.path.join(self.scan_path, file_system_element)
            )
        ]

        # Perform initial files scanning
        self.full_file_paths = [
            os.path.join(self.scan_path, file_system_element)
            for file_system_element in os.listdir(self.scan_path)
            if self.__matches_file_classification(
                os.path.join(self.scan_path, file_system_element)
            )
        ]

        self.do_recursive_directory_scanning()

    def show_vars(self):
        print(self.full_dir_paths, self.full_file_paths)

    def make_diagrams(
        self,
        collect_files=True,
        file_name_containers=False,
        base_path: str | None = None,
    ):
        diagram_generator = DiagramGenerator()
        diagrams: list[D2Diagram] = []
        for f in self.full_file_paths:
            name = f.split("/")[-1]
            with open(f) as python_file:
                diagram = diagram_generator.generate_diagram(
                    python_file.read(),
                    name,
                    base_path=base_path,
                    save_file=not collect_files,
                    file_name_container=file_name_containers,
                )
                if collect_files and diagram:
                    diagrams.append(diagram)
        if diagrams:
            classes = sum([diagram.shapes for diagram in diagrams], [])
            connections = [
                D2HashableConnection(x.shape_1, x.shape_2, x.label, x.direction)
                for x in sum([diagram.connections for diagram in diagrams], [])
            ]
            diagram_generator.save_diagram_to_file(
                base_path if base_path else "./",
                D2Diagram(classes, list(set(connections))),
                "code_diagrams",
            )

    def do_recursive_directory_scanning(self):
        new_found_directory_paths: list[str] = []
        if self.full_dir_paths:
            directory_path: str
            for directory_path in self.full_dir_paths:
                for file_system_element in os.listdir(directory_path):
                    full_file_path = os.path.join(directory_path, file_system_element)
                    if os.path.isdir(full_file_path):
                        new_found_directory_paths.append(
                            os.path.join(directory_path, file_system_element)
                        )
                    if os.path.isfile(
                        full_file_path
                    ) and self.__matches_file_classification(full_file_path):
                        self.full_file_paths.append(
                            os.path.join(directory_path, file_system_element)
                        )
            self.full_dir_paths = new_found_directory_paths
            self.do_recursive_directory_scanning()
