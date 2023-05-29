# paint calculator

test_h = int(input("Enter height of the wall: "))
test_w = int(input("Enter width of the wall: "))
coverage = 5


def paint_calc(height, width, cover):
  cans_req = round((height * width) / cover)
  print(f"You will need {cans_req} of paint")


paint_calc(height=test_h, width=test_w, cover=coverage)
