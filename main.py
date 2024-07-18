from __future__ import annotations
from typing import List
from mesonbuild.mparser import Parser, FunctionNode, AssignmentNode
import json

filename = 'meson.build'
with open(filename, 'r') as meson_file:
    meson_file_content:str = meson_file.read()
    parser = Parser(meson_file_content, filename)
    parsed_lines = parser.parse().lines

    project_name:str = "DEFAULT"
    library_list:List[str] = []
    vcpkg_json_cont:dict = dict()

    for line in parsed_lines:
        if isinstance(line,FunctionNode):
            if(line.func_name.value == "project"):
                #Found project(), get name.
                project_name = line.args.arguments[0].value
                #print(project_name)
        if isinstance(line, AssignmentNode):
            if(isinstance(line.value, FunctionNode) and line.value.func_name.value == "dependency"):
                # Found dependency(), get library name.
                library_name: str = line.value.args.arguments[0].value
                library_list.append(library_name)
                #print(library_name)

    vcpkg_json_cont['name'] = project_name
    vcpkg_json_cont['version'] = '1'
    vcpkg_json_cont['description'] = 'Auto-generated vcpkg.json'
    vcpkg_json_cont['dependencies'] = library_list
    vcpkg_json_str:str = json.dumps(vcpkg_json_cont, indent=2, ensure_ascii=False)
    with open('vcpkg.json', 'w') as vfile:
        vfile.write(vcpkg_json_str)


