#!/usr/bin/env python3
"""
Quick Build Demo Script for Python Apple Support

This script helps you build Python frameworks for specific Apple platforms
with helpful progress indicators and error handling.
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_step(step_num, total_steps, message):
    """Print a build step."""
    print(f"\n{Colors.OKCYAN}{Colors.BOLD}[Step {step_num}/{total_steps}]{Colors.ENDC} {message}")

def print_success(message):
    """Print a success message."""
    print(f"{Colors.OKGREEN}✓ {message}{Colors.ENDC}")

def print_error(message):
    """Print an error message."""
    print(f"{Colors.FAIL}✗ {message}{Colors.ENDC}")

def print_info(message):
    """Print an info message."""
    print(f"{Colors.OKCYAN}ℹ {message}{Colors.ENDC}")

def run_command(cmd, description, show_output=False):
    """Run a shell command and report results."""
    print_info(f"{description}...")
    
    try:
        if show_output:
            result = subprocess.run(cmd, shell=True, check=True)
        else:
            result = subprocess.run(cmd, shell=True, check=True, 
                                  capture_output=True, text=True)
        print_success(f"{description} completed")
        return True, result
    except subprocess.CalledProcessError as e:
        print_error(f"{description} failed")
        if hasattr(e, 'stderr') and e.stderr:
            print(f"{Colors.FAIL}Error output:{Colors.ENDC}")
            print(e.stderr[:500])  # Show first 500 chars of error
        return False, e

def build_platform(platform, clean_first=False, show_output=False):
    """Build Python for a specific platform."""
    platform = platform.lower()
    valid_platforms = ['macos', 'ios', 'tvos', 'watchos', 'visionos']
    
    if platform not in valid_platforms:
        print_error(f"Invalid platform: {platform}")
        print_info(f"Valid platforms: {', '.join(valid_platforms)}")
        return False
    
    # Capitalize platform name for make target
    platform_target = platform[0].upper() + platform[1:]
    if platform == 'macos':
        platform_target = 'macOS'
    elif platform == 'tvos':
        platform_target = 'tvOS'
    elif platform == 'watchos':
        platform_target = 'watchOS'
    elif platform == 'visionos':
        platform_target = 'visionOS'
    
    print(f"""
{Colors.HEADER}{Colors.BOLD}
╔════════════════════════════════════════════════════════════╗
║  Building Python for {platform_target:^42} ║
╚════════════════════════════════════════════════════════════╝
{Colors.ENDC}
""")
    
    project_dir = Path(__file__).parent.parent
    
    total_steps = 3 if clean_first else 2
    current_step = 1
    
    # Optional clean step
    if clean_first:
        print_step(current_step, total_steps, "Cleaning previous builds")
        success, _ = run_command(
            f"cd {project_dir} && make clean-{platform_target}",
            f"Cleaning {platform_target}",
            show_output=show_output
        )
        if not success:
            print_error("Clean failed, but continuing anyway...")
        current_step += 1
        time.sleep(1)
    
    # Build step
    print_step(current_step, total_steps, f"Building Python for {platform_target}")
    print_info("This may take 30-60 minutes depending on your system...")
    
    start_time = time.time()
    success, result = run_command(
        f"cd {project_dir} && make {platform_target}",
        f"Building {platform_target}",
        show_output=show_output
    )
    
    if not success:
        print_error(f"\nBuild failed for {platform_target}")
        return False
    
    elapsed_time = time.time() - start_time
    print_success(f"Build completed in {elapsed_time/60:.1f} minutes")
    current_step += 1
    
    # Check output
    print_step(current_step, total_steps, "Verifying build output")
    
    dist_dir = project_dir / "dist"
    if dist_dir.exists():
        build_files = list(dist_dir.glob(f"*{platform}*.tar.gz"))
        if build_files:
            print_success(f"Found {len(build_files)} build artifact(s):")
            for build_file in build_files:
                size_mb = build_file.stat().st_size / (1024 * 1024)
                print(f"  {Colors.OKGREEN}→{Colors.ENDC} {build_file.name} ({size_mb:.1f} MB)")
        else:
            print_error("No build artifacts found in dist/")
            return False
    else:
        print_error("dist/ directory not found")
        return False
    
    print(f"""
{Colors.OKGREEN}{Colors.BOLD}
╔════════════════════════════════════════════════════════════╗
║  Build Successful! 🎉                                      ║
╚════════════════════════════════════════════════════════════╝
{Colors.ENDC}
""")
    
    print_info(f"Your Python {platform_target} framework is ready to use!")
    print_info(f"Find it in: {dist_dir}")
    print_info(f"See USAGE.md for instructions on using it in Xcode projects")
    
    return True

def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Build Python frameworks for Apple platforms',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --platform iOS              Build for iOS
  %(prog)s --platform macOS --clean    Clean and build for macOS
  %(prog)s --platform tvOS --verbose   Build for tvOS with verbose output
  
Supported platforms: macOS, iOS, tvOS, watchOS, visionOS
        """
    )
    
    parser.add_argument(
        '--platform', '-p',
        required=True,
        help='Apple platform to build for (macOS, iOS, tvOS, watchOS, visionOS)'
    )
    
    parser.add_argument(
        '--clean', '-c',
        action='store_true',
        help='Clean before building'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show build output (verbose mode)'
    )
    
    args = parser.parse_args()
    
    # Check if running on macOS
    if sys.platform != 'darwin':
        print_error("This script must be run on macOS")
        sys.exit(1)
    
    # Run the build
    success = build_platform(args.platform, args.clean, args.verbose)
    
    if success:
        sys.exit(0)
    else:
        print_error("\nBuild failed. Check the output above for details.")
        print_info("Try running with --verbose flag for more information")
        sys.exit(1)

if __name__ == "__main__":
    main()
