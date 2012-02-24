# encoding: UTF-8

# 그러니깐 C(40, 20) 임

def factorial n
  (1..n).reduce(1){|s,i| s * i}
end

def permutation n, r
  ((n-r+1)..n).reduce(1){|s, i| s*i}
end

puts permutation(40, 20) / factorial(20)