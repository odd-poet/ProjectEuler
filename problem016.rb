# encoding: UTF-8
# http://projecteuler.net/problem=16

puts (2 ** 1000).to_s.each_char.reduce(0){|s, i| s += i.to_i}