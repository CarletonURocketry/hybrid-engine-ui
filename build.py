import subprocess

subprocess.run(["pyside6-rcc", "main_window/ui/resources.qrc", "-o", "main_window/ui/rc_resources.py"])
subprocess.run(["pyside6-uic", "main_window/ui/form.ui", "--rc-prefix", "--from-imports", "-o", "main_window/ui/ui_form.py"])