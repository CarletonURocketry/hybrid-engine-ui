# hybrid-engine-ui

This repo contains the source code for the hybrid engine ground system UI

## Setup 

0. (Only required if working on UI) Follow steps on InSpace wiki to apply for Qt educational license and install Qt tools https://imaginary-fennel-36b.notion.site/PyQt-9af8dcdfb79d4bae98e3848670bb9994
1. Create a Python virtual environment `python -m venv <virtual environment name>`
2. Activate the virtual environment `.\<venv directory>\Scripts\Activate.ps1`
3. Install the required dependencies by running `pip install -r requirements.txt`

## Running 
This application can be run either from the command line or in the Qt creator application. To run this application from the command line run `python widget.py`

## Project structure
Here's a quick breakdown of the files and directories of this project
- `logos` - Directory containing pngs of the CUInspace Avionics logo
- `TheColdHasFlown.xlsx` - Excel sheet containing propulsion cold flow data
- `form.ui` - An XML-like document that we can use with Qt Creator to manually edit or UI. Do not attempt to manually edit this file
- `hybrid-engine-ui.pyproject` and `hybrid-engine-ui.pyproject.user` - Files generated by Qt creator that contain metadata about the project. Do not attempt to manually edit these files
- `ui_form.py` - The "compiled" version of `form.ui`. This is the Python code that actually creates the user interface. This is created when running the project within Qt Creator but it can also be created by running `pyside6-uic form.ui -o ui_form.py`
- `widget.py` - The Pythong code that launches the UI and acts as the entry point to the application
