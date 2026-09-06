import os
import tempfile
from app.domain.tree_walker import get_files_to_parse

def test_tree_walker_respects_gitignore():
    # 1. Create a temporary directory for our test
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a .gitignore file
        with open(os.path.join(temp_dir, ".gitignore"), "w") as f:
            f.write("secret.txt\nnode_modules/\n")
            
        # Create a valid python file
        with open(os.path.join(temp_dir, "main.py"), "w") as f:
            f.write("print('hello')")
            
        # Create an ignored file
        with open(os.path.join(temp_dir, "secret.txt"), "w") as f:
            f.write("my password")
            
        # Create an ignored binary file (caught by our hardcoded extensions)
        with open(os.path.join(temp_dir, "image.png"), "w") as f:
            f.write("fake binary data")

        # 2. Run our tree walker
        valid_files = get_files_to_parse(temp_dir)
        
        # 3. Assert the results! 
        # It should ONLY find .gitignore and main.py
        file_names = [os.path.basename(path) for path in valid_files]
        
        assert "main.py" in file_names
        assert ".gitignore" in file_names
        assert "secret.txt" not in file_names
        assert "image.png" not in file_names
