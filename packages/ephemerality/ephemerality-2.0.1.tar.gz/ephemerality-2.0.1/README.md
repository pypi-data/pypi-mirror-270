# Ephemerality metric
Ephemerality metrics are used to estimate the healthiness of various (online) activities, e.g. online discussions. 
It shows how 'ephemeral' these activities are, that is whether they are more or less uniform
over the period of interest or are only clustered around one or several short time periods.

Ephemerality formula is defined as follows:

$$
\varepsilon_\alpha^{core}=\left(1 - \frac1\alpha \cdot \frac{core\ length}{period\ length}\right)^+
$$

Essentially, **ephemerality** is a portion of the time period occupied by non‑core activity. The core activity can be 
defined in different ways and is parametrized by $\alpha$ — the minimal percentage of total activity it needs to 
contain. 

We defined 4 versions of computing these core periods: 

1. **Left $\alpha$-core**. Continuous time span from **the beginning of the period** to the point when $\alpha$% of 
total activity volume is contained within. Measures how fast activity becomes negligible after the start of the period.
Best suited for the types of activity with well-defined start time, e.g. reactions to posts, videos, news, etc.

2. **Right $\alpha$-core**. Continuous time span from **the end of the period** to the point when $\alpha$% of total 
activity volume is contained within. Measures how far in the past the meaningful past of activity spans. Best suited for
when you want to analyze activity within a specific time frame (for instance, up until the current date).

3. **Middle $\alpha$-core**. Continuous time span from **in the middle of the period** that contains $\alpha$% of total 
activity volume. Computed by cutting out at most (but as close to) $\frac{1-\alpha}2$% of activity volume from the 
beginning and the end of the period. Best suited for activities with no identifiable start and end times within the 
period of interest, e.g. discussions of certain topics onj social media.

4. **Sorted $\alpha$-core**. **Minimal number of time bins** that together contain $\alpha$% of total activity volume 
(left $\alpha$‑core for activity vectors sorted in descending order). Measures what portion of time is occupied by the
most prominent activity. Works well in combination with other cores to check whether all of the activity was centered 
around one or more short periods of time.

## Requirements
The code was tested to work with Python 3.10, Numpy 1.24.2, and pydantic 2.7.1, but is expected to also run with their
older versions.
FastAPI ^0.110.2 and uvicorn ^0.22.0 are also needed to run the ephemerality computation web-service. 
Matplotlib ^3.8.4 is needed for visualization of computed activity cores.

## How to run
Ephemerality package can be run as a standalone Python module, or used inside regular Python scripts.

### Standalone

The code can be run directly as a module `python3 -m ephemerality [args]`. There are two modes provided: a 
command line-based computation and a RESTful service. In case of the latter, there is an option to use a Docker 
container, either from Docker Hub (`hpaibsc/ephemerality:latest`) or built with the provided Dockerfile.

To run the computation from the command lineuse `cmd` argument:

```shell
python3 -m ephemerality cmd [activity] [-h] [-i INPUT_FILE] [-r] [-o OUTPUT_FILE.json] [-c CORE_TYPES] [-t THRESHOLD] [--plot]
```

In case of activity vector of moderate size, you can enter it either as a sequence of numbers directly, or as a 
comma/space separated string. Alternatively, you can save the activity vector(s) in a *.csv file (a vector per line) or 
*.json file. In case of the latter, please use the following format for each input (you can have a single dictionary or 
a list of ones):

```NumPy
JSON/Python input body format

Attributes
----------
input_sequence : Sequence[str | float | int]
    Input sequence of either activity over time bins, or timestamps to be aggregated into an activity vector.
input_type : Literal['activity', 'a', 'timestamps', 't', 'datetime', 'd'], default='a'
    Format of the input sequence.
threshold : float, default=.8
    Ratio of the activity considered core.
time_format : str, optional, default="%Y-%m-%dT%H:%M:%S.%fZ"
    If input type is datetime, specifies the datetime format used (refer to `strptime` format guidelines).
timezone : float, optional, default=0.
    If input type is datetime, specifies the offset in hours from the UTC time. Should be within [-24, +24] range.
range : tuple[str | float | int, str | float | int], optional
    If input type is timestamp or datetime, specifies the time range of the activity vector. 
    Defaults to (min, max) of the input timestamps.
granularity : Literal['week', 'day', 'hour'] or str, optional, default='day'
    If input type is timestamp or datetime, specifies the size of time bins when converting to activity vector.
    Can be specified as \'{}d\' or \'{}h\' (e.g. '2d' or '7.5h') for a custom time bin size in days or hours.
reference_name : str, optional
    Will be added to the output for easier matching between inputs and outputs (besides identical sorting).
```

