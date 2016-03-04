class HTMLGen:
  def tag(self, tagtype, text):
      return "<" + tagtype + ">" + text + "<//" + tagtype + ">"
  
  def a(self, text):
      return self.tag("a", text)
      
  def b(self, text):
      return self.tag("b", text)
      
  def p(self, text):
      return self.tag("p", text)

  def body(self, text):
      return self.tag("body", text)

  def div(self, text):
      return self.tag("div", text)

  def span(self, text):
      return self.tag("span", text)
      
  def title(self, text):
      return self.tag("title", text)
      
  def comment(self, text):
      return "<!--" + text + "-->"

htmlGen = HTMLGen()

print(htmlGen.a('test'))
print(htmlGen.comment('test'))