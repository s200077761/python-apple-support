# 📱 Demo Applications

This directory contains example applications showcasing Python running on Apple platforms.

## What's Included

While the full builds require significant time, here are demo concepts you can implement once you have the frameworks built:

## 1. Hello World iOS App

A simple iOS app that runs Python code.

**What it does:**
- Initializes Python runtime
- Runs a simple Python script
- Displays output in UILabel

**Python code it runs:**
```python
import sys
import platform

def get_device_info():
    return {
        'platform': sys.platform,
        'version': sys.version,
        'architecture': platform.machine(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    }

if __name__ == '__main__':
    info = get_device_info()
    print("Hello from Python on iOS!")
    print(f"Platform: {info['platform']}")
    print(f"Architecture: {info['architecture']}")
    print(f"Python: {info['python_version']}")
```

## 2. Calculator Widget (watchOS)

A Python-powered calculator for Apple Watch.

**Features:**
- Basic arithmetic operations in Python
- WatchKit UI
- Real-time calculations

## 3. Data Visualizer (visionOS)

Visualize data in 3D space using Python.

**Features:**
- NumPy for data processing
- RealityKit integration
- Immersive Python data science

## 4. Home Automation (tvOS)

Control smart home devices from Apple TV using Python.

**Features:**
- Python automation scripts
- tvOS interface
- Network communications

## 5. System Monitor (macOS)

A menu bar app showing system stats using Python.

**Features:**
- Real-time system monitoring
- Python data processing
- macOS native UI

## How to Use These Demos

### Step 1: Build the Framework

First, build Python for your target platform:

```bash
python3 scripts/build_demo.py --platform iOS
```

### Step 2: Create Xcode Project

1. Open Xcode
2. Create new App project
3. Choose your target platform (iOS, macOS, etc.)

### Step 3: Add Python Framework

1. Extract your built framework from `dist/`
2. Drag `Python.xcframework` into your Xcode project
3. Ensure it's added to "Frameworks, Libraries, and Embedded Content"
4. Set to "Embed & Sign"

### Step 4: Add Python Code

Create an `app` folder in your project with your Python scripts:

```
MyApp/
├── MyApp/
│   ├── main.swift
│   └── ContentView.swift
└── Resources/
    └── app/
        └── main.py  <- Your Python code here
```

### Step 5: Initialize Python

In your app delegate or main entry point:

**Swift:**
```swift
import Python

func initializePython() {
    guard let pythonHome = Bundle.main.path(forResource: "python", ofType: nil) else {
        print("Python framework not found")
        return
    }
    
    let appPath = Bundle.main.path(forResource: "app", ofType: nil)
    
    setenv("PYTHONHOME", pythonHome, 1)
    setenv("PYTHONPATH", appPath, 1)
    
    Py_Initialize()
    
    // Python is now ready!
}
```

**Objective-C:**
```objc
#include <Python/Python.h>

- (void)initializePython {
    NSString *resourcePath = [[NSBundle mainBundle] resourcePath];
    NSString *pythonHome = [NSString stringWithFormat:@"%@/python", resourcePath];
    NSString *appPath = [NSString stringWithFormat:@"%@/app", resourcePath];
    
    setenv("PYTHONHOME", [pythonHome UTF8String], 1);
    setenv("PYTHONPATH", [appPath UTF8String], 1);
    
    Py_Initialize();
    
    // Python is now ready!
}
```

### Step 6: Run Python Code

**From Swift:**
```swift
import PythonKit  // Optional, for easier Python interaction

// Using C API
let code = """
print('Hello from Python!')
import sys
print(f'Running on {sys.platform}')
"""
PyRun_SimpleString(code)

// Using PythonKit (if installed)
let sys = Python.import("sys")
print("Python version: \(sys.version)")
```

## Example: iOS App with Python

Here's a complete minimal example for iOS:

**ContentView.swift:**
```swift
import SwiftUI
import Python

struct ContentView: View {
    @State private var output: String = "Initializing Python..."
    
    var body: some View {
        VStack {
            Text("Python on iOS")
                .font(.title)
            
            Text(output)
                .padding()
            
            Button("Run Python") {
                runPython()
            }
        }
        .onAppear {
            initializePython()
        }
    }
    
    func initializePython() {
        guard let pythonHome = Bundle.main.path(forResource: "python", ofType: nil) else {
            output = "Python not found"
            return
        }
        
        setenv("PYTHONHOME", pythonHome, 1)
        Py_Initialize()
        output = "Python ready!"
    }
    
    func runPython() {
        let code = """
        import sys
        result = f'Python {sys.version_info.major}.{sys.version_info.minor} on {sys.platform}'
        print(result)
        """
        
        PyRun_SimpleString(code)
        output = "Python executed! Check console."
    }
}
```

## Resources

- **iOS Testbed**: After building iOS, find testbed project in dist archive
- **visionOS Testbed**: After building visionOS, find testbed project in dist archive
- **CPython iOS Docs**: https://docs.python.org/3/using/ios.html
- **Briefcase Docs**: https://briefcase.readthedocs.io/
- **PythonKit**: https://github.com/pvieito/PythonKit

## Tips for Demo Development

1. **Start Simple**: Begin with print statements and basic Python code
2. **Use Testbeds**: The iOS/visionOS testbeds are great starting points
3. **Check Console**: Use Xcode's console to see Python output
4. **Debug Carefully**: Python runtime errors can be tricky on mobile
5. **Test on Device**: Simulator and device may behave differently

## Next Steps

1. Build your chosen platform framework
2. Extract and explore the testbed projects (iOS/visionOS)
3. Modify the testbed to run your own Python code
4. Create your own Xcode project with Python
5. Share your creations!

Happy Python app development on Apple platforms! 🐍🍎
