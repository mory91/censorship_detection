from ast import arg
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
    cmd = f"tshark -w {output_file}.raw > {output_file}"
    process = subprocess.Popen(cmd, shell=True)
    print(f"The process id is : {process.pid}")
    return process
    
def stop_tshark_in_backgorund(process_object):
    pid = process_object.pid
    process_object.kill()
    subprocess.run(f"kill {pid+1}", shell=True) # For local use added + 1 to kill the tshark process as well.
    

def make_requests(url_list):
    for url in url_list:
        response = requests.get("http://" + url)
        print(response.status_code)
    
def main():
    if len(sys.argv) < 3:
        print("USAGE: python3 tshark_runner.py <input_file> <output_file> ")
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    url_list = import_url_list(input_file_name)
    tshark_p = run_tshark_in_background(output_file_name)
    make_requests(url_list)
    stop_tshark_in_backgorund(tshark_p)

if __name__ == "__main__":
    main()