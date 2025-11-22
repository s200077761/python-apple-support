# 🚀 Quick Start Guide

Welcome! This guide will get you building Python for Apple platforms in minutes.

## Step 1: Check Your System

First, verify your system is ready:

```bash
python3 scripts/check_system.py
```

This will check for:
- macOS operating system
- Xcode installation
- Command Line Tools
- Python 3.8+
- Required build tools
- Sufficient disk space

## Step 2: Run the Welcome Script

Get an overview of the project:

```bash
python3 scripts/welcome.py
```

This will show you:
- Project information
- Supported platforms
- Available commands
- Current configuration

## Step 3: Choose Your Platform

Decide which Apple platform you want to build for:

- **macOS** - Desktop Macs (easiest to start with)
- **iOS** - iPhones and iPads
- **tvOS** - Apple TV
- **watchOS** - Apple Watch
- **visionOS** - Apple Vision Pro

## Step 4: Build!

### Option A: Quick Build (Recommended for First Time)

Use the helper script for a guided build:

```bash
python3 scripts/build_demo.py --platform iOS
```

Replace `iOS` with your chosen platform (macOS, iOS, tvOS, watchOS, or visionOS).

### Option B: Direct Build

Use make directly for more control:

```bash
make iOS
```

Or build everything:

```bash
make all
```

## What Happens During Build?

The build process will:

1. **Download** - Fetch Python source and dependencies (~100MB)
2. **Patch** - Apply Apple platform patches
3. **Compile** - Build for multiple architectures (this takes time!)
4. **Package** - Create XCFramework bundles

**Expected Time:**
- Single platform: 30-60 minutes
- All platforms: 1-2 hours

**Expected Disk Usage:**
- Downloads: ~500MB
- Build artifacts: ~2-3GB per platform
- Final packages: ~50-100MB per platform

## Step 5: Find Your Build

After building, your frameworks will be in:

```
dist/
├── Python-3.14-iOS-support.custom.tar.gz
├── Python-3.14-macOS-support.custom.tar.gz
└── ... (other platforms)
```

Each archive contains:
- `Python.xcframework` - The Python runtime
- `VERSIONS` - Build information
- Platform-specific tools and configs

## Step 6: Use It!

### For Briefcase Projects

[Briefcase](https://briefcase.readthedocs.io/) will automatically download and use pre-built versions. To use your custom build:

1. Build your framework
2. Extract to Briefcase's support directory
3. Build your app with Briefcase

### For Xcode Projects

See the [USAGE.md](USAGE.md) file for detailed instructions on:
- Adding the framework to your Xcode project
- Initializing the Python runtime
- Running Python code from Objective-C or Swift

## Common Build Commands

```bash
# Clean everything and start fresh
make distclean

# Clean just build artifacts
make clean

# Build specific platform
make macOS
make iOS
make tvOS
make watchOS
make visionOS

# Get variables/configuration
make vars

# Clean specific platform
make clean-iOS
```

## Troubleshooting

### Build Fails

1. Check system requirements: `python3 scripts/check_system.py`
2. Clean and retry: `make distclean && make iOS`
3. Check disk space: `df -h .`
4. Verify Xcode: `xcodebuild -version`

### Out of Disk Space

The build process needs ~10GB free space. To free up space:

```bash
# Remove old builds
make distclean

# Remove just downloads
rm -rf downloads/
```

### Xcode Issues

```bash
# Reset Xcode command line tools
sudo xcode-select --reset

# Accept Xcode license
sudo xcodebuild -license accept
```

### Python Version Issues

Make sure you're using Python 3.8 or later:

```bash
python3 --version
```

## What's Next?

1. **Explore** - Look at the generated `dist/` files
2. **Learn** - Read [USAGE.md](USAGE.md) for integration guide
3. **Experiment** - Try the iOS/visionOS testbed projects
4. **Customize** - Edit `personal.config` for your preferences
5. **Build** - Create your own Python apps for Apple platforms!

## Getting Help

- Check [USAGE.md](USAGE.md) for detailed usage instructions
- Review [README.md](README.md) for project overview
- See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
- Visit [BeeWare Documentation](https://docs.beeware.org/) for app development

## Success! 🎉

You now have Python frameworks ready to use in your Apple platform projects!

**What you can do:**
- Embed Python in iOS apps
- Create Python-powered Apple Watch apps
- Build visionOS experiences with Python
- Run Python code on Apple TV
- Use Python in macOS applications

**Happy coding!** 🐍🍎
