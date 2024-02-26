#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
    
  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    return self.value.count(". ") + self.value.count("? ") + self.value.count("! ") + (1 
                                                                                       if self.value.endswith(".")
                                                                                        or self.value.endswith("?")
                                                                                        or self.value.endswith("!")
                                                                                        else 0)
