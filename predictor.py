import subprocess

command = "docker stats --no-stream --format '{{.Name}}|{{.CPUPerc}}|{{.MemPerc}}'"
output = subprocess.getoutput(command)

for line in output.split("\n"):

    parts = line.split("|")

    if len(parts) == 3:

        name = parts[0]

        cpu = float(parts[1].replace("%", ""))
        mem = float(parts[2].replace("%", ""))

        score = cpu + mem

        if score > 120:
            risk = "HIGH FAILURE RISK"

        elif score > 60:
            risk = "MEDIUM RISK"

        else:
            risk = "LOW RISK"

        print(name, risk)
