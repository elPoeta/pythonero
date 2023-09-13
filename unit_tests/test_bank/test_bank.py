from bank import value

def main():
  test_value_hello_without_spaces()
  test_value_hello_with_spaces()
  test_value_hello_with_name()
  test_value_how_doing()
  test_value_whats_happening()
  test_value_whats_up()

def test_value_hello_without_spaces():
  assert value("Hello".lower()) == 0

def test_value_hello_with_spaces():
  assert value(" Hello ".lower().strip()) == 0

def test_value_hello_with_name():
  assert value("Hello, Newman".lower()) == 0

def test_value_how_doing():
  assert value("How you doing?".lower()) == 20

def test_value_whats_happening():
  assert value("What's happening?".lower()) == 100

def test_value_whats_up():
  assert value("What's up?".lower()) == 100

if __name__ == "__main__":
  main()
  
# test_value_hello_without_spaces()
# test_value_hello_with_spaces()
# test_value_hello_with_name()
# test_value_how_doing()
# test_value_whats_happening()
# test_value_whats_up()