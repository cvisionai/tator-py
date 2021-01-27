# Extract tracks of interest

The python script `extract_tracks_of_interest.py` gathers a set of states, filters them based on
their intersection with a given region of interest, and downloads the associated localization
graphics of the filtered states.


## Usage

```
usage: extract_tracks_of_interest.py [-h] [--host HOST] [--token TOKEN] [--project PROJECT]
                                     [--state-type STATE_TYPE] [--state-file STATE_FILE]
                                     [--tracks-file TRACKS_FILE] [--out-folder OUT_FOLDER] [--roi ROI]
                                     [--get-states | --filter-states]

Add attribute to existing type

optional arguments:
  -h, --help            show this help message and exit
  --host HOST
  --token TOKEN         Your API token.
  --project PROJECT     Unique project id
  --state-type STATE_TYPE
                        The type of state to consider
  --state-file STATE_FILE
                        The text file where the intermediate list of states will be stored or read from
  --tracks-file TRACKS_FILE
                        The text file where the intermediate list of filtered states will be stored or
                        read from
  --out-folder OUT_FOLDER
                        The folder where the localization graphics will be downloaded
  --roi ROI             The id of the localization that defines the region of interest
  --get-states          Stop processing after all states are retrieved
  --filter-states       Stop processing after states are filtered
```
