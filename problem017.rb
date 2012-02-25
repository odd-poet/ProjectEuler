#!/usr/bin/env ruby
# encoding: UTF-8
class Numeric 
  def to_words
    return "#{self}" if self > 1000
    words = []
    over100 = self.to_i / 100
    if over100 == 10 
      words << "one thousand"
    elsif over100 == 0
    else 
      words << WORD_20[over100]
      words << "hundred"
    end
    under100 = self.to_i % 100
    if under100 > 0 
      words << "and" unless words.empty?
      words << to_words_0_to_99(under100)
    end
    return words.join(" ")
  end
  
  private   
  def to_words_0_to_99 num
    raise if num < 0 or num > 99
    return WORD_20[num] if num <= 20
    x0 = num / 10
    x = num % 10
    words = WORD_TY[x0]
    words += " " + WORD_20[x] if x > 0 
    return words
  end
  
  WORD_20 = %w{
    zero one two three four five six seven eight nine ten
    eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty
  }
  WORD_TY = %w{
    zero ten twenty thirty forty fifty sixty seventy eighty ninety
  }
end

puts (1..1000).reduce(0) {|sum, num|  
  sum + num.to_words.gsub(/\s/,'').size
}