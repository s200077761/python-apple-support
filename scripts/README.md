# Helper Scripts

This directory contains utility scripts to make working with Python Apple Support easier.

## Available Scripts

### check_system.py

Verifies that your system meets all requirements for building Python frameworks.

### welcome.py

Interactive introduction to the project with system information and quick commands.

### build_demo.py

Guided build process with progress tracking and error handling.

### generate_template.py

Generates starter templates for Python-powered Apple applications.

---

## Script Details

### check_system.py

Verifies that your system meets all requirements for building Python frameworks.

**Usage:**
```bash
python3 scripts/check_system.py
```

**Checks:**
- ✓ macOS Operating System
- ✓ Xcode installation
- ✓ Command Line Tools
- ✓ Python version (3.8+)
- ✓ Build tools (make, git)
- ✓ Disk space (10GB+)

**Exit Codes:**
- 0: All checks passed
- 1: One or more checks failed

---

### welcome.py

Interactive introduction to the project with system information and quick commands.

**Usage:**
```bash
python3 scripts/welcome.py
```

**Features:**
- Colorful, informative output
- System requirements check
- Project information display
- Supported platforms overview
- Quick command reference
- Suggested next steps

**Output:**
- Project configuration
- Available build targets
- Existing build artifacts
- Platform capabilities
- Helpful command list

---

### build_demo.py

Guided build process with progress tracking and error handling.

**Usage:**
```bash
# Basic usage
python3 scripts/build_demo.py --platform iOS

# With clean before build
python3 scripts/build_demo.py --platform macOS --clean

# Verbose output
python3 scripts/build_demo.py --platform tvOS --verbose
```

**Arguments:**
- `--platform, -p` (required): Apple platform to build for
  - Choices: macOS, iOS, tvOS, watchOS, visionOS
- `--clean, -c` (optional): Clean before building
- `--verbose, -v` (optional): Show detailed build output

**Features:**
- Step-by-step progress tracking
- Time estimation
- Error handling and reporting
- Build artifact verification
- Colorful status output
- Build time reporting

**Example:**
```bash
$ python3 scripts/build_demo.py --platform iOS

╔════════════════════════════════════════════════════════════╗
║  Building Python for iOS                                    ║
╚════════════════════════════════════════════════════════════╝

[Step 1/2] Building Python for iOS
ℹ This may take 30-60 minutes depending on your system...
✓ Building iOS completed
✓ Build completed in 42.3 minutes

[Step 2/2] Verifying build output
✓ Found 1 build artifact(s):
  → Python-3.14-iOS-support.custom.tar.gz (87.3 MB)

╔════════════════════════════════════════════════════════════╗
║  Build Successful! 🎉                                      ║
╚════════════════════════════════════════════════════════════╝
```

---

## Script Design

All scripts follow these conventions:

### Color Coding
- 🟢 Green (✓): Success/Pass
- 🔵 Cyan (ℹ): Information  
- 🟡 Yellow (⚠): Warning
- 🔴 Red (✗): Error/Fail

### Exit Codes
- 0: Success
- 1: Failure

### Requirements
- Python 3.8+
- macOS (for build scripts)
- No external dependencies (uses only stdlib)

## Creating Your Own Scripts

### generate_template.py

Generates starter templates for Python-powered Apple applications.

**Usage:**
```bash
# Generate iOS app template
python3 scripts/generate_template.py --platform iOS --name "MyApp"

# Generate macOS app template  
python3 scripts/generate_template.py --platform macOS --name "DesktopApp"

# Specify output directory
python3 scripts/generate_template.py -p visionOS -n "VisionApp" -o ~/Projects
```

**Arguments:**
- `--platform, -p` (required): Target platform (iOS, macOS, tvOS, watchOS, visionOS)
- `--name, -n` (optional): App name (default: MyPythonApp)
- `--output, -o` (optional): Output directory (default: ./template)

**Generated Files:**
- `ContentView.swift` - SwiftUI view with Python integration
- `app/main.py` - Python code for the app
- `README.md` - Setup and usage instructions

---

## Creating Your Own Scripts

Feel free to add your own helper scripts to this directory! Here's a template:

```python
#!/usr/bin/env python3
"""
Your Script Name - Brief Description

Detailed description of what your script does.
"""

import sys
from pathlib import Path

class Colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def main():
    """Main function."""
    print(f"{Colors.OKGREEN}Your script works!{Colors.ENDC}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

Make it executable:
```bash
chmod +x scripts/your_script.py
```

## Tips

1. **Start with check_system.py** - Always verify your system first
2. **Use welcome.py** - Get oriented before building
3. **Try build_demo.py** - Easier than using make directly
4. **Use --verbose** - When troubleshooting build issues
5. **Keep scripts simple** - These use only Python stdlib for portability

## Contributing

If you create useful scripts, consider:
- Following the existing patterns
- Adding documentation here
- Using consistent color coding
- Providing helpful error messages
- Including usage examples

---

**Note**: These scripts are part of the personal fork enhancements. They work alongside the original Makefile-based build system.
