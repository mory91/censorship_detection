from ast import arg
from tqdm import tqdm
import subprocess
import requests
import json
import sys

def import_url_list(input_file):
    host_list = []
    with open(input_file, "r") as file:
        host_list = json.load(file)
        print(host_list[0])
    return host_list

def run_tshark_in_background(output_file):
    cmd = f"tshark -w {output_file}"
    process = subprocess.Popen(cmd, shell=True)
    print(f"The process id is : {process.pid}")
    return process
    
def stop_tshark_in_backgorund(process_object):
    pid = process_object.pid
    process_object.kill()
    subprocess.run(f"kill {pid+1}", shell=True) # For local use added + 1 to kill the tshark process as well.
    

def make_requests(url_list):
    for url in tqdm(url_list, desc="Loading...."):
        try:
            if not url.startswith('http'):
                response = requests.get("https://" + url, timeout=5)
            else:
                response = requests.get(url, timeout=5)
            # print(response.status_code)
        except requests.exceptions.ConnectionError:
            print(f"{url} had connection error")
        except requests.exceptions.TooManyRedirects:
            print(f"{url} had too many redirects")
        except requests.exceptions.Timeout:
            print(f"{url} timeout")
        except Exception as e:
            print(e)

def main():
    if len(sys.argv) < 3:
        print("USAGE: python3 tshark_runner.py <input_file> <output_path> ")
    input_file_name = sys.argv[1]
    output_path_name = sys.argv[2]

    output_file_name = f"{output_path_name}/log.raw"

    url_list = import_url_list(input_file_name)
    tshark_p = run_tshark_in_background(output_file_name)
    make_requests(url_list)
    stop_tshark_in_backgorund(tshark_p)

if __name__ == "__main__":
    main()
