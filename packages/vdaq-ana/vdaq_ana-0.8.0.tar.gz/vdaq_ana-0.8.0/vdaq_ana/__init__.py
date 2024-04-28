# VDaq analysis package.

__version__ = "0.8.0"


def analyze_data():
    """Analyze data."""
    from .cmmds.analyze_data import analyze_data
    analyze_data()

def show_data():
    """Analyze data."""
    from .cmmds.show_data import show_data
    show_data()

def getSpectrum():
    """Makes an spectrum."""
    from .cmmds.getSpectrum import getSpectrum
    getSpectrum()

def getFileInfo():
    """Makes an spectrum."""
    from .cmmds.getFileInfo import getFileInfo
    getFileInfo()

