import toolneon
import random
import time

def generate(textSet, duration, direction):
  files = toolneon.generateGifPoster(
    textSet,
    './font/QingKe.ttf',
    100,
    (500, 500),
    duration=duration,
    direction=direction
  )
  if not files:
    return None
  random.seed(time.time())
  res = random.randint(0, 2)
  return f'../../backend/{files[res]}'

  