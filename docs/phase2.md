## Controller – Phase 2 Design

### Input
The controller receives a single URL as input.

### Responsibilities
- Call the Fetcher to retrieve raw HTML for the URL.
- Pass fetched content to the Parser to extract structured data.
- Pass extracted text to the Cleaner to normalize and clean it.
- Assemble the final document object containing:
  - URL
  - title
  - cleaned text
  - outgoing links

### Output
The controller returns a dictionary containing all structured and cleaned data related to the URL.

### Failure Handling
- If the webpage cannot be fetched, the controller handles the failure (skip, log, or retry).
- If parsing or cleaning fails, the controller skips the document safely.
- The controller ensures failures do not crash the entire pipeline.
  