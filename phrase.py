def generate_answers(phrase):
  def answer(letter):
    index = 0;
    hits = []
    while letter in phrase[index:]:
      f = phrase.find(letter, index)
      hits.append(f)
      index = f+1
    return hits
  return answer
