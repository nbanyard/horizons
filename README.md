# Horizon Generator

Program to generate elevations showing the horizon and lie of the land for any
point in Great Britian.
The program uses files which must be obtained from the Ordnance Survey OS
OpenData project.

The program is implemented in several different languages as a learning
exercise.

## Unit test

To run all tests: `make test`.

To run the Go tests: `make test_go`, other languages are similar.

### Implementation order

When creating a new implementation write one test at a time and get it working.
The following order is suggested.

* By northing generator walks due North.
* By northing generator walks due South.
* By northing generator takes one step East.
* By northing generator takes one step West.
* By northing generator walks due North East.
* By northing generator walks due South East.
* By northing generator walks 3-4-5 South Westish.
* By northing generator walks 3-4-5 North Westish.
