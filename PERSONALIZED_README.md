# 🍎 My Personal Python Apple Support Project

Welcome to **s200077761's customized Python Apple Support framework**! 

This is a personalized fork of the Python Apple Support project, specially configured to build and run Python applications on all Apple platforms including macOS, iOS, tvOS, watchOS, and visionOS.

## 🌟 What Makes This Special

This personalized version includes:

- **Quick Start Scripts**: Easy-to-use scripts for building Python frameworks
- **Demo Applications**: Sample apps showing Python running on Apple devices
- **Custom Configuration**: Pre-configured build settings optimized for development
- **Enhanced Documentation**: Step-by-step guides for every Apple platform
- **Personal Branding**: This is YOUR Python on Apple toolkit!

## 🚀 Quick Start

### Prerequisites
- macOS with Xcode installed (Xcode 14 or later recommended)
- Command Line Tools: `xcode-select --install`
- At least 10GB of free disk space

### Build Everything
```bash
# Build Python for all Apple platforms
make all

# Or build for specific platforms:
make macOS    # Build for macOS only
make iOS      # Build for iOS only
make tvOS     # Build for tvOS only
make watchOS  # Build for watchOS only
make visionOS # Build for visionOS only
```

### Try the Demo
```bash
# Run the welcome script to see what this project can do
python3 scripts/welcome.py

# Build a quick demo for iOS
python3 scripts/build_demo.py --platform iOS
```

## 📱 Supported Platforms

This project builds Python frameworks for:

- **macOS 11+** (Big Sur and later) - Intel & Apple Silicon
- **iOS 13.0+** - iPhone, iPad, iPod Touch
- **tvOS 12.0+** - Apple TV
- **watchOS 4.0+** - Apple Watch
- **visionOS 2.0+** - Apple Vision Pro

## 🎯 What You Get

After building, you'll find in the `dist/` folder:
- Python.xcframework - Ready to embed in Xcode projects
- Complete Python standard library
- Support for arm64 and x86_64 architectures
- Pre-configured build scripts

## 🛠️ Customization Guide

### Personal Build Number
Edit the `BUILD_NUMBER` in the Makefile:
```makefile
BUILD_NUMBER=my-custom-build-1
```

### Python Version
The project currently builds Python 3.14.0. To change versions:
1. Edit `PYTHON_VERSION` in the Makefile
2. Run `make distclean` to clear old builds
3. Run `make` to build the new version

### Adding Custom Patches
Place your custom patches in the `patch/Python/` directory and they'll be automatically applied during the build process.

## 📚 Learn More

- [Original Usage Guide](USAGE.md) - Detailed instructions for using the framework
- [Contributing](CONTRIBUTING.md) - How to contribute improvements
- [BeeWare Python Apple Support](https://github.com/beeware/Python-Apple-support) - Upstream project

## 🎨 Personal Projects Built With This

Use this section to showcase your own apps built with this framework!

- [ ] My First iOS Python App
- [ ] My Python-powered Apple Watch App
- [ ] My visionOS Python Experience

## 💡 Tips & Tricks

1. **Faster Builds**: Use `make iOS` for just iOS instead of building all platforms
2. **Clean Slate**: Run `make distclean` to start fresh
3. **Testing**: Use the testbed projects in iOS/visionOS distributions
4. **Size Matters**: The full build can take 1-2 hours and several GB

## 🤝 Getting Help

- Check the [Usage Guide](USAGE.md) for detailed instructions
- Review the [CPython iOS documentation](https://docs.python.org/3/using/ios.html)
- Look at example Briefcase projects for working implementations

## 📜 License

This project inherits the Python Software Foundation License from CPython.
See [LICENSE](LICENSE) for details.

---

**Built with ❤️ for Apple platforms by s200077761**
