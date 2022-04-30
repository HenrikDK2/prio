# Prio

Prio is a small daemon to easily adjust both niceness and ionice values of processes automatically in the background.

It's created to be simple and easily configurable, might be further enhanced if there is demand for this service.

## Install service

Run the build script. Once it's build use your package manager to install the package. Example would be `yay -U package` or `sudo pacman -U package`

After installing the package remember to enable the service after making the neccesary configuration changes below.

Example: `systemctl enable prio.service`

## Configuration

Before starting the service you need to make a configuration file which is neccesary to change the priorities of the programs relevant for you.

### Example config file

```json
{
  "update_freq": 30,
  "processes": [
    { "name": "example_file_name", "nice": 5, "ionice": { "c": 1 } }
  ]
}
```

_The config have to be located at `/opt/prio/config.json`. Any changes requires restarting the service `systemctl restart prio.service` or rebooting._

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
