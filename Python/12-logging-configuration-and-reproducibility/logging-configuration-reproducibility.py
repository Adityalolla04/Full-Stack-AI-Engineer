"""
Logging, Configuration, and Reproducibility - Production-Ready Code

This module covers best practices for production Python code:
- Logging levels and handlers
- Configuration (basicConfig, config dicts)
- Random seed and reproducibility
- Environment variables
- Configuration files (.env, .yaml)
- Reproducible Python code
"""

import logging
import logging.config
import os
import random
import numpy as np
from datetime import datetime
from typing import Dict, Any

# ============================================================================
# 1. LOGGING LEVELS AND HANDLERS
# ============================================================================

print("\n" + "="*70)
print("1. LOGGING LEVELS AND HANDLERS")
print("="*70)

print("\n--- Logging Levels ---")
print("""
Logging Levels (lowest to highest severity):
- DEBUG (10): Detailed diagnostic information
- INFO (20): Confirmation that events are working
- WARNING (30): Warning about potential issues
- ERROR (40): Error occurred, something failed
- CRITICAL (50): Critical error, system may fail

Default level is WARNING, so DEBUG and INFO are not shown.
""")

print("\n--- Basic Logging Setup ---")

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

print("Demonstrating logging levels:")
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

print("\n--- Different Log Formats ---")

# Different format styles
formats = [
    '%(message)s',  # Simple
    '[%(levelname)s] %(message)s',  # With level
    '[%(levelname)s] %(name)s: %(message)s',  # With logger name
    '[%(levelname)s] %(asctime)s - %(name)s: %(message)s',  # Full
]

print("\nCommon format options:")
print("  %(levelname)s - Log level (DEBUG, INFO, etc.)")
print("  %(name)s - Logger name")
print("  %(message)s - Log message")
print("  %(asctime)s - Timestamp")
print("  %(filename)s - Source filename")
print("  %(lineno)d - Line number")
print("  %(funcName)s - Function name")
print("  %(process)d - Process ID")
print("  %(thread)d - Thread ID")

print("\n--- File Handler ---")

# Create file handler
log_filename = "app.log"
file_handler = logging.FileHandler(log_filename)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s')
file_handler.setFormatter(formatter)

# Get root logger and add handler
file_logger = logging.getLogger("file_logger")
file_logger.addHandler(file_handler)
file_logger.setLevel(logging.DEBUG)

file_logger.info("This message goes to file")
file_logger.error("This error also goes to file")

# Read and display file content
with open(log_filename, 'r') as f:
    print(f"\nLog file content:\n{f.read()}")

# Cleanup
os.remove(log_filename)

print("\n--- Multiple Handlers ---")

def setup_logger_with_multiple_handlers():
    """Setup logger with console and file handlers"""
    logger = logging.getLogger("multi_handler")
    logger.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_fmt = logging.Formatter('[CONSOLE] %(levelname)s: %(message)s')
    console_handler.setFormatter(console_fmt)
    
    # File handler
    file_handler = logging.FileHandler("multi.log")
    file_handler.setLevel(logging.DEBUG)
    file_fmt = logging.Formatter('[FILE] %(levelname)s - %(asctime)s: %(message)s')
    file_handler.setFormatter(file_fmt)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

multi_logger = setup_logger_with_multiple_handlers()
print("Multi-handler logging (only WARNING+ to console, all to file):")
multi_logger.debug("Debug message")
multi_logger.info("Info message")
multi_logger.warning("Warning message")

if os.path.exists("multi.log"):
    os.remove("multi.log")

# ============================================================================
# 2. CONFIGURATION WITH DICTIONARIES
# ============================================================================

print("\n" + "="*70)
print("2. CONFIGURATION WITH DICTIONARIES")
print("="*70)

print("\n--- Dictionary-based Configuration ---")

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(levelname)s] %(asctime)s - %(name)s: %(message)s'
        },
        'detailed': {
            'format': '[%(levelname)s] %(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(funcName)s(): %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'filename': 'app.log'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
}

print("Dictionary-based logging configuration ready")
print("Can be used with: logging.config.dictConfig(LOGGING_CONFIG)")

# ============================================================================
# 3. RANDOM SEED AND REPRODUCIBILITY
# ============================================================================

print("\n" + "="*70)
print("3. RANDOM SEED AND REPRODUCIBILITY")
print("="*70)

print("\n--- Random Without Seed ---")
print("Without seed, results are different each run:")
print(f"Random 1: {random.random()}")
print(f"Random 2: {random.random()}")
print(f"Random 3: {random.random()}")

