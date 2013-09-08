import turtle

t = turtle.Pen()

def spirale(t, segment, pourcent, angle, iterations):
  if iterations == 0: return
  t.forward(segment)
  t.left(angle)
  ajout_segment = (segment*(pourcent/100.0))
  spirale(t, segment+ajout_segment, pourcent, angle, iterations-1)

t.speed("fast")

spirale(t, 10, 15, 98, 30)

raw_input()