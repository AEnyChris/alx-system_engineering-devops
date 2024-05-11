#!/usr/bin/env ruby
#pattern = ARGV[0].scan(/from:(.\w+)|to:(.\w+)|flags:([0-9:-]+)/)

pattern = ARGV[0].scan(/\[from:(.*?)\]|\[to:(.*?)\]|\[flags:(.*?)\]/)
array = [pattern[0].compact,pattern[1].compact,pattern[2].compact]
data = array.join(",")

puts data
