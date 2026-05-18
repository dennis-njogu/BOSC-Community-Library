# 🛠️ Scripts & Automation Tools

This section contains utility scripts for managing, searching, and maintaining the BOSC Community Library.

---

## 📋 Available Scripts

### 🔍 [search_resources.py](search_resources.py)
Search and discover educational resources.

**Usage:**
```bash
python scripts/search_resources.py "query"
```

**Examples:**
```bash
# Search by subject
python scripts/search_resources.py "mathematics"

# Search by language
python scripts/search_resources.py "kiswahili"

# Search by difficulty
python scripts/search_resources.py "beginner"

# Combined search
python scripts/search_resources.py "mathematics kiswahili beginner"
```

**Output:**
- Matching resources
- File locations
- Brief descriptions

---

### 🚀 [setup.py](setup.py)
Install project dependencies and set up environment.

**Usage:**
```bash
python scripts/setup.py
```

**What it does:**
- ✅ Checks Python version
- ✅ Creates virtual environment (if needed)
- ✅ Installs dependencies from requirements.txt
- ✅ Runs initial setup tasks
- ✅ Verifies installation

**Output:**
- Installation status
- Setup summary
- Any warnings or errors

---

## 🚀 Running Scripts

### Basic Usage

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat  # Windows

# Run a script
python scripts/script_name.py [arguments]
```

### Required Environment

- Python 3.8+
- Virtual environment activated
- Dependencies installed (run `python scripts/setup.py`)

### Error Handling

```bash
# If script not found
# Make sure you're in project root:
cd BOSC-Community-Library
python scripts/search_resources.py "query"

# If permission denied (macOS/Linux)
chmod +x scripts/*.py
python scripts/script_name.py
```

---

## 📝 Creating New Scripts

### Script Template

Create new scripts following this pattern:

```python
#!/usr/bin/env python3
"""
Script description - one line summary.

Longer description explaining what the script does,
how it works, and what output to expect.
"""

import sys
import argparse

def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Script description'
    )
    parser.add_argument('query', help='Search query')
    parser.add_argument(
        '--verbose', 
        action='store_true', 
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    # Your code here
    print(f"Processing: {args.query}")

if __name__ == '__main__':
    main()
```

### Script Checklist

Before submitting a new script:

- ✅ Clear, descriptive name (`verb_noun.py`)
- ✅ Docstring explaining purpose
- ✅ Command-line arguments with help text
- ✅ Error handling for invalid input
- ✅ Tests written and passing
- ✅ README documentation updated
- ✅ No hardcoded paths (use config files)
- ✅ Compatible with Python 3.8+

### Adding to README

Add script description to this file:

```markdown
### 📋 [script_name.py](script_name.py)
Brief description.

**Usage:**
\`\`\`bash
python scripts/script_name.py [args]
\`\`\`

**Examples:**
\`\`\`bash
...
\`\`\`
```

---

## 🔧 Script Categories

### Resource Management
- `search_resources.py` — Search and discover resources

### Project Setup
- `setup.py` — Initial setup and installation
- (Add others as needed)

### Development Tools
- (To be added)

### Deployment & Maintenance
- (To be added)

---

## 📦 Dependencies

Scripts use the following Python packages:

**Core:**
- Python 3.8+
- Standard library modules

**Optional:**
- `click` — Command-line interface
- `requests` — HTTP requests
- `python-dotenv` — Environment variable loading

See [requirements.txt](../requirements.txt) for complete list.

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named..."

```bash
# Solution: Install dependencies
python scripts/setup.py

# Or install manually:
pip install -r requirements.txt
```

### "Permission denied" (macOS/Linux)

```bash
# Make script executable:
chmod +x scripts/script_name.py

# Then run:
python scripts/script_name.py
```

### "Python command not found"

```bash
# Use Python 3 explicitly:
python3 scripts/script_name.py

# Or activate virtual environment:
source venv/bin/activate
python scripts/script_name.py
```

---

## 📖 Script Development Guide

### Best Practices

✅ **Clear Names** — Use `verb_noun.py` format  
✅ **Documentation** — Include docstrings and help text  
✅ **Error Handling** — Handle edge cases gracefully  
✅ **Testing** — Write tests for your script  
✅ **Logging** — Add debug/verbose output  
✅ **Config** — Use config files, not hardcoded values  
✅ **Performance** — Optimize for large datasets  
✅ **Compatibility** — Support Python 3.8+  

### Example: Complete Script

```python
#!/usr/bin/env python3
"""
search_resources.py - Search educational resources.

Searches the resource library for matching topics,
languages, and difficulty levels.
"""

import os
import argparse
from pathlib import Path

def search_resources(query, verbose=False):
    """
    Search for resources matching query.
    
    Args:
        query (str): Search term
        verbose (bool): Print detailed info
    
    Returns:
        list: Matching resources
    """
    resources_dir = Path(__file__).parent.parent / 'resources'
    results = []
    
    # Search implementation
    for resource_file in resources_dir.rglob('*.md'):
        with open(resource_file) as f:
            content = f.read()
            if query.lower() in content.lower():
                results.append(resource_file)
                if verbose:
                    print(f"Found: {resource_file}")
    
    return results

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Search educational resources'
    )
    parser.add_argument('query', help='Search query')
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    results = search_resources(args.query, args.verbose)
    
    print(f"\nFound {len(results)} matching resources:")
    for result in results:
        print(f"  - {result}")

if __name__ == '__main__':
    main()
```

---

## 🤝 Contributing Scripts

### To Add a New Script

1. Create script following [template](#script-template)
2. Write tests for the script
3. Add documentation to this README
4. Submit as PR
5. Include usage examples
6. Request review from maintainers

### Script Suggestions

Have an idea for a useful script? 
- Open a GitHub Issue describing what it should do
- Include use cases and examples
- Community might help implement it!

---

## 📞 Getting Help

### Script Not Working?

1. Check [Troubleshooting](#troubleshooting) section
2. Verify Python version: `python --version`
3. Check dependencies installed: `pip list`
4. Try with `--verbose` flag if available
5. Open GitHub Issue with:
   - Script name and command
   - Error message
   - Your environment (OS, Python version)

### How to Use a Script?

1. Check this README for documentation
2. Run with `--help` for more info:
   ```bash
   python scripts/script_name.py --help
   ```
3. See examples section above
4. Check script docstring: `python -c "import scripts.script_name; help(scripts.script_name)"`

---

## 📚 More Information

- [Installation Guide](../docs/deployment/installation.md) — Setup
- [Architecture Docs](../docs/architecture.md) — System design
- [Contributing Guide](../GETTING_STARTED.md) — How to contribute
- [Main README](../README.md) — Project overview

---

**[← Back to Main README](../README.md)**

---

*Want to add a useful script? See [Contributing Scripts](#contributing-scripts)*
