# json_encode

This is a JSON obfuscator tool which replaces all the strings in a file with unicodeescape sequences, making it more difficult for a human reader to analyse it.

Example:

input: "name": "John"

output: "\u006e\u0061\u006d\u0065": "\u004a\u006f\u0068\u006e"
