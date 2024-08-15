from exa_py import Exa
import os
import csv

# Initialize Exa clientt
exa = Exa(os.getenv("EXA_API_KEY"))

# Perform search and get contents in a single call
results = exa.search_and_contents(
    "Manufacturers specializing in high-precision machining for aerospace turbine components",
    use_autoprompt=True,
    num_results=1000,
    type="neural",
    category="company",
    summary=True
)

# Write results to CSV
csv_file = "aero-turbine-manufacturers.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["URL", "Published Date", "Summary"])

    # Write the data
    for result in results.results:
        writer.writerow([
            result.url,
            result.published_date,
            result.summary if hasattr(result, 'summary') else ""
        ])

print(f"Results written to {csv_file}")