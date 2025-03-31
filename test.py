import os
import re
from dotenv import load_dotenv

load_dotenv()

from pollo.agents.draft.writer import generate_drafts_from_topics

# Define the base directory where topic folders are located
base_dir = "."  # Change this to your actual base directory path

# Define directories to exclude from processing
EXCLUDE_DIRS = [
    "01. Finacial Markets",
    "02. Arbitrage"
]

# Get all directories in the base directory
all_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

# Filter directories matching the pattern "[0-9+]. [Topic Name]"
topic_dirs = [d for d in all_dirs if re.match(r"^\d+\.\s+.+$", d)]

# Exclude directories that are in the EXCLUDE_DIRS list
topic_dirs = [d for d in topic_dirs if d not in EXCLUDE_DIRS]

# Define the perspectives for all topics
basic_perspective = "Focus on the foundational concepts of financial mathematics and quantitative finance, including financial markets, arbitrage principles, asset pricing, and risk assessment. Explore the theoretical foundations, properties, and basic applications of these concepts in financial analysis and portfolio management."
advanced_perspective = "Focus on advanced quantitative finance topics, including stochastic processes, Brownian motion, stochastic calculus, Itô's lemma, and derivatives pricing models like the Black-Scholes formula. Address computational methods for option pricing, hedging strategies, and applications in modern risk management frameworks."

# Process each topic directory
for directory in topic_dirs:
    print(f"Processing directory: {directory}")
    generate_drafts_from_topics(
        directory=directory,
        perspectives=[
            basic_perspective,
            advanced_perspective,
        ],
        json_per_perspective=1,
        branching_factor=1
    )
    
print(f"Processed {len(topic_dirs)} topic directories")