# Hybrid Engine UI Usage Guide

## Basic Usage
The Hybrid Engine UI comes pre-configured with the correct multicast IP address and port used by the pad server. First, ensure that the laptop running the Hybrid Engine UI is on the same Wi-Fi network as the pad server. To connect to the multicast address, navigate to the "Connection" tab and click on the button labeled "Join multicast group". If the pad server is powered on, you should begin receiving telemetry data and can view it on the "Telemetry" tab

## Logging
Whenever the Hybrid Engine UI joins a mutlicast group, it immediately begins logging all received telemetry data in a timestamped CSV file. Timestamped sensor data can be found in the `data_csv` directory and timestamped updates of the system state (actuator flips, etc) can be found in `state_csv`. The default name for the CSV file that gets created whenever a multicast group is joined is simply the datetime stamp when it was created. The name for the current running CSV file can be changed by presseing the "Rename current CSV file" button. Clicking the "Start new CSV file" button will cause the application to create a new file and start writing to that one, this could be useful in creating sections during a single test. System logs that display system information are logged in the "Log" tab and can be exported using the "Export to file" button.

In addition to CSV logging, the raw UDP packets are also logged into .dump files. These are not human readable but can be replayed using the "Open raw data file" button

## PID Window
A separate window displaying a P&ID diagram with pressure readings in their respective locations of the current system can be opened by clicking "Open PID window" button. The P&ID diagram displayed in this window can be changed in the "Display Configuration" tab. The two available configurations are the "Cold flow" and "Static fire" diagrams.

## Display configurations
The "Display configuration" tab contains components that allow an operator to modify aspects of how data is displayed in the "Telemetry" tab. 
- The "Moving average previous value weight" number input changes the α value in the equation when displaying the current reading of sensor values. The equation is (last value * α) + (new value * (1 - α))
- The "PID diagram" radio buttons allow an operator to select which P&ID diagram to display in the PID window
- The "Valves open by default" section allows an operator to add a new valve ID which would be open in the system by default allowing for more accurate representation
- For each graph, separate options can be applied to each one. To remove a default open valve, click on an item in the list and press the same button
  - **Data display mode**: Can pick between displaying "Last X points" or "Point received in last X seconds", where X can be configured in the number input on the right
  - **Threshold markers**: Add permanent lines to each graph, helps for visualizing when sensor values exceed a certain point. Lines can be removed in same way as default valves
Display options can be saved by clicking the "Save default display configuration" button on the bottom and will be used on next startup