# Extract tracks of interest

The python script `extract_graphics_and_sort.py` gathers a set of localizations, downloads their associated graphics, and sorts them into folders based on their `Species` attribute.


## Example Usage

```
$ python3 extract_graphics_and_sort.py \
    --host https://www.tatorapp.com \
    --token 548212020384e3510e1bd49dccd65e688aa4467f \
    --project 28 \
    --localization-type 61
01/28/2021 07:31:26 PM INFO:File localization_list.txt not found
01/28/2021 07:31:26 PM INFO:Retrieving values from server
01/28/2021 07:31:28 PM INFO:Values retireved!
01/28/2021 07:31:28 PM INFO:Storing retrieved values in localization_list.txt
01/28/2021 07:31:28 PM INFO:Values stored!
01/28/2021 07:31:28 PM INFO:Total number of localizations: 2281
01/28/2021 07:31:28 PM INFO:Retrieving localization graphics from server...
100% [****************************************************************************************************]
01/28/2021 07:31:28 PM INFO:Localization graphics retrieved!

```
