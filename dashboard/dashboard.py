# dashboard/dashboard.py
from flask import Flask, jsonify, render_template, request
import threading, sys, os, time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)

from server.server import start_internal_server, get_metrics, toggle_cache
from client.client_simulator import run_load_test, stop as stop_simulator

app = Flask(__name__, template_folder='templates')

_load_lock = threading.Lock()
_load_state = {"running": False}

# start server automatically
start_internal_server()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    try:
        return jsonify(get_metrics())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/toggle_cache')
def cache_toggle():
    try:
        state = toggle_cache()
        return jsonify({"cache_enabled": state})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/start_test', methods=['POST'])
def start_test():
    data = {}
    try:
        data = request.get_json(silent=True) or {}
    except Exception:
        data = {}

    mode = data.get("mode", "continuous")
    clients = int(data.get("clients", 50))
    path = data.get("path", "/index.html")
    rounds = int(data.get("rounds", 1))
    stagger_ms = int(data.get("stagger_ms", 5))

    with _load_lock:
        if _load_state["running"]:
            return jsonify({"status": "already_running"}), 400
        _load_state["running"] = True

    def bg():
        try:
            run_load_test(client_count=clients, server_host="127.0.0.1", server_port=8081,
                          path=path, rounds_per_thread=rounds, stagger_ms=stagger_ms, mode=mode)
        except Exception as e:
            print("[Dashboard] load error", e)
        finally:
            with _load_lock:
                _load_state["running"] = False

    threading.Thread(target=bg, daemon=True).start()
    return jsonify({"status": "started", "mode": mode, "clients": clients})

@app.route('/stop_test', methods=['POST'])
def stop_test():
    stop_simulator()
    with _load_lock:
        _load_state["running"] = False
    return jsonify({"status": "stopped"})

@app.route('/test_status')
def test_status():
    with _load_lock:
        return jsonify({"running": _load_state["running"]})

if __name__ == '__main__':
    print("[System] Dashboard running at http://localhost:5000 (internal server started)")
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
