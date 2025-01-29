python3 -m venv myenv
source myenv/bin/activate
pip install requests
python -c "import requests; print(requests.__version__)"