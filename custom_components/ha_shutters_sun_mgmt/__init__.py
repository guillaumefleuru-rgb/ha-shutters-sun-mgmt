"""
Custom integration to deploy blueprints from this repository.
This integration copies blueprints to /config/blueprints/ on startup.
"""
import os
import shutil
from pathlib import Path
from homeassistant.core import HomeAssistant

DOMAIN = "ha_shutters_sun_mgmt"
BLUEPRINTS_DIR = Path(__file__).parent / "blueprints"
TARGET_DIR = Path("/config/blueprints/ha_shutters_sun_mgmt")


async def async_setup(hass: HomeAssistant, config):
    """Copy blueprints to /config/blueprints/ on startup."""
    await _copy_blueprints()
    return True


async def _copy_blueprints():
    """Copy all blueprints from custom_components to /config/blueprints/."""
    if not BLUEPRINTS_DIR.exists():
        return

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    for blueprint_file in BLUEPRINTS_DIR.glob("*.yaml"):
        target_path = TARGET_DIR / blueprint_file.name
        shutil.copy2(blueprint_file, target_path)

    # Also copy example.yaml if it exists
    example_file = BLUEPRINTS_DIR / "example.yaml"
    if example_file.exists():
        shutil.copy2(example_file, TARGET_DIR / "example.yaml")