The module uses uvicorn package to run a REST service. To start it use `api` argument:

```shell
python3 -m ephemerality api [-h] [--host HOST] [--port PORT] ...
```

Any additional arguments will be passed  as arguments to the uvicorn call.

The web-service initialized this way accepts GET requests of the following format:

```http
http://{url}/ephemerality/{api_version}/all?core_types=lmrs&include_input=False
```

* `api_version` is optional and is used for backward compatibility, it defaults to the latest API version.
* `core_types` is a string specifying the core types for which ephemerality needs to be computed. `l` for the left 
core, `m` for the middle core, `r` for the right core, `s` for the sorted core, or any combination of thereof. 
It defaults to all core types, `lmrs`.
* `include_input` is a boolean value specifying whether the input should be also included in the output for each 
computation.
* `input_data` is a body argument in JSON format. It should contain a list of JSON dictionaries of the input type 
specified above.

The output is in JSON format. It is a list of dictionaries, with one entry per each input:

```json
[
  {
    "input": ...,
    "output": {
      "eph_left_core": 1.0,
      "eph_middle_core": 1.0,
      "eph_right_core": 1.0,
      "eph_sorted_core": 1.0,
      "len_left_core": 0,
      "len_middle_core": 0,
      "len_right_core": 0,
      "len_sorted_core": 0
    }
  },
  ...
]
```

`input` value depends on the provided input parameters:
* If `include_input` was set to True, it will be a copy of the corresponding input dictionary.
* Otherwise it will be a string:
  - `reference_name` if it was provided;
  - or a zero-base counter number of the corresponding input.

#### Docker container

Finally, you can also use the docker container to run the aforementioned REST service. You can either get the image 
from Docker Hub:

```shell
docker pull hpaibsc/ephemerality:latest
```

Or build it from the source using the provided Dockerfile.

The web-service will be available at `http://0.0.0.0:8080` inside of the container.

### Python

Finally, it is possible to just import the ephemerality computation function from the module:

```Python
from ephemerality import compute_ephemerality

activity = [0., 0., 0., .2, .55, 0., .15, .1, 0., 0.]
threshold = 0.8
compute_ephemerality(activity, threshold)
```

Output:
```pycon
EphemeralitySet(
    eph_left_core=0.1250000000000001, 
    eph_middle_core=0.5, 
    eph_right_core=0.2500000000000001, 
    eph_sorted_core=0.625, 
    len_left_core=7, 
    len_middle_core=4, 
    len_right_core=6, 
    len_sorted_core=3)
```

`compute_ephemerality` function has the following signature:

```NumPy
Compute ephemerality values for given activity vector.

This function computes ephemerality for a numeric vector using all current definitions of actiovity cores.
Alpha (desired non-ephemeral core length) can be specified with ``threshold parameter. In case not all cores are 
needed, the required types can be specified in ``types``.

Parameters
----------
activity_vector : Sequence[float | int]
    A sequence of activity values. Time bins corresponding to each value is assumed to be of equal length. Does not
    need to be normalised.
threshold : float, default=0.8
    Desired non-ephemeral core length as fraction. Ephemerality is equal to 1.0 if the core length is at least ``threshold`` of
    the ``activity_vector`` length.
types : str, default='lmrs'
    Activity cores to be computed. A sequence of characters corresponding to core types.
    'l' for left core, 'm' for middle core, 'r' for right core, 's' for sorted core. Multiples of the same character
     will be ignored.
plot : bool, default=False
    Set to True to display the activity over time plot with core periods highlighted.

Returns
-------
EphemeralitySet
    Container for the computed core lengths and ephemerality values
```

