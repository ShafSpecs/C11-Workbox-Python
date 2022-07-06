import sys
import time

print("Loading:")

# animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
             "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
  time.sleep(0.2)
  sys.stdout.write("\r" + animation[i % len(animation)])
  sys.stdout.flush()

print("\n")

# Another one


def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.09)
  
  print()


# to use it:

sp("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁")


# Another one
def sc():
  jk = 0.09
  time.sleep(jk)
  
  
def loading7():
  for i in range(5):
    print("=")
    sc()
    print("==")
    sc()
    print("===")
    sc()
    print("====")
    sc()
    print("=====")
    sc()
    print("======")
    sc()
    print("=======")
    sc()
    print("========")
    sc()
    print("=========")
    sc()
    print("===========")
    sc()
    time.sleep(1)