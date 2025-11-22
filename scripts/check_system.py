#!/usr/bin/env python3
"""
System Check Script for Python Apple Support

This script verifies that your system is ready to build Python frameworks
for Apple platforms.
"""

import subprocess
import sys
import os
from pathlib import Path

class Colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def check_item(name, test_func, fix_hint=None):
    """Check a requirement and print status."""
    print(f"Checking {name}...", end=" ")
    try:
        result = test_func()
        if result:
            print(f"{Colors.OKGREEN}✓ PASS{Colors.ENDC}")
            return True
        else:
            print(f"{Colors.FAIL}✗ FAIL{Colors.ENDC}")
            if fix_hint:
                print(f"  {Colors.WARNING}→ {fix_hint}{Colors.ENDC}")
            return False
    except Exception as e:
        print(f"{Colors.FAIL}✗ FAIL{Colors.ENDC}")
        print(f"  {Colors.WARNING}→ Error: {str(e)}{Colors.ENDC}")
        if fix_hint:
            print(f"  {Colors.WARNING}→ {fix_hint}{Colors.ENDC}")
        return False

def check_macos():
    """Check if running on macOS."""
    return sys.platform == 'darwin'

def check_xcode():
    """Check if Xcode is installed."""
    try:
        subprocess.run(['xcodebuild', '-version'], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_commandline_tools():
    """Check if Xcode Command Line Tools are installed."""
    try:
        result = subprocess.run(['xcode-select', '-p'], 
                              capture_output=True, text=True, check=True)
        return len(result.stdout.strip()) > 0
    except subprocess.CalledProcessError:
        return False

def check_python_version():
    """Check if Python version is 3.8+."""
    return sys.version_info >= (3, 8)

def check_make():
    """Check if make is available."""
    try:
        subprocess.run(['make', '--version'], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_git():
    """Check if git is available."""
    try:
        subprocess.run(['git', '--version'], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_disk_space():
    """Check if there's at least 10GB free space."""
    stat = os.statvfs('.')
    free_gb = (stat.f_bavail * stat.f_frsize) / (1024**3)
    return free_gb >= 10

def get_disk_space():
    """Get free disk space in GB."""
    stat = os.statvfs('.')
    return (stat.f_bavail * stat.f_frsize) / (1024**3)

def main():
    """Main function."""
    print(f"\n{Colors.BOLD}=== Python Apple Support - System Check ==={Colors.ENDC}\n")
    
    checks = [
        ("macOS Operating System", check_macos, 
         "This project requires macOS to build Apple frameworks"),
        
        ("Xcode", check_xcode, 
         "Install Xcode from the Mac App Store"),
        
        ("Xcode Command Line Tools", check_commandline_tools, 
         "Run: xcode-select --install"),
        
        ("Python 3.8+", check_python_version, 
         f"Current version: {sys.version_info.major}.{sys.version_info.minor}. Python 3.8+ required. Upgrade via Homebrew: 'brew install python3' or download latest from python.org"),
        
        ("make", check_make, 
         "Install Xcode Command Line Tools"),
        
        ("git", check_git, 
         "Install Xcode Command Line Tools or Homebrew git"),
        
        ("Disk Space (10GB+)", check_disk_space, 
         f"Free space: {get_disk_space():.1f}GB. Free up disk space."),
    ]
    
    results = []
    for name, test_func, fix_hint in checks:
        results.append(check_item(name, test_func, fix_hint))
    
    print(f"\n{Colors.BOLD}=== Summary ==={Colors.ENDC}")
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"{Colors.OKGREEN}{Colors.BOLD}All checks passed! ✓{Colors.ENDC}")
        print(f"\nYour system is ready to build Python for Apple platforms!")
        print(f"Run: python3 scripts/welcome.py to get started")
        return 0
    else:
        print(f"{Colors.WARNING}{passed}/{total} checks passed{Colors.ENDC}")
        print(f"\nPlease fix the issues above before building.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
