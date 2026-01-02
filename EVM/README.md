# EVM (Electronic Voting Machine)

A Python-based electronic voting system with multiple components for managing candidates, polling booths, and vote tallying.

## Project Structure

- **Control_Unit.py** - Main control system for the voting machine
- **Polling_booth.py** - Polling booth interface and vote casting
- **result.py** - Vote counting and result generation
- **candidates.csv** - List of candidates
- **votes.json** - Vote data storage
- **final_results.json** - Final election results
- **communicator.txt** - Communication log

## Features

- Candidate management
- Secure vote casting at polling booths
- Vote aggregation and result calculation
- Result storage in JSON format

## Usage

1. Set up candidates in `candidates.csv`
2. Run `Control_Unit.py` to initialize the system
3. Use `Polling_booth.py` for vote casting
4. Execute `result.py` to generate results

## Files

- `votes.json` - Stores individual votes
- `final_results.json` - Contains aggregated results
- `communicator.txt` - Logs system communications

AI assistance was used in the creation of this project.