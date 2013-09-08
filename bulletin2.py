from kidscode import ask

total = 0
notes = 0
fin = False
while not fin:
  notes = notes + 1
  note = ask("Note " + str(notes) + ": ")
  if note == "fin":
    fin = True
  else:
    total = total + int(note)

moyenne = total / notes

print "Total: " + str(total) + "/" + str(notes*20)
print "Moyenne: " + str(moyenne) + "/20"