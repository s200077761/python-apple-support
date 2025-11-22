# 🍎 Python Apple Support - Personal Edition

> **Personal fork by s200077761** - Enhanced with custom scripts and guides

This is a meta-package for building a version of Python that can be
embedded into a macOS, iOS, tvOS, watchOS, or visionOS project.

## 🎯 Personal Enhancements

This fork includes several improvements to make it easier to use:

- **[📋 Project Overview](PROJECT_OVERVIEW.md)** - Complete guide to this fork
- **[📖 Personalized README](PERSONALIZED_README.md)** - Customized overview and branding
- **[🚀 Quick Start Guide](QUICKSTART.md)** - Get building in minutes
- **[📱 Demo Applications](DEMOS.md)** - Example apps and code snippets
- **[🛠️ Helper Scripts](scripts/)** - Automated build and check scripts

### Quick Commands

```bash
# Check if your system is ready
python3 scripts/check_system.py

# See project overview and capabilities  
python3 scripts/welcome.py

# Build for a specific platform with guidance
python3 scripts/build_demo.py --platform iOS
```

**This branch builds a packaged version of Python 3.14**. Other Python
versions are available by cloning other branches of the main repository:

- [Python
  3.10](https://github.com/beeware/Python-Apple-support/tree/3.10)
- [Python
  3.11](https://github.com/beeware/Python-Apple-support/tree/3.11)
- [Python
  3.12](https://github.com/beeware/Python-Apple-support/tree/3.12)
- [Python
  3.13](https://github.com/beeware/Python-Apple-support/tree/3.13)

It works by downloading, patching, and building a fat binary of Python
and selected pre-requisites, and packaging them as frameworks that can
be incorporated into an Xcode project. The binary modules in the Python
standard library are distributed as binaries that can be dynamically
loaded at runtime.

The macOS package is a re-bundling of the official macOS binary,
modified so that it is relocatable, with the IDLE, Tkinter and turtle
packages removed, and the App Store compliance patch applied.

The iOS, tvOS, watchOS, and visionOS packages compiled by this project
use the official [PEP 730](https://peps.python.org/pep-0730/) code that
is part of Python 3.13 to provide iOS support; the relevant patches have
been backported to 3.10-3.12. Additional patches have been applied to add
tvOS, watchOS, and visionOS support.

The binaries support x86_64 and arm64 for macOS; arm64 for iOS and
appleTV devices; arm64_32 for watchOS devices; and arm64 for visionOS
devices. It also supports device simulators on both x86_64 and M1
hardware, except for visionOS, for which x86_64 simulators are
officially unsupported. This should enable the code to run on:

- macOS 11 (Big Sur) or later, on:
  - MacBook (including MacBooks using Apple Silicon)
  - iMac (including iMacs using Apple Silicon)
  - Mac Mini (including Apple Silicon Mac minis)
  - Mac Studio (all models)
  - Mac Pro (all models)

- iOS 13.0 or later, on:
  - iPhone (6s or later)
  - iPad (5th gen or later)
  - iPad Air (all models)
  - iPad Mini (2 or later)
  - iPad Pro (all models)
  - iPod Touch (7th gen or later)

- tvOS 12.0 or later, on:
  - Apple TV (4th gen or later)

- watchOS 4.0 or later, on:
  - Apple Watch (4th gen or later)

- visionOS 2.0 or later, on:
  - Apple Vision Pro

## 🚀 Quickstart

### The Easy Way (Recommended)

1. **Check your system**: `python3 scripts/check_system.py`
2. **See what's possible**: `python3 scripts/welcome.py`
3. **Build your first framework**: `python3 scripts/build_demo.py --platform iOS`

### The Standard Way

The easist way to use these packages is by creating a project with
[Briefcase](https://github.com/beeware/briefcase). Briefcase will
download pre-compiled versions of these support packages, and add them
to an Xcode project (or pre-build stub application, in the case of
macOS).

Pre-built versions of the frameworks can be downloaded from the [Github
releases page](https://github.com/beeware/Python-Apple-support/releases)
and added to your project.

### Building From Source

To build the frameworks on your own, download/clone this
repository, and then in the root directory, run:

- `make` (or `make all`) to build everything.
- `make macOS` to build everything for macOS.
- `make iOS` to build everything for iOS.
- `make tvOS` to build everything for tvOS.
- `make watchOS` to build everything for watchOS.
- `make visionOS` to build everything for visionOS.

**See [QUICKSTART.md](QUICKSTART.md) for detailed step-by-step instructions!**

This should:

1.  Download the original source packages
2.  Patch them as required for compatibility with the selected OS
3.  Build the packages as Xcode-compatible XCFrameworks.

The resulting support packages will be packaged as `.tar.gz` files in
the `dist` folder.

Each support package contains:

- `VERSIONS`, a text file describing the specific versions of code used
  to build the support package;
- `Python.xcframework`, a multi-architecture build of the Python runtime
  library.

On iOS/tvOS/watchOS/visionOS, the `Python.xcframework` contains a slice
for each supported ABI (device and simulator). The folder containing the
slice can also be used as a `PYTHONHOME`, as it contains a `bin`,
`include` and `lib` directory.

The `bin` folder does not contain Python executables (as they can't be
invoked). However, it *does* contain shell aliases for the compilers
that are needed to build packages. This is required because Xcode uses
the `xcrun` alias to dynamically generate the name of binaries, but a
lot of C tooling expects that `CC` will not contain spaces.

Each slice of an iOS/tvOS/watchOS/visionOS XCframework also contains a
`platform-config` folder with a subfolder for each supported
architecture in that slice. These subfolders can be used to make a macOS
Python environment behave as if it were on an iOS/tvOS/watchOS/visionOS
device. This works in one of two ways:

1.  **A sitecustomize.py script**. If the `platform-config` subfolder is
    on your `PYTHONPATH` when a Python interpreter is started, a site
    customization will be applied that patches methods in `sys`,
    `sysconfig` and `platform` that are used to identify the system.
2.  **A make_cross_venv.py script**. If you call `make_cross_venv.py`,
    providing the location of a virtual environment, the script will add
    some files to the `site-packages` folder of that environment that
    will automatically apply the same set of patches as the
    `sitecustomize.py` script whenever the environment is activated,
    without any need to modify `PYTHONPATH`. If you use `build` to
    create an isolated PEP 517 environment to build a wheel, these
    patches will also be applied to the isolated build environment that
    is created.

iOS and visionOS distributions also contain a copy of the iOS or
visionOS `testbed` project - an Xcode project that can be used to run
test suites of Python code. See the [CPython documentation on testing
packages](https://docs.python.org/3/using/ios.html#testing-a-python-package)
for details on how to use this testbed.

For a detailed instructions on using the support package in your own
project, see the [usage guide](./USAGE.md)

## Building binary wheels

This project packages the Python standard library, but does not address
building binary wheels. Binary wheels for macOS can be obtained from
PyPI. [Mobile Forge](https://github.com/beeware/mobile-forge) is a
project that provides the tooling to build build binary wheels for iOS
(and potentially for tvOS, watchOS, and visionOS, although that hasn't
been tested).

## Historical support

The following versions were supported in the past, but are no longer
maintained:

- [Python 2.7](https://github.com/beeware/Python-Apple-support/tree/2.7)
  (EOL January 2020)
- [Python 3.4](https://github.com/beeware/Python-Apple-support/tree/3.4)
  (EOL March 2019)
- [Python 3.5](https://github.com/beeware/Python-Apple-support/tree/3.5)
  (EOL February 2021)
- [Python 3.6](https://github.com/beeware/Python-Apple-support/tree/3.6)
  (EOL December 2021)
- [Python 3.7](https://github.com/beeware/Python-Apple-support/tree/3.7)
  (EOL September 2022)
- [Python 3.8](https://github.com/beeware/Python-Apple-support/tree/3.8)
  (EOL October 2024)
- [Python 3.9](https://github.com/beeware/Python-Apple-support/tree/3.9)
  (EOL October 2025)

---

## 🎨 Personal Fork Features

This fork (s200077761/python-apple-support) includes enhanced tooling:

### Helper Scripts

Located in `scripts/`:

- **check_system.py** - Verify your Mac is ready to build
- **welcome.py** - Interactive project overview and capabilities
- **build_demo.py** - Guided build process with progress tracking

### Enhanced Documentation

- **PERSONALIZED_README.md** - Custom overview with personal branding
- **QUICKSTART.md** - Step-by-step guide for beginners
- **DEMOS.md** - Example applications and code samples

### Configuration

- **personal.config** - Customizable build settings and preferences

### Usage

```bash
# Start here - check if you're ready to build
python3 scripts/check_system.py

# Learn about the project
python3 scripts/welcome.py

# Build with guidance
python3 scripts/build_demo.py --platform iOS --verbose
```

All original functionality is preserved. These additions make the project more accessible and easier to customize!

---

**Upstream Project**: [beeware/Python-Apple-support](https://github.com/beeware/Python-Apple-support)

**Personal Fork**: Built with ❤️ for Apple platforms by s200077761
