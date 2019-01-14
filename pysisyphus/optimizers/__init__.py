import logging

__all__ = [
    "BFGS",
    "ConjugateGradient",
    "FIRE",
    "LBFGS",
    "QuickMin",
    "RFOptimizer",
    "SteepestDescent",
    "SciPyOptimizer",
]

logger = logging.getLogger("optimizer")
logger.setLevel(logging.DEBUG)
# delay = True prevents creation of empty logfiles
handler = logging.FileHandler("optimizer.log", mode="w", delay=True)
fmt_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(fmt_str)
handler.setFormatter(formatter)
logger.addHandler(handler)

logger = logging.getLogger("internal_coords")
logger.setLevel(logging.DEBUG)
# delay = True prevents creation of empty logfiles
handler = logging.FileHandler("internal_coords.log", mode="w", delay=True)
fmt_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(fmt_str)
handler.setFormatter(formatter)
logger.addHandler(handler)
