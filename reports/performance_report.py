import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

REPORTS_DIR = 'reports'
RESULTS_FILE = os.path.join(REPORTS_DIR, 'test_results.json')
GRAPH_FILE = os.path.join(REPORTS_DIR, 'performance_graph.png')

def save_test_results(results):
    os.makedirs(REPORTS_DIR, exist_ok=True)

    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r') as f:
            all_results = json.load(f)
    else:
        all_results = []

    all_results.append(results)

    if len(all_results) > 50:
        all_results = all_results[-50:]

    with open(RESULTS_FILE, 'w') as f:
        json.dump(all_results, f, indent=2)

    print(f"Test results saved to {RESULTS_FILE}")

def generate_performance_graph():
    if not os.path.exists(RESULTS_FILE):
        print("No test results found. Run some tests first.")
        return

    with open(RESULTS_FILE, 'r') as f:
        all_results = json.load(f)

    if not all_results:
        print("No test results to plot.")
        return

    timestamps = [datetime.fromisoformat(r['timestamp']).strftime('%H:%M:%S') for r in all_results]
    total_requests = [r['total_requests'] for r in all_results]
    avg_response_times = [r['avg_response_time'] * 1000 for r in all_results]
    success_rates = [r['success_rate'] for r in all_results]

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
    fig.patch.set_facecolor('#1a1a1a')

    ax1.plot(timestamps, total_requests, marker='o', color='#3b82f6', linewidth=2, markersize=6)
    ax1.set_ylabel('Total Requests', fontsize=12, color='white')
    ax1.set_title('Load Test Performance Report', fontsize=16, fontweight='bold', color='white', pad=20)
    ax1.grid(True, alpha=0.3)
    ax1.set_facecolor('#2a2a2a')
    ax1.tick_params(colors='white')
    ax1.spines['bottom'].set_color('white')
    ax1.spines['top'].set_color('white')
    ax1.spines['left'].set_color('white')
    ax1.spines['right'].set_color('white')

    ax2.plot(timestamps, avg_response_times, marker='s', color='#10b981', linewidth=2, markersize=6)
    ax2.set_ylabel('Avg Response Time (ms)', fontsize=12, color='white')
    ax2.grid(True, alpha=0.3)
    ax2.set_facecolor('#2a2a2a')
    ax2.tick_params(colors='white')
    ax2.spines['bottom'].set_color('white')
    ax2.spines['top'].set_color('white')
    ax2.spines['left'].set_color('white')
    ax2.spines['right'].set_color('white')

    ax3.plot(timestamps, success_rates, marker='^', color='#f59e0b', linewidth=2, markersize=6)
    ax3.set_ylabel('Success Rate (%)', fontsize=12, color='white')
    ax3.set_xlabel('Test Time', fontsize=12, color='white')
    ax3.grid(True, alpha=0.3)
    ax3.set_facecolor('#2a2a2a')
    ax3.tick_params(colors='white')
    ax3.spines['bottom'].set_color('white')
    ax3.spines['top'].set_color('white')
    ax3.spines['left'].set_color('white')
    ax3.spines['right'].set_color('white')

    for ax in [ax1, ax2, ax3]:
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig(GRAPH_FILE, dpi=300, facecolor='#1a1a1a', edgecolor='none')
    print(f"Performance graph saved to {GRAPH_FILE}")

def print_summary_report():
    if not os.path.exists(RESULTS_FILE):
        print("No test results found.")
        return

    with open(RESULTS_FILE, 'r') as f:
        all_results = json.load(f)

    if not all_results:
        print("No test results available.")
        return

    print("\n" + "="*70)
    print("PERFORMANCE SUMMARY REPORT")
    print("="*70)

    total_tests = len(all_results)
    total_requests_all = sum(r['total_requests'] for r in all_results)
    avg_response_all = sum(r['avg_response_time'] for r in all_results) / total_tests
    avg_success_rate = sum(r['success_rate'] for r in all_results) / total_tests

    print(f"Total Tests Run:           {total_tests}")
    print(f"Total Requests Processed:  {total_requests_all:,}")
    print(f"Average Response Time:     {avg_response_all*1000:.2f}ms")
    print(f"Average Success Rate:      {avg_success_rate:.2f}%")

    print("\nRecent Test Results:")
    print("-" * 70)

    for i, result in enumerate(all_results[-5:], 1):
        print(f"\nTest {i}:")
        print(f"  Time:              {result['timestamp']}")
        print(f"  Total Requests:    {result['total_requests']}")
        print(f"  Successful:        {result['successful']}")
        print(f"  Failed:            {result['failed']}")
        print(f"  Success Rate:      {result['success_rate']:.2f}%")
        print(f"  Avg Response Time: {result['avg_response_time']*1000:.2f}ms")
        print(f"  Requests/Second:   {result['requests_per_second']:.2f}")

    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    generate_performance_graph()
    print_summary_report()
