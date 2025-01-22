import subprocess

subprocess.run(["pyside6-rcc", "main_window/ui/resources.qrc", "-o", "main_window/ui/rc_resources.py"])
subprocess.run(["pyside6-uic", "main_window/ui/form.ui", "--rc-prefix", "--from-imports", "-o", "main_window/ui/ui_form.py"])
subprocess.run(["pyside6-rcc", "main_window/ui/pid_window/resources.qrc", "-o", "main_window/ui/pid_window/rc_resources.py"])
subprocess.run(["pyside6-uic", "main_window/ui/pid_window/pid_window.ui", "--rc-prefix", "--from-imports", "-o", "main_window/ui/pid_window/ui_pid_window.py"])