EphemeralitySet is a simple container of the following format:

```NumPy
Container for ephemerality and core size values.

This class is a simple pydantic BaseModel used to store computed core lengths and corresponding ephemerality values
by core type. Values that were not computed default to None.

Attributes
----------
len_left_core : int, optional
    Length of the left core in time bins
len_middle_core : int, optional
    Length of the middle core in time bins
len_right_core : int, optional
    Length of the right core in time bins
len_sorted_core : int, optional
    Length of the sorted core in time bins

eph_left_core: float, optional
    Ephemerality value for the left core
eph_middle_core: float, optional
    Ephemerality value for the middle core
eph_right_core: float, optional
    Ephemerality value for the right core
eph_sorted_core: float, optional
    Ephemerality value for the sorted core
```

## Examples

Below are several examples of activity vectors and corresponding ephemerality computation results, demonstrating 
how this module can be used. All input activity vectors represent one year of activity with one day granularity. 
Threshold of $\alpha=0.8$ was used for all of the examples.

### Example 1

![Activity vector 1](images/example_1.png)

This vector represents a typical reaction activity to a post of any kind (e.g. text post, video, etc.). Most of the 
activity is concentrated at the beginning of the observation period and quickly goes down noise afterwards. Assuming 
we picked the start of the vector well (i.e. the time of posting), we will obtain the following ephemerality 
computation results:

![Results 1](images/results_1.png)

Here you can see that for the selected period ephemerality values for all cores except for the right core are high. 
Essentially, ephemerality value of 0.75 in this case signifies that about a quarter of the period corresponded to 
non-core activity.

The exception of the right core (which is computed from the right end of the activity vector) makes sense, as to 
accumulate the 80% of activity we need to go to almost the beginning of the vector. This can be interpreted as the 
fact, that looking into the past from the last (e.g. current) data this activity goes essentially full period deep. 
That is, this activity existed for quite a while in the past, and did not appear recently.

### Example 2

![Activity vector 2](images/example_2.png)

This activity vector has a few smaller but more gradual active periods and a big peak by its end. This produces the 
following results:

![Results 2](images/results_2.png)

Left and middle core ephemeralities in this case are pretty low, as it takes almost all the period to accumulate the 
80% of activity. The final peak was not enough to offset the previous, more gradual, activity.

In case of the right core, the last two peaks did contain the required amount of activity, so the ephemerality value 
is significant.

Finally, as the  majority of the activity is concentrated in the three peaks, the sorted ephemerality value is rather 
high (albeit not close to 1, thanks to the widths of the first two peaks).

### Example 3

![Activity vector 3](images/example_3.png)

In this example the vector contains 4 intense and abrupt peaks of activity among the general noise, a clear indicator 
of the forced activity injections. However, these peaks are spread throughout the observation period, with one being 
close to the beginning of the vector, and another one to its end.  

![Results 3](images/results_3.png)

Non-sorted cores in this case do cover most of the observation period due to the spread of the peaks. However, the 
sorted ephemerality value is very high, signifying that most of this activity were contained within a small number of 
actual days.

Here we should note that it is important to look at ephemerality for all the core types. From the current results we 
know that there are several well-spread short peaks of activity. If the middle core ephemerality was also high, that 
would have signified that there is only one peak or a close cluster of peaks in the middle of the period. If either 
the left or right core ephemerality were also high, that would have meant that this peak is closer to the left or the 
right end of the vector respectively.  

### Example 4

![Activity vector 4](images/example_4.png)

In the final example, the activity is locally chaotic but more or less uniform over the whole period. There is a small 
evolution of the trend here, but nothing unexpected.

![Results 4](images/results_4.png)

And this uniformity is confirmed by the resulting ephemerality values which are close to 0 (it would have been 0 in 
case of the same amount of activity each day). Here the slightly higher value of the sorted core ephemerality 
corresponds to the general variance of the activity: the lower the local fluctuations are, the closer to 0 it will be. 
