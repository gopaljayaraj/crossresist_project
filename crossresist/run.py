import os
import sys

base_path = os.path.dirname(os.getcwd())
sys.path.append(base_path)

from crossresist import app

if __name__ == '__main__':
	app.run(debug=True, port=9989)
