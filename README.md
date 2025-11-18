# 🌐 Multi-Threaded Client-Based Web Server with Real-Time Dashboard

A comprehensive Python-based web server demonstrating advanced Operating Systems concepts including multi-threading, concurrency, resource sharing, and real-time system monitoring. Features an interactive dashboard with automated load testing capabilities.

![Project Banner](https://images.pexels.com/photos/1181671/pexels-photo-1181671.jpeg?auto=compress&cs=tinysrgb&w=1200)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [OS Concepts Demonstrated](#os-concepts-demonstrated)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dashboard Features](#dashboard-features)
- [API Endpoints](#api-endpoints)
- [Performance Testing](#performance-testing)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)

## 🎯 Overview

This project implements a production-ready, multi-threaded web server that handles multiple concurrent clients using a thread pool architecture. It includes a real-time interactive dashboard built with Flask, TailwindCSS, and Chart.js that visualizes server performance and allows automated load testing with a single click.

### Key Highlights

- **Multi-threaded Architecture**: Efficient handling of concurrent requests using a thread pool
- **Real-Time Monitoring**: Live dashboard updating every second with server metrics
- **Automated Load Testing**: One-click testing with 100 concurrent client requests
- **Smart Caching**: In-memory file caching for improved performance
- **Session Management**: Cookie-based unique session tracking
- **Thread-Safe Operations**: Proper synchronization for shared resources
- **Performance Visualization**: Real-time graphs and historical performance reports

## ✨ Features

### 🧠 Web Server (`server/`)

- **TCP Socket Server**: Low-level socket programming with Python's `socket` module
- **Thread Pool**: Fixed worker threads for efficient resource management
- **Static File Serving**: Serves HTML files with proper HTTP responses
- **404 Handling**: Graceful error handling for missing resources
- **Thread-Safe Metrics**: Shared dictionary with lock-based synchronization
- **Request Logging**: Comprehensive logging to `logs/server.log`
- **In-Memory Caching**: Stores recently requested files for faster response
- **Cookie Management**: Assigns unique session IDs to each client

### ⚡ Client Simulator (`client/`)

- **Concurrent Load Testing**: Sends 100+ simultaneous requests
- **Multi-threaded Clients**: Each client runs in its own thread
- **Performance Metrics**: Tracks response times and success rates
- **Programmable API**: Exposable `run_load_test()` function

### 🎨 Dashboard (`dashboard/`)

**Backend (Flask)**:
- `/` - Dashboard homepage
- `/metrics` - JSON metrics endpoint (updates every second)
- `/start_test` - Triggers automated 100-client load test
- `/toggle_cache` - Enable/disable caching dynamically
- `/test_status` - Check if load test is running

**Frontend**:
- Modern, responsive design with TailwindCSS
- Real-time updating metrics cards
- Live performance graphs using Chart.js
- Recent requests table with color-coded status
- Interactive cards with hover effects
- One-click automated load testing

### 📊 Performance Reports (`reports/`)

- JSON-based result storage
- Matplotlib graphs with dark theme
- Historical performance tracking
- Summary statistics generation

## 🧩 OS Concepts Demonstrated

This project showcases core Operating Systems principles:

| Concept | Implementation |
|---------|---------------|
| **Concurrency** | Multiple threads handling simultaneous client requests |
| **Synchronization** | Lock-based thread-safe access to shared metrics dictionary |
| **Resource Management** | Thread pool limiting concurrent workers to prevent resource exhaustion |
| **I/O Operations** | Socket programming for network communication, file system operations |
| **Process Communication** | Inter-process data sharing via TCP sockets |
| **Scheduling** | Operating system thread scheduling and context switching |
| **Deadlock Prevention** | Proper lock acquisition/release patterns |

## 🛠️ Technology Stack

- **Python 3.8+** - Core language
- **Socket** - Network programming
- **Threading & Queue** - Concurrency primitives
- **Flask** - Dashboard web framework
- **TailwindCSS** - Modern utility-first CSS
- **Chart.js** - Interactive data visualization
- **Matplotlib** - Performance report generation
- **JSON** - Data serialization
- **Logging** - Application logging

## 📁 Project Structure

```
project/
├── server/
│   ├── server.py              # Main web server implementation
│   ├── threadpool.py          # Thread pool manager
│   ├── logger_config.py       # Logging configuration
│   └── static/
│       ├── index.html         # Homepage
│       └── about.html         # About page
├── client/
│   └── client_simulator.py   # Load testing client
├── dashboard/
│   ├── dashboard.py           # Flask backend
│   └── templates/
│       └── index.html         # Dashboard frontend
├── reports/
│   ├── performance_report.py  # Report generation
│   ├── test_results.json      # Historical results
│   └── performance_graph.png  # Generated graphs
├── logs/
│   └── server.log             # Server logs
├── run_all.py                 # Orchestrator script
└── README.md                  # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Clone/Download the Project

```bash
cd project/
```

### Step 2: Install Dependencies

```bash
pip install flask matplotlib
```

### Step 3: Verify Installation

```bash
python3 run_all.py
```

This will automatically:
1. Check for required packages
2. Start the web server on port 8080
3. Start the dashboard on port 5000

## 💻 Usage

### Quick Start (Recommended)

Run everything with one command:

```bash
python3 run_all.py
```

Then open your browser to:
- **Dashboard**: http://localhost:5000
- **Web Server**: http://localhost:8080

### Manual Start

**Terminal 1 - Web Server:**
```bash
python3 -m server.server
```

**Terminal 2 - Dashboard:**
```bash
python3 -m dashboard.dashboard
```

**Terminal 3 - Load Test (Optional):**
```bash
python3 -m client.client_simulator
```

### Using the Dashboard

1. **Open Dashboard**: Navigate to http://localhost:5000
2. **View Metrics**: See real-time active clients, total requests, response times
3. **Start Auto Test**: Click the blue "Start Test" card to launch 100 concurrent requests
4. **Watch Live Updates**: Observe metrics spike and graphs update in real-time
5. **Toggle Cache**: Click the orange "Caching" card to enable/disable caching
6. **Review Logs**: Scroll down to see the 10 most recent requests

## 🎨 Dashboard Features

### Interactive Cards

| Card | Function | Details |
|------|----------|---------|
| 🧠 Start Test | Trigger load test | Launches 100 concurrent client requests |
| 📊 Live Metrics | Active clients | Shows current active connections |
| 💾 Caching | Toggle cache | Enable/disable in-memory file caching |
| ⚡ Avg Response | Response time | Average response time in milliseconds |
| 🍪 Cookies | Session tracking | Number of unique sessions |
| 🧵 Thread Pool | Worker threads | Thread pool size and queue status |

### Real-Time Graph

- **X-Axis**: Time (updates every second)
- **Y-Axis (Left)**: Active Clients (green line)
- **Y-Axis (Right)**: Total Requests (blue line)
- **Max Data Points**: 30 seconds of history

### Recent Requests Table

Displays last 10 requests with:
- Client IP address
- Requested path
- Response time (ms)
- HTTP status code (color-coded)

## 🔌 API Endpoints

### Dashboard Backend

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard homepage |
| `/metrics` | GET | JSON metrics (real-time) |
| `/start_test` | GET | Trigger 100-client load test |
| `/toggle_cache` | GET | Enable/disable caching |
| `/test_status` | GET | Check if test is running |

### Example Response: `/metrics`

```json
{
  "active_clients": 5,
  "total_requests": 1523,
  "average_response_time": 0.0234,
  "recent_requests": [...],
  "cache_enabled": true,
  "cache_hits": 890,
  "cache_misses": 633,
  "unique_sessions": 12,
  "thread_pool_size": 10,
  "queue_size": 0
}
```

## 📈 Performance Testing

### Automated Testing

Click "Start Test" in the dashboard to automatically:
1. Spawn 100 client threads
2. Send concurrent GET requests to the server
3. Measure response times
4. Update dashboard metrics in real-time
5. Display results in console

### Manual Testing

```bash
python3 -m client.client_simulator
```

### Generate Performance Report

```bash
python3 -m reports.performance_report
```

This creates:
- `reports/test_results.json` - Historical data
- `reports/performance_graph.png` - Visual performance graph

## 📸 Screenshots

### Dashboard Overview

![Dashboard Preview](https://images.pexels.com/photos/577585/pexels-photo-577585.jpeg?auto=compress&cs=tinysrgb&w=1200)

*Real-time dashboard showing live metrics, graphs, and recent requests*

### Performance Graph

![Performance Graph](https://images.pexels.com/photos/669610/pexels-photo-669610.jpeg?auto=compress&cs=tinysrgb&w=1200)

*Historical performance visualization with response times and success rates*

### Load Testing in Action

![Load Test](https://images.pexels.com/photos/3861969/pexels-photo-3861969.jpeg?auto=compress&cs=tinysrgb&w=1200)

*100 concurrent clients hitting the server - watch metrics spike!*

## 🔮 Future Improvements

### Security Enhancements
- [ ] HTTPS/TLS support with SSL certificates
- [ ] Authentication and authorization middleware
- [ ] Rate limiting per IP address
- [ ] Input validation and sanitization

### Performance Optimizations
- [ ] Async I/O with asyncio or aiohttp
- [ ] HTTP/2 support
- [ ] Connection pooling
- [ ] Response compression (gzip)

### Scalability
- [ ] Load balancing across multiple server instances
- [ ] Distributed caching (Redis)
- [ ] Horizontal scaling support
- [ ] Database integration for persistent sessions

### Monitoring
- [ ] Prometheus metrics export
- [ ] Grafana dashboard integration
- [ ] Email/Slack alerts for anomalies
- [ ] Detailed error tracking

### Features
- [ ] WebSocket support for real-time bidirectional communication
- [ ] RESTful API with multiple routes
- [ ] File upload/download capabilities
- [ ] Server-Sent Events (SSE) for live updates

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Add unit tests for thread pool
- Implement HTTPS support
- Create Docker containerization
- Add configuration file support
- Improve error handling

## 📄 License

This project is created for educational purposes to demonstrate Operating Systems concepts.

## 👨‍💻 Author

Created as a comprehensive demonstration of:
- Multi-threaded programming
- Socket programming
- Web server architecture
- Real-time data visualization
- OS concepts in practice

---

## 🎓 Learning Outcomes

By studying and running this project, you will understand:

1. **How web servers handle concurrent connections** using thread pools
2. **Thread synchronization** with locks to prevent race conditions
3. **Socket programming** for network communication
4. **Real-time data visualization** with modern web technologies
5. **Performance testing** and metrics collection
6. **Resource management** in multi-threaded applications

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Kill process on port 8080
lsof -ti:8080 | xargs kill -9

# Kill process on port 5000
lsof -ti:5000 | xargs kill -9
```

### Import Errors

Make sure you're running from the project root directory:
```bash
cd /path/to/project
python3 run_all.py
```

### Missing Dependencies

```bash
pip install --upgrade flask matplotlib
```

## 📚 References

- [Python Socket Programming](https://docs.python.org/3/library/socket.html)
- [Python Threading](https://docs.python.org/3/library/threading.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Chart.js](https://www.chartjs.org/)
- [TailwindCSS](https://tailwindcss.com/)

---

**⚡ Ready to see it in action? Run `python3 run_all.py` and open http://localhost:5000!**
