#!/usr/bin/env python3
"""
Welcome to s200077761's Python Apple Support Project!

This script provides an overview of the project and helps you get started
building Python frameworks for Apple platforms.
"""

import os
import sys
import subprocess
from pathlib import Path

# ANSI color codes for pretty output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    """Print a colored header."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(60)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}\n")

def print_success(text):
    """Print a success message."""
    print(f"{Colors.OKGREEN}✓ {text}{Colors.ENDC}")

def print_info(text):
    """Print an info message."""
    print(f"{Colors.OKCYAN}ℹ {text}{Colors.ENDC}")

def print_warning(text):
    """Print a warning message."""
    print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")

def print_error(text):
    """Print an error message."""
    print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")

def check_requirements():
    """Check if the system meets the requirements."""
    print_header("Checking System Requirements")
    
    # Check macOS
    if sys.platform != 'darwin':
        print_error("This project requires macOS to build Apple platform frameworks")
        return False
    print_success("Running on macOS")
    
    # Check Xcode
    try:
        result = subprocess.run(['xcodebuild', '-version'], 
                              capture_output=True, text=True, check=True)
        xcode_version = result.stdout.split('\n')[0]
        print_success(f"Xcode found: {xcode_version}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_error("Xcode not found or not properly installed")
        print_info("Install Xcode from the App Store or run: xcode-select --install")
        return False
    
    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    if sys.version_info.major == 3 and sys.version_info.minor >= 8:
        print_success(f"Python version: {python_version}")
    else:
        print_warning(f"Python {python_version} detected. Python 3.8+ recommended")
    
    # Check disk space
    stat = os.statvfs('.')
    free_gb = (stat.f_bavail * stat.f_frsize) / (1024**3)
    if free_gb > 10:
        print_success(f"Available disk space: {free_gb:.1f} GB")
    else:
        print_warning(f"Low disk space: {free_gb:.1f} GB (10+ GB recommended)")
    
    return True

def show_project_info():
    """Display project information."""
    print_header("Project Information")
    
    project_dir = Path(__file__).parent.parent
    
    print(f"{Colors.BOLD}Project Directory:{Colors.ENDC} {project_dir}")
    
    # Check if Makefile exists
    makefile = project_dir / "Makefile"
    if makefile.exists():
        print_success("Makefile found")
        
        # Read Python version from Makefile
        with open(makefile, 'r') as f:
            for line in f:
                if line.startswith('PYTHON_VERSION='):
                    version = line.split('=')[1].strip()
                    print_info(f"Configured Python version: {version}")
                    break
    
    # Check for existing builds
    dist_dir = project_dir / "dist"
    if dist_dir.exists():
        build_files = list(dist_dir.glob("*.tar.gz"))
        if build_files:
            print_success(f"Found {len(build_files)} existing build(s) in dist/")
            for build_file in build_files[:3]:  # Show first 3
                print(f"  - {build_file.name}")
        else:
            print_info("No builds found in dist/ directory")
    else:
        print_info("dist/ directory not created yet (no builds)")

def show_quick_commands():
    """Show quick start commands."""
    print_header("Quick Start Commands")
    
    commands = [
        ("Build for all platforms", "make all"),
        ("Build for macOS only", "make macOS"),
        ("Build for iOS only", "make iOS"),
        ("Build for tvOS only", "make tvOS"),
        ("Build for watchOS only", "make watchOS"),
        ("Build for visionOS only", "make visionOS"),
        ("Clean build artifacts", "make clean"),
        ("Complete clean (includes downloads)", "make distclean"),
    ]
    
    for desc, cmd in commands:
        print(f"{Colors.OKBLUE}{cmd:40}{Colors.ENDC} # {desc}")

def show_platforms():
    """Show supported platforms."""
    print_header("Supported Apple Platforms")
    
    platforms = [
        ("macOS", "11.0+", "Big Sur and later", "x86_64, arm64"),
        ("iOS", "13.0+", "iPhone, iPad, iPod Touch", "arm64, simulator"),
        ("tvOS", "12.0+", "Apple TV", "arm64, simulator"),
        ("watchOS", "4.0+", "Apple Watch", "arm64_32, simulator"),
        ("visionOS", "2.0+", "Apple Vision Pro", "arm64, simulator"),
    ]
    
    for name, min_version, desc, archs in platforms:
        print(f"{Colors.BOLD}{name:12}{Colors.ENDC} {min_version:8} - {desc}")
        print(f"{'':12} Architectures: {archs}")
        print()

def show_next_steps():
    """Show suggested next steps."""
    print_header("Suggested Next Steps")
    
    steps = [
        "1. Review the PERSONALIZED_README.md for detailed information",
        "2. Start with a single platform: make iOS",
        "3. Check the dist/ folder for your built frameworks",
        "4. Read USAGE.md to learn how to use the frameworks in Xcode",
        "5. Try the test suite with the iOS/visionOS testbed projects",
    ]
    
    for step in steps:
        print(f"{Colors.OKCYAN}{step}{Colors.ENDC}")

def main():
    """Main function."""
    print(f"""
{Colors.HEADER}{Colors.BOLD}
    🍎 Python Apple Support - Personal Edition
    ==========================================
    
    Owner: s200077761
    Purpose: Build Python frameworks for all Apple platforms
{Colors.ENDC}
    """)
    
    if not check_requirements():
        print_error("\nSystem requirements not met. Please resolve the issues above.")
        sys.exit(1)
    
    show_project_info()
    show_platforms()
    show_quick_commands()
    show_next_steps()
    
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}Ready to build Python for Apple platforms!{Colors.ENDC}\n")
    print(f"{Colors.OKCYAN}For more information, see PERSONALIZED_README.md{Colors.ENDC}\n")

if __name__ == "__main__":
    main()