print("\n--- Random With Seed ---")
print("With seed, results are reproducible:")

# Set seed and generate numbers
random.seed(42)
print(f"With seed(42):")
print(f"  Random 1: {random.random()}")
print(f"  Random 2: {random.random()}")
print(f"  Random 3: {random.random()}")

# Set same seed - get same results
random.seed(42)
print(f"\nWith seed(42) again:")
print(f"  Random 1: {random.random()}")
print(f"  Random 2: {random.random()}")
print(f"  Random 3: {random.random()}")

print("\n--- NumPy Random Seed ---")

np.random.seed(42)
print(f"NumPy with seed(42):")
print(f"  Array 1: {np.random.rand(3)}")

np.random.seed(42)
print(f"NumPy with seed(42) again:")
print(f"  Array 1: {np.random.rand(3)}")

print("\n--- Complete Reproducibility Setup ---")

def set_reproducible_environment(seed: int = 42) -> None:
    """Set seed for all randomness sources"""
    random.seed(seed)
    np.random.seed(seed)
    # For TensorFlow: tf.random.set_seed(seed)
    # For PyTorch: torch.manual_seed(seed)

set_reproducible_environment(42)
print(f"Random: {random.random()}")
print(f"NumPy: {np.random.rand()}")

# ============================================================================
# 4. ENVIRONMENT VARIABLES
# ============================================================================

print("\n" + "="*70)
print("4. ENVIRONMENT VARIABLES")
print("="*70)

print("\n--- Reading Environment Variables ---")

# Set an environment variable for demonstration
os.environ['APP_ENV'] = 'development'
os.environ['DEBUG_MODE'] = 'true'

print("Reading environment variables:")
app_env = os.environ.get('APP_ENV', 'production')
debug_mode = os.environ.get('DEBUG_MODE', 'false')

print(f"APP_ENV: {app_env}")
print(f"DEBUG_MODE: {debug_mode}")
print(f"Non-existent var: {os.environ.get('MISSING_VAR', 'default_value')}")

print("\n--- Type Conversion ---")

def get_env_int(key: str, default: int) -> int:
    """Get integer environment variable"""
    return int(os.environ.get(key, default))

def get_env_bool(key: str, default: bool) -> bool:
    """Get boolean environment variable"""
    value = os.environ.get(key, str(default)).lower()
    return value in ('true', 'yes', '1', 'on')

os.environ['MAX_WORKERS'] = '4'
os.environ['ENABLE_CACHE'] = 'true'

max_workers = get_env_int('MAX_WORKERS', 2)
enable_cache = get_env_bool('ENABLE_CACHE', False)

print(f"MAX_WORKERS (int): {max_workers}")
print(f"ENABLE_CACHE (bool): {enable_cache}")

# ============================================================================
# 5. CONFIGURATION FILES
# ============================================================================

print("\n" + "="*70)
print("5. CONFIGURATION FILES")
print("="*70)

print("\n--- .env File Format ---")
print("""
.env file example:
  DATABASE_URL=postgresql://user:pass@localhost/db
  API_KEY=your_api_key_here
  DEBUG=True
  MAX_CONNECTIONS=10

Reading .env file:
  from dotenv import load_dotenv
  load_dotenv()  # Loads from .env
  
  db_url = os.environ.get('DATABASE_URL')
""")

print("\n--- YAML Configuration ---")
print("""
config.yaml example:
  app:
    name: MyApp
    version: 1.0
    debug: true
  
  database:
    host: localhost
    port: 5432
    name: mydb
  
  logging:
    level: INFO
    file: app.log

Reading YAML:
  import yaml
  
  with open('config.yaml') as f:
      config = yaml.safe_load(f)
  
  db_host = config['database']['host']
""")

print("\n--- INI Configuration ---")
print("""
config.ini example:
  [app]
  name = MyApp
  version = 1.0
  debug = true
  
  [database]
  host = localhost
  port = 5432
  name = mydb

Reading INI:
  import configparser
  
  config = configparser.ConfigParser()
  config.read('config.ini')
  
  db_host = config['database']['host']
  debug = config.getboolean('app', 'debug')
""")

# ============================================================================
# 6. REPRODUCIBLE PYTHON CODE
# ============================================================================

print("\n" + "="*70)
print("6. REPRODUCIBLE PYTHON CODE")
print("="*70)

