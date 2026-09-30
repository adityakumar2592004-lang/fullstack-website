import ast
from typing import Tuple, Optional

FORBIDDEN_MODULES = {
    "os", "subprocess", "ctypes", "pty", "socket", "urllib", "requests",
    "http", "shutil", "multiprocessing", "threading", "signal", "posix",
    "winreg", "webbrowser", "sys"
}

FORBIDDEN_CALLS = {
    "eval", "exec", "compile", "__import__"
}

FORBIDDEN_ATTRS = {
    "__subclasses__", "__bases__", "__mro__", "__globals__", "__builtins__"
}

def validate_code_security(code: str) -> Tuple[bool, Optional[str]]:
    """
    Statically analyzes user code AST to block malicious modules and sandbox escape vectors
    while allowing all standard DSA libraries (math, collections, heapq, bisect, etc.).
    """
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        # Syntax error will be reported with precise line number in test runner
        return True, None

    for node in ast.walk(tree):
        # 1. Check imports: import os, import socket, etc.
        if isinstance(node, ast.Import):
            for alias in node.names:
                root_module = alias.name.split('.')[0]
                if root_module in FORBIDDEN_MODULES:
                    return False, f"Security Violation (line {node.lineno}): Importing '{alias.name}' is not allowed in the DSA sandbox."

        # 2. Check from X import Y
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root_module = node.module.split('.')[0]
                if root_module in FORBIDDEN_MODULES:
                    return False, f"Security Violation (line {node.lineno}): Importing from '{node.module}' is not allowed in the DSA sandbox."

        # 3. Check forbidden function calls
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id in FORBIDDEN_CALLS:
                    return False, f"Security Violation (line {node.lineno}): Function '{node.func.id}()' is prohibited."

        # 4. Check forbidden attribute accesses (e.g. obj.__subclasses__)
        elif isinstance(node, ast.Attribute):
            if node.attr in FORBIDDEN_ATTRS:
                return False, f"Security Violation (line {node.lineno}): Access to attribute '{node.attr}' is restricted."

    return True, None
