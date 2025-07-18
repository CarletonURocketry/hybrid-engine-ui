# hybrid-engine-ui

This repo contains the source code for the hybrid engine ground system UI

## Setup 

0. (Only required if working on UI) Follow steps on InSpace wiki to apply for Qt educational license and install Qt tools https://imaginary-fennel-36b.notion.site/PyQt-9af8dcdfb79d4bae98e3848670bb9994
1. Create a Python virtual environment `python -m venv <virtual environment name>`
2. Activate the virtual environment
   - **On Windows**: Run `.\<venv directory>\Scripts\Activate.ps1`. Note that you made need modify your machines execution policy if on Windows 11. To do so, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
   - **On Linux/Mac**: Run `source <venv directory>\bin\activate`
3. Install the required dependencies by running `pip install -r requirements.txt`
4. Build the UI either using [custom build steps in Qt Creator](https://github.com/CarletonURocketry/hybrid-engine-ui/pull/40) or running the build script `python build.py` 

## Running 
This application can be run either from the command line or in the Qt creator application. If running in Qt creator ensure that you have correctly added the [custom build steps](https://github.com/CarletonURocketry/hybrid-engine-ui/pull/40). To run this application from the command line run `python main.py`

## Project structure
Here's a quick breakdown of the files and directories of this project
- `main.py` - Entrypoint of project, creates and displays and instance of `MainWindow`. This is the only file that needs to be executed
- `build.py` - Python script that compiles generated `.ui` and `.qrc` files
- `packet_spec.py` - Contains implementation of the [hybrid communications packet specification](https://github.com/CarletonURocketry/hybrid-comm-format/) and related parsing functions
- `data_conversions.py` - Contains functions for converting data from sensor readings into their actual representative values
- `main_window` - Contains code for user `MainWindow` interface
  - `ui` - Contains generated and compiled UI code and images
    - `form.ui` - Generated XML-like file representation of UI
    - `ui_form.py` - Compiled Python code of `form.ui`
    - `pid_window.ui` - Generated XML-like file representation of the P&ID diagram window
    - `ui_pid_window.ui` - Compiled Python code of `pid_window.ui`
    - `resources.qrc` - Generated file containing information of images and other assets
    - `rc_resources.` - Compiled Python code of `resources.qrc`
  - `main_window.py` - Contains code for `MainWindow` class, primarily consists of imports from other files
  - `udp.py` - Contains all slots and handler code for UDP stuff
  - `data_handlers.py` - Contains all code for processing data
  - `recording_and_playback.py` - Contains all code for handling recording and playback of data
  - `logging.py` - Contains all code for handling logging
  - `config.py` - Contains code for loading the ui with preset values from `config.json`. Primarily for default threshold lines on graphs and multicast settings.
  - `serial.py` - Contains all slots and handler code for serial stuff
  - `csv_writer.py` - Contains a custom "buffered CSV writer" class that writes received parsed data into timestamped CSV files

## Deployment
In an effort to make the UI quickly accessible for all systems, PySide6-deploy is used to convert the Python code to C code and create an executable that is included in each new release. PySide6 uses the `pysidedeploy.spec` file that is included in this repo to compile the application into an executable. Note: this file requires specific information about where the project is on your machine as well as where the Python executable is. You can use `pysidedeploy.spec.template` and replace everything in <> brackets. 

Once you have filled out the template file and created a `pysidedeploy.spec` file, create a fresh executable with the current code, using `pyside6-deploy`. This process takes a few minutes and is only really necesarry when making a new release. Furthermore, at the cost of accessbility, the executable will take slightly longer to launch than the python application but should perform comparatively.
