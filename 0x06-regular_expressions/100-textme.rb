#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <log_entry>"
  exit 1
end

log_entry = ARGV[0]

pattern = /\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/

if match_data = log_entry.match(pattern)
  sender = match_data[1]
  receiver = match_data[2]
  flags = match_data[3]

  puts "#{sender},#{receiver},#{flags}"
else
  puts "Error: Unable to extract information from the log entry."
end