print("""
Reproducibility Best Practices:

1. Set Seeds:
   - Set random seed at start of script
   - Document seed value
   - Use same seed for all runs

2. Document Dependencies:
   - requirements.txt with pinned versions
   - requirements.txt format:
     numpy==1.21.0
     pandas==1.3.0
     scikit-learn==0.24.2

3. Configuration Management:
   - Use config files instead of hardcoding
   - Document all configuration options
   - Use environment for sensitive data

4. Logging:
   - Log important decisions and values
   - Use consistent log format
   - Save logs for later analysis

5. Data Management:
   - Version control data files
   - Document data preprocessing steps
   - Save intermediate results

6. Version Control:
   - Commit code and config
   - Use tags for releases
   - Document code changes

7. Testing:
   - Write tests for critical functions
   - Test with same seed
   - Compare results with known outputs
""")

print("\n--- Reproducible Code Example ---")

class ReproducibleExperiment:
    """Template for reproducible ML experiments"""
    
    def __init__(self, seed: int = 42, config: Dict[str, Any] = None):
        self.seed = seed
        self.config = config or {}
        self.setup_reproducibility()
    
    def setup_reproducibility(self) -> None:
        """Setup reproducible environment"""
        random.seed(self.seed)
        np.random.seed(self.seed)
        
        # Log configuration
        logger = logging.getLogger(__name__)
        logger.info(f"Experiment seed: {self.seed}")
        logger.info(f"Configuration: {self.config}")
    
    def run(self) -> Dict[str, Any]:
        """Run experiment and return results"""
        logger = logging.getLogger(__name__)
        logger.info("Starting experiment")
        
        # Simulate experiment
        results = {
            'random_value': random.random(),
            'numpy_value': np.random.rand(),
            'timestamp': datetime.now().isoformat(),
            'seed': self.seed
        }
        
        logger.info(f"Results: {results}")
        return results

print("\nRunning reproducible experiment twice with same seed:")
exp1 = ReproducibleExperiment(seed=42)
results1 = exp1.run()

exp2 = ReproducibleExperiment(seed=42)
results2 = exp2.run()

print(f"Random values match: {results1['random_value'] == results2['random_value']}")
print(f"NumPy values match: {results1['numpy_value'] == results2['numpy_value']}")

# ============================================================================
# 7. BEST PRACTICES CHECKLIST
# ============================================================================

print("\n" + "="*70)
print("7. BEST PRACTICES CHECKLIST")
print("="*70)

print("""
Code Quality Checklist:

Configuration:
  ✓ Use environment variables for secrets
  ✓ Use config files for settings
  ✓ Never hardcode sensitive data
  ✓ Document all configuration options

Logging:
  ✓ Use appropriate log levels
  ✓ Include timestamps
  ✓ Include context (function name, line number)
  ✓ Log important events and errors
  ✓ Don't log sensitive data

Reproducibility:
  ✓ Set random seeds
  ✓ Pin dependency versions
  ✓ Document data preprocessing
  ✓ Save experiment configurations
  ✓ Use version control

Testing:
  ✓ Write unit tests
  ✓ Test edge cases
  ✓ Test error conditions
  ✓ Test with same seed for reproducibility
  ✓ Use continuous integration

Documentation:
  ✓ Write clear docstrings
  ✓ Document configuration options
  ✓ Document assumptions
  ✓ Document data formats
  ✓ Keep README updated

Code Organization:
  ✓ Use consistent file structure
  ✓ Separate concerns
  ✓ Use meaningful names
  ✓ Keep functions focused
  ✓ Use type hints
""")

# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES")
print("="*70)

print("""
1. Logging System:
   - Setup logger with console and file handlers
   - Create different log formats
   - Test all logging levels
   - Add context information to logs
   - Implement custom formatters

2. Configuration Management:
   - Create config dictionary
   - Setup environment variables
   - Load configuration from file
   - Validate configuration values
   - Handle missing configuration

3. Reproducibility:
   - Create reproducible experiment class
   - Set seeds for all random sources
   - Log all hyperparameters
   - Save and load experiment state
   - Verify reproducibility

4. Data Processing Pipeline:
   - Log each step with appropriate level
   - Use configuration for parameters
   - Set random seeds where needed
   - Save intermediate results
   - Document assumptions

5. Production-Ready Application:
   - Implement complete logging system
   - Use configuration file
   - Add command-line argument parsing
   - Implement error handling
   - Add status/progress logging
   - Create requirements.txt
   - Add type hints
   - Write unit tests
""")

print("\n" + "="*70)
print("Module completed successfully!")
print("="*70)
