# Extract tracks of interest

The python script `extract_tracks_of_interest.py` gathers a set of states, filters them based on
their intersection with a given region of interest, and downloads the associated localization
graphics of the filtered states.


## Example Usage

```
$ python3 extract_tracks_of_interest.py \
    --host https://cloud.tator.io \
    --token <token> \
    --project 23 \
    --state-type 44 \
    --versions 80
01/27/2021 02:16:21 PM INFO:Found file state_list.txt, loading values
01/27/2021 02:16:21 PM INFO:Stored values not retrieved with the same parameters
01/27/2021 02:16:21 PM INFO:Retrieving values from server
01/27/2021 02:16:22 PM INFO:Values retireved!
01/27/2021 02:16:22 PM INFO:Storing retrieved values in state_list.txt
01/27/2021 02:16:22 PM INFO:Values stored!
01/27/2021 02:16:22 PM INFO:Total number of states: 996
01/27/2021 02:16:22 PM INFO:File track_list.txt not found or contains stale data
01/27/2021 02:16:22 PM INFO:Filtering values
100% [****************************************************************************************************]
01/27/2021 02:17:21 PM INFO:Values filtered!
01/27/2021 02:17:21 PM INFO:Storing calculated values in track_list.txt
01/27/2021 02:17:21 PM INFO:Values stored!
01/27/2021 02:17:21 PM INFO:Filtered number of states: 113
01/27/2021 02:17:21 PM INFO:Retrieving localization graphics from server...
100% [****************************************************************************************************]
01/27/2021 02:22:56 PM INFO:Localization graphics retrieved!
```
