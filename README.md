# Prio

Prio is a small daemon to easily adjust both niceness and ionice values of processes automatically in the background.

It's created to be simple and easily configurable, might be further enhanced if there is demand for this service.

## Configuration

### Example config file

```json
{
  "update_freq": 30,
  "processes": [
    { "name": "example_file_name", "nice": 5, "ionice": { "c": 1 } }
  ]
}
```

_Should be located at "$home/.config/prio/config.json", it will automically create the folder and file if it doesn't exist upon launch._

### Main JSON object keys

| key         | data type | default value   | description                                          |
| ----------- | --------- | --------------- | ---------------------------------------------------- |
| update_freq | int       | 30 (Seconds)    | The frequency of checking running processes          |
| processes   | array     | example process | Contains list of processes with specified priorities |

### Process keys

| key    | data type | description                                                                                                                                        |
| ------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| name   | string    | Process name                                                                                                                                       |
| nice   | int       | Niceness value of process                                                                                                                          |
| ionice | obj       | Contains the scheduling class and the scheduling class data keys [More info about ionice](https://www.tutorialspoint.com/unix_commands/ionice.htm) |

### Ionice keys

| key | data type | description                                                           |
| --- | --------- | --------------------------------------------------------------------- |
| c   | int       | The scheduling class. 1 for real time, 2 for best-effort, 3 for idle. |
| n   | int       | The scheduling class data for real time and best-effort accepts 0-7   |
