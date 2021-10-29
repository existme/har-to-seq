# har-to-seq
HAR to sequence diagram conversion tool

HAR (HTTP Archive format) is a file format used by many web browsers to export network traffic.

To analyze traffic on a web site, go to the developer tool, select network and save log. Then address the page(s).
Finally it's possible to export the traffic in a HAR file, that this project can analyze.

NOTE! This project is still under development.

## har-dump
Small utility program that dumps a HAR file to standard output
in a human readable way.

Syntax: har-dump <filename-of-har-file>
