# recTrack

A simple tracker for Northeastern University's recreation website: [recreation.northeastern.edu](https://thechesirecat.github.io/recTrack/index.html)

## Overview

This project is a scraper/tracker powered by GitHub Actions. The code is designed to be minimal and lightweight, serving the purpose of tracking updates on the Northeastern recreation page.

## How It Works

- The project uses GitHub Actions to automate the scraping process.
- Data is periodically fetched from the [Northeastern recreation website](https://recreation.northeastern.edu).
- You can visit the tracker URL to see the updates: [recTrack](https://thechesirecat.github.io/recTrack/index.html).

## Why?

This is a personal project to practice using GitHub Actions and web scraping.

**Note:** I don't commit personal code nearly as much as I should. The frequency of GitHub Actions running on this project may make it seem like I am more active on GitHub than I actually am. My contributions reflect the automation of the tracker, not personal code commits.

## Issue with Cloning the Repo

Because the GitHub Action runs very frequently (often multiple times a day), the repository has accumulated a large number of commits. If you're trying to clone this repo, it may take a long time due to the size of the Git history from scraped data being committed over time.

### Suggested Solutions:
- **Shallow Clone:** If you just need the latest version of the code and don't need the full commit history, you can perform a shallow clone using the `--depth` option:
  ```bash
  git clone --depth 1 https://github.com/thechesirecat/recTrack.git
