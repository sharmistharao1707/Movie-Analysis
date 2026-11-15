# Codebase Summary: Movie Rating and Analysis

## Overview

This script is an interactive, menu-driven Command-Line Interface (CLI) tool built in Python. It serves as an introductory data analysis and visualization utility that combines file I/O, DataFrame manipulation, and plotting into a continuous execution loop.

## Architecture & Workflow

1. **Initialization Phase:**
   * Uses Python's built-in `csv` module to create `movies.csv` and populate it with a header row and 4 initial records (*Inception*, *Titanic*, *Avengers*, *Interstellar*).
   * Loads the newly created CSV file into memory as a `pandas.DataFrame` (`df`).

2. **Interactive Event Loop (`while True`):**
   * Presents an 8-option text menu to the user.
   * Captures user selection via standard input (`input()`), casting it to an integer.

3. **Functional Modules (Menu Handlers):**
   * **View Operations (Options 1 & 2):** Outputs the raw DataFrame to the console (`print(df)`) or extracts dimensionality via `df.shape`.
   * **Data Mutation (Options 3 & 4):**
     * *Insertion:* Appends a new row at index `len(df)` using `.loc[]`.
     * *Deletion:* Filters the DataFrame using boolean indexing (`df[df["Movie_ID"] != mid]`).
     * Both operations immediately synchronize the updated DataFrame back to `movies.csv` using `df.to_csv(..., index=False)`.
   * **Visualization (Options 5, 6 & 7):** Leverages `matplotlib.pyplot` to render blocking GUI windows displaying line plots, bar charts, and a 5-bin histogram based on the `"Movie_Name"` and `"Rating"` columns.
   * **Termination (Option 8):** Breaks out of the `while` loop to cleanly exit the application.

## Technical Takeaways & Potential Improvements

* **Persistence Fix:** Wrapping the initial CSV creation block in an `os.path.exists("movies.csv")` check would allow user-added movies to persist across multiple runs of the program.
* **Error Handling:** Adding `try-except` blocks around `int()` and `float()` type casts would prevent the program from crashing on accidental invalid user inputs.
* **Index Management:** Using `df.loc[len(df)]` after deleting rows can occasionally overwrite existing indices if the DataFrame index is not reset (`df.reset_index(drop=True)`).
