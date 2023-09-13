from twttr import shorten
import pytest
 
def main():
  test_shorten()

def test_shorten():
  assert shorten("aeiouAEIOU50.cS") == "50.cS"


if __name__ == "__main__":
    main()