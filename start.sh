#!/bin/bash
# Quick Start Script for Python Apple Support
# This script guides you through the initial setup

echo "🍎 Python Apple Support - Quick Start"
echo "======================================"
echo ""
echo "This script will help you get started with building Python for Apple platforms."
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "   Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Run system check
echo "Step 1: Checking system requirements..."
echo "========================================"
python3 scripts/check_system.py
CHECK_RESULT=$?

echo ""
echo ""

if [ $CHECK_RESULT -ne 0 ]; then
    echo "⚠️  System requirements not fully met."
    echo "   Please resolve the issues above before building."
    echo ""
    echo "Common fixes:"
    echo "  • Install Xcode from the Mac App Store"
    echo "  • Run: xcode-select --install"
    echo "  • Upgrade Python: brew install python@3.11"
    echo ""
    exit 1
fi

echo "Step 2: Learning about the project..."
echo "======================================"
echo ""
echo "Running welcome script..."
python3 scripts/welcome.py

echo ""
echo ""
echo "Step 3: What would you like to do?"
echo "===================================="
echo ""
echo "Choose an option:"
echo "  1) Build Python for iOS"
echo "  2) Build Python for macOS"
echo "  3) Build Python for all platforms"
echo "  4) Generate app template"
echo "  5) Read documentation"
echo "  6) Exit"
echo ""
read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo ""
        echo "Building Python for iOS..."
        python3 scripts/build_demo.py --platform iOS
        ;;
    2)
        echo ""
        echo "Building Python for macOS..."
        python3 scripts/build_demo.py --platform macOS
        ;;
    3)
        echo ""
        echo "Building Python for all platforms (this will take 1-2 hours)..."
        read -p "Are you sure? (y/n): " confirm
        if [ "$confirm" = "y" ]; then
            make all
        else
            echo "Build cancelled."
        fi
        ;;
    4)
        echo ""
        read -p "Enter app name: " app_name
        read -p "Enter platform (iOS/macOS/tvOS/watchOS/visionOS): " platform
        python3 scripts/generate_template.py --platform "$platform" --name "$app_name"
        ;;
    5)
        echo ""
        echo "Available documentation:"
        echo "  • README.md - Main overview"
        echo "  • QUICKSTART.md - Step-by-step guide"
        echo "  • PROJECT_OVERVIEW.md - Complete reference"
        echo "  • DEMOS.md - Example applications"
        echo "  • USAGE.md - Using frameworks in Xcode"
        echo ""
        echo "Open any of these files to learn more!"
        ;;
    6)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "✅ Done!"
echo ""
echo "Next steps:"
echo "  • Check the dist/ folder for built frameworks"
echo "  • Read USAGE.md for integration instructions"
echo "  • Generate templates with: python3 scripts/generate_template.py"
echo ""
