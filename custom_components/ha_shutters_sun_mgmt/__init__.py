"""
Custom component to serve blueprints for HACS compatibility.
This is a minimal integration to allow HACS to recognize the repository as valid.
"""

from homeassistant.core import HomeAssistant

DOMAIN = "ha_shutters_sun_mgmt"

async def async_setup(hass: HomeAssistant, config):
    """Minimal setup to make HACS recognize this as a valid repository."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    """Handle a config entry."""
    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    """Unload a config entry."""
    return True
