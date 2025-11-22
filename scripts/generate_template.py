#!/usr/bin/env python3
"""
Example Template Generator for Python Apple Support

This script generates starter templates for creating Python-powered Apple apps.
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime

TEMPLATES = {
    'ios': {
        'name': 'iOS App with Python',
        'description': 'iPhone/iPad app template',
        'files': ['ContentView.swift', 'AppDelegate.swift', 'main.py']
    },
    'macos': {
        'name': 'macOS App with Python',
        'description': 'Desktop Mac app template',
        'files': ['ContentView.swift', 'AppDelegate.swift', 'main.py']
    },
    'watchos': {
        'name': 'watchOS App with Python',
        'description': 'Apple Watch app template',
        'files': ['ContentView.swift', 'main.py']
    },
    'tvos': {
        'name': 'tvOS App with Python',
        'description': 'Apple TV app template',
        'files': ['ContentView.swift', 'main.py']
    },
    'visionos': {
        'name': 'visionOS App with Python',
        'description': 'Vision Pro app template',
        'files': ['ContentView.swift', 'main.py']
    }
}

SWIFT_TEMPLATE = '''//
//  ContentView.swift
//  {app_name}
//
//  Created by s200077761 on {date}
//  Python Apple Support Example
//
//  Note: This template uses SwiftUI and the Python C API.
//  The 'import Python' statement gives access to Python C API functions.
//  Make sure Python.xcframework is added to your project and set to "Embed & Sign".
//

import SwiftUI
import Python

struct ContentView: View {{
    @State private var pythonOutput: String = "Initializing Python..."
    @State private var isInitialized: Bool = false
    
    var body: some View {{
        VStack(spacing: 20) {{
            Text("{app_name}")
                .font(.largeTitle)
                .bold()
            
            Text(pythonOutput)
                .padding()
                .multilineTextAlignment(.center)
            
            if isInitialized {{
                Button("Run Python Code") {{
                    runPythonCode()
                }}
                .buttonStyle(.borderedProminent)
            }}
        }}
        .padding()
        .onAppear {{
            initializePython()
        }}
    }}
    
    func initializePython() {{
        guard let pythonHome = Bundle.main.path(forResource: "python", ofType: nil) else {{
            pythonOutput = "Error: Python framework not found in bundle"
            return
        }}
        
        let appPath = Bundle.main.path(forResource: "app", ofType: nil)
        
        setenv("PYTHONHOME", pythonHome, 1)
        if let appPath = appPath {{
            setenv("PYTHONPATH", appPath, 1)
        }}
        
        Py_Initialize()
        
        isInitialized = true
        pythonOutput = "Python initialized successfully!\\nTap button to run Python code."
    }}
    
    func runPythonCode() {{
        // Run the main.py script
        let code = """
        import sys
        try:
            with open('app/main.py', 'r') as f:
                exec(f.read())
        except Exception as e:
            print(f"Error: {{e}}")
        """
        
        PyRun_SimpleString(code)
        pythonOutput = "Python code executed!\\nCheck Xcode console for output."
    }}
}}

#Preview {{
    ContentView()
}}
'''

PYTHON_TEMPLATE = '''#!/usr/bin/env python3
"""
{app_name} - Python Module
Created by s200077761 on {date}

