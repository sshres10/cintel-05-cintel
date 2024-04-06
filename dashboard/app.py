# From shiny, import just reactive and render
from shiny import reactive, render

# From shiny.express, import just ui
from shiny.express import ui

# Imports from Python Standard Library to simulate live data
import random
from datetime import datetime

# Import icons
from faicons import icon_svg

# Set up the reactive content

UPDATE_INTERVAL_SECS: int = 1  # Update interval in seconds

@reactive.calc()
def reactive_calc_combined():
    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Data generation logic
    temp = round(random.uniform(-18, -16), 1)  # Generate a random temperature
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp

    return {"temp": temp, "timestamp": timestamp}

# Define the UI layout - Page Options

ui.page_opts(title="PyShiny Express: Live Data (Basic)", fillable=True)

# Define the UI layout - Sidebar

with ui.sidebar(open="open"):
    ui.h2("Antarctic Explorer", class_="text-center")
    ui.p("A demonstration of real-time temperature readings in Antarctica.", class_="text-center")

# Define the UI layout - Main Section

ui.h2("Current Temperature")

@render.text
def display_temp():
    """Get the latest reading and return a temperature string."""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} C"

ui.p("warmer than usual")
icon_svg("sun")
ui.hr()

ui.h2("Current Date and Time")

@render.text
def display_time():
    """Get the latest reading and return a timestamp string."""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"