import networkx as nx
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY_LANGUAGE=Language(tspython.language())

class CallGraphBuilder:
    def __init__(self):
        self.parser=Parser(PY_LANGUAGE)
        self.func_query=Query(PY_LANGUAGE, "(function_definition name: (identifier) @func_name)")
        self.call_query=Query(PY_LANGUAGE, "(call function : (identifier) @call_name)")

    def build_graph(self, code_content:str) -> nx.DiGraph:
        graph=nx.DiGraph()

        code_bytes= code_content.encode("utf-8")
        tree= self.parser.parse(code_bytes)

        cursor=QueryCursor(self.func_query)
        matches= cursor.matches(tree.root_node)

        for match in matches:
            func_name_node = list(match[1].values())[0][0]
            caller_name= code_bytes[func_name_node.start_byte : func_name_node.end_byte].decode("utf-8")

            graph.add_node(caller_name)

            func_def_node= func_name_node.parent

            call_cursor=QueryCursor(self.call_query)
            call_matches= call_cursor.matches(func_def_node)

            for cmatch in call_matches : 
                call_name_node= list(cmatch[1].values())[0][0]
                callee_name= code_bytes[call_name_node.start_byte : call_name_node.end_byte].decode("utf-8")

                graph.add_edge(caller_name, callee_name)

        return graph
    