This is the main Python code for your {platform} app.
"""

import sys
import platform

def main():
    """Main function - customize this with your app logic."""
    print("=" * 50)
    print("Hello from Python on {platform}!")
    print("=" * 50)
    
    # System information
    print(f"\\nPython Version: {{sys.version_info.major}}.{{sys.version_info.minor}}.{{sys.version_info.micro}}")
    print(f"Platform: {{sys.platform}}")
    print(f"Architecture: {{platform.machine()}}")
    
    # Your app logic here
    print("\\n✓ Python is running successfully!")
    print("\\nCustomize this file (app/main.py) with your own code!")
    
    # Example: Simple calculation
    result = calculate_example()
    print(f"\\nExample calculation: {{result}}")
    
    return 0

def calculate_example():
    """Example function - replace with your own."""
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    average = total / len(numbers)
    return f"Sum={{total}}, Average={{average}}"

if __name__ == "__main__":
    sys.exit(main())
'''

README_TEMPLATE = '''# {app_name}

A Python-powered {platform} application.

Created with Python Apple Support by s200077761 on {date}

## Files

- `ContentView.swift` - Main SwiftUI view with Python integration
- `app/main.py` - Python code that runs in the app
- `README.md` - This file

## Setup Instructions

1. **Create Xcode Project**
   - Open Xcode
   - Create new {platform} App
   - Choose SwiftUI for interface

2. **Add Python Framework**
   - Build Python framework: `python3 scripts/build_demo.py --platform {platform_lower}`
   - Extract `Python.xcframework` from built archive in `dist/`
   - Drag `Python.xcframework` into Xcode project
   - Ensure it's set to "Embed & Sign"

3. **Add Your Code**
   - Replace ContentView.swift with the provided template
   - Create `app/` folder in Xcode (Resources group)
   - Add `main.py` to the `app/` folder
   - Add both to your app's target

4. **Configure Bridging**
   - Add Python.xcframework to "Frameworks, Libraries, and Embedded Content"
   - Set to "Embed & Sign"
   - **For Swift projects**: Use `import Python` (included in template)
     - This import gives access to Python C API functions (Py_Initialize, PyRun_SimpleString, etc.)
     - No bridging header needed for pure Swift projects
   - **For Objective-C or mixed projects**: 
     - Create a bridging header if needed
     - Add `#include <Python/Python.h>` to the bridging header
   - The Python.xcframework must be properly embedded for runtime access

5. **Build and Run**
   - Select a simulator or device
   - Build and run your app
   - Python code will execute on launch

## Customization

### Modify Python Code

Edit `app/main.py` to add your Python functionality:

```python
def my_function():
    # Your code here
    return "Hello from Python!"
```

### Call from Swift

In `ContentView.swift`, you can run Python code:

```swift
let code = """
import main
result = main.my_function()
print(result)
"""
PyRun_SimpleString(code)
```

### Add Python Packages

To use additional Python packages:
1. Build them for {platform} (see Mobile Forge)
2. Add .so files to your app bundle
3. Import them in Python code

## Troubleshooting

**Python not found:**
- Verify Python.xcframework is in "Frameworks" folder
- Check it's set to "Embed & Sign"
- Verify bundle contains python/ folder

**Import errors:**
- Check PYTHONPATH is set correctly
- Ensure app/ folder is in bundle
- Verify .py files are in app target

**Runtime crashes:**
- Check Xcode console for Python errors
- Verify Py_Initialize() succeeds
- Test Python code independently first

## Resources

- [Python Apple Support Docs](../USAGE.md)
- [CPython iOS Guide](https://docs.python.org/3/using/ios.html)
- [Briefcase Documentation](https://briefcase.readthedocs.io/)

## Next Steps

1. Test the basic template
2. Add your Python business logic
3. Create Swift UI for user interaction
4. Build and test on device
5. Distribute via TestFlight or App Store

Happy coding! 🐍🍎
'''

def generate_template(platform, app_name, output_dir):
    """Generate app template files."""
    platform_lower = platform.lower()
    if platform_lower not in TEMPLATES:
        print(f"Error: Unknown platform '{platform}'")
        print(f"Available: {', '.join(TEMPLATES.keys())}")
        return False
    
    template = TEMPLATES[platform_lower]
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Create app subdirectory for Python code
    app_dir = output_path / 'app'
    app_dir.mkdir(exist_ok=True)
    
    # Generate date
    date = datetime.now().strftime("%Y-%m-%d")
    
    print(f"\n📱 Generating {template['name']} template...")
    print(f"📁 Output directory: {output_path.absolute()}\n")
    
    # Generate Swift file
    swift_file = output_path / 'ContentView.swift'
    swift_content = SWIFT_TEMPLATE.format(
        app_name=app_name,
        date=date,
        platform=platform
    )
    swift_file.write_text(swift_content)
    print(f"✓ Created {swift_file.name}")
    
    # Generate Python file
    python_file = app_dir / 'main.py'
    python_content = PYTHON_TEMPLATE.format(
        app_name=app_name,
        date=date,
        platform=platform
    )
    python_file.write_text(python_content)
    print(f"✓ Created app/{python_file.name}")
    
    # Generate README
    readme_file = output_path / 'README.md'
    readme_content = README_TEMPLATE.format(
        app_name=app_name,
        date=date,
        platform=platform,
        platform_lower=platform_lower
    )
    readme_file.write_text(readme_content)
    print(f"✓ Created {readme_file.name}")
    
    print(f"\n✅ Template generated successfully!")
    print(f"\n📖 Next steps:")
    print(f"   1. Read {output_path.absolute()}/README.md")
    print(f"   2. Create Xcode project for {platform}")
    print(f"   3. Add Python.xcframework")
    print(f"   4. Copy template files into project")
    print(f"   5. Build and run!")
    
    return True

def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Generate starter templates for Python-powered Apple apps',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s --platform iOS --name "MyPythonApp"
  %(prog)s -p macOS -n "PythonDesktop" -o ~/Documents/Templates
  %(prog)s --platform visionOS --name "PythonVision"

Supported platforms: iOS, macOS, tvOS, watchOS, visionOS
        '''
    )
    
    parser.add_argument(
        '--platform', '-p',
        required=True,
        help='Target Apple platform'
    )
    
    parser.add_argument(
        '--name', '-n',
        default='MyPythonApp',
        help='App name (default: MyPythonApp)'
    )
    
    parser.add_argument(
        '--output', '-o',
        default='./template',
        help='Output directory (default: ./template)'
    )
    
    args = parser.parse_args()
    
    success = generate_template(args.platform, args.name, args.output)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
