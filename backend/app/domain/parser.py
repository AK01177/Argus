import tree_sitter_python as tspython
import tree_sitter_javascript as tsjavascript
from tree_sitter import  Language, Parser, Query, QueryCursor

PY_LANGUAGE= Language(tspython.language())
JS_LANGAUGE= Language(tsjavascript.language())

class TreeSitterParser:
    def __init__(self):
        self.parser=Parser()

    def _get_language(self, file_path: str) -> Language| None:
        if file_path.endswith(".py"):
            return PY_LANGUAGE
        if file_path.endswith(".js") or file_path.endswith(".ts") or file_path.endswith(".jsx") or file_path.endswith("tsx") : 
            return JS_LANGAUGE
        return None

    def extract_chunks(self, file_path: str, code_content: str) -> list[str]:
        language=self._get_language(file_path)
        if not language:
            return [code_content]

        self.parser.language= language

        code_bytes= code_content.encode("utf-8")
        tree= self.parser.parse(code_bytes)

        query_string="""(function_definition) @function
        (class_definition) @class"""

        if language == JS_LANGAUGE:
            query_string="""(function_declaration) @function
            (class_declaration) @class
            (arrow_function) @arrow"""

        query= Query(language, query_string)
        cursor = QueryCursor(query)
        matches = cursor.matches(tree.root_node)

        chunks=[]
        for match in matches:
            match_dict=match[1]

            for nodes in match_dict.values():
                for node in nodes:
                    chunk_bytes= code_bytes[node.start_byte : node.end_byte]
                    chunks.append(chunk_bytes.decode("utf-8"))

        if not chunks:
            return [code_content]

        return chunks