def loading_bar(percentige):
    final_percentige = f'{percentige}%'
    percentige = percentige//10
    bar = ''
    for _ in range(percentige):
        bar += '%'
    for _ in range(10-percentige):
        bar += '.'
    if percentige == 10:
        print(f'{final_percentige} Complete!\n[{bar}]')
    if percentige < 10:
        print(f'{final_percentige} [{bar}]\nStill loading...')


percenige = int(input())
loading_bar(percenige)

