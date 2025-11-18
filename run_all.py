#!/usr/bin/env python3
import subprocess
import sys
import time
import os
from threading import Thread

def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║   🌐 Multi-Threaded Web Server with Real-Time Dashboard       ║
    ║                                                                ║
    ║   Starting all components...                                  ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def run_server():
    print("\n[1/2] Starting Web Server on port 8080...")
    print("=" * 60)
    try:
        subprocess.run([sys.executable, '-m', 'server.server'], cwd=os.getcwd())
    except KeyboardInterrupt:
        print("\n[SERVER] Shutting down...")

def run_dashboard():
    print("\n[2/2] Starting Dashboard on port 5000...")
    print("=" * 60)
    time.sleep(2)
    try:
        subprocess.run([sys.executable, '-m', 'dashboard.dashboard'], cwd=os.getcwd())
    except KeyboardInterrupt:
        print("\n[DASHBOARD] Shutting down...")

def main():
    print_banner()

    print("\n📋 Prerequisites Check:")
    print("-" * 60)

    required_packages = ['flask', 'matplotlib']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} NOT installed")
            missing_packages.append(package)

    if missing_packages:
        print(f"\n⚠️  Missing packages detected!")
        print(f"Please install them using:")
        print(f"pip install {' '.join(missing_packages)}")
        print("\nOr install all dependencies:")
        print("pip install flask matplotlib")
        sys.exit(1)

    print("\n✅ All prerequisites satisfied!\n")
    print("=" * 60)

    server_thread = Thread(target=run_server, daemon=True)
    server_thread.start()

    time.sleep(3)

    dashboard_thread = Thread(target=run_dashboard, daemon=True)
    dashboard_thread.start()

    print("\n" + "=" * 60)
    print("🚀 ALL SYSTEMS OPERATIONAL")
    print("=" * 60)
    print("\n📍 Access Points:")
    print("   Web Server:  http://localhost:8080")
    print("   Dashboard:   http://localhost:5000")
    print("\n💡 Usage:")
    print("   1. Open http://localhost:5000 in your browser")
    print("   2. Click 'Start Auto Test' to run 100 concurrent requests")
    print("   3. Watch real-time metrics and graphs update")
    print("\n⚠️  Press Ctrl+C to stop all services")
    print("=" * 60 + "\n")

    try:
        server_thread.join()
        dashboard_thread.join()
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down all services...")
        print("=" * 60)
        print("✅ Server stopped")
        print("✅ Dashboard stopped")
        print("\nThank you for using Multi-Threaded Web Server!")
        print("=" * 60 + "\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
