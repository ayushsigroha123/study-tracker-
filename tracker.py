import json
import time

FILE = "data.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {"sessions": [], "current": None}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def start_session(subject):
    data = load_data()

    if data["current"] is not None:
        print("Session already running!")
        return

    data["current"] = {
        "subject": subject,
        "start_time": time.time()
    }

    save_data(data)
    print(f"Started studying {subject}")

def stop_session():
    data = load_data()

    if data["current"] is None:
        print("No active session!")
        return

    end_time = time.time()
    session = data["current"]

    duration = end_time - session["start_time"]

    data["sessions"].append({
        "subject": session["subject"],
        "duration": duration
    })

    data["current"] = None
    save_data(data)

    print("Session ended!")

def show_summary():
    data = load_data()
    summary = {}

    for s in data["sessions"]:
        subject = s["subject"]
        duration = s["duration"] / 60  # minutes

        summary[subject] = summary.get(subject, 0) + duration

    print("\nStudy Summary (in minutes):")
    for sub, time_spent in summary.items():
        print(f"{sub}: {round(time_spent, 2)} mins")
