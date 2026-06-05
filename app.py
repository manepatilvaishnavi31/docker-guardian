from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():

    command = "docker stats --no-stream --format '{{.Name}}|{{.CPUPerc}}|{{.MemPerc}}'"
    output = subprocess.getoutput(command)

    containers = []

    for line in output.split("\n"):

        parts = line.split("|")

        if len(parts) == 3:

            name = parts[0]
            cpu = parts[1]
            mem = parts[2]

            cpu_val = float(cpu.replace("%", ""))
            mem_val = float(mem.replace("%", ""))

            if cpu_val > 80 or mem_val > 80:
                alert = "High Usage"
                risk = "High"

            elif cpu_val > 50 or mem_val > 50:
                alert = "Warning"
                risk = "Medium"

            else:
                alert = "Normal"
                risk = "Low"

            containers.append({
                "name": name,
                "cpu": cpu,
                "mem": mem,
                "alert": alert,
                "risk": risk
            })

    return render_template("dashboard.html", containers=containers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
