class codeparser:
    """Base class"""

    def parse_file(self, file_path, content):
        raise NotImplementedError("Subclass must implement the parse_file method")

class basicparser(codeparser):
    "Prototype"

    def parse_file(self, file_path, content):
        lines=content.split('\n')
        return{"file_path": file_path,
               "lines":len(lines),
               "size": len(content),
               "status": "Parsed Yippeeee!!!"}