# recTrack

A lightweight tracker for Northeastern University's recreation website: [recreation.northeastern.edu](https://thechesirecat.github.io/recTrack/index.html)

## Overview

recTrack is a GitHub Actions-based scraper designed to track updates on the Northeastern recreation page. The code is minimalistic, focusing solely on fetching and tracking changes to the site.

## How It Works

- GitHub Actions automates the scraping process on a regular schedule.
- Data is fetched periodically from the [Northeastern recreation website](https://recreation.northeastern.edu).
- Visit [recTrack](https://thechesirecat.github.io/recTrack/index.html) to view updates.

## Motivation

This project serves as a practice in using GitHub Actions and web scraping. Since the recreation website only displays current values without historical records, this tracker provides historical data for forecasting and other analytics.

**Note:** The frequent GitHub Actions updates might make it seem like I’m highly active on GitHub, but most contributions reflect the tracker’s automation rather than personal code commits.

## Cloning the Repository

The frequent GitHub Action runs have resulted in a large commit history, which can make cloning the repository slow.

### Solution:
- **Shallow Clone:** If you only need the latest version, perform a shallow clone to limit the download to recent commits:
  ```bash
  git clone --depth 1 https://github.com/thechesirecat/recTrack.git
  ```
