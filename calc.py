import os
import re

def process(experiment_folder):
    folder_pattern = re.compile(r'run(\d+)')
    total_tx_packets, total_rx_packets, total_mean_delay, flow_count = 0, 0, 0, 0

    for folder_name in os.listdir(experiment_folder):
        folder_path = os.path.join(experiment_folder, folder_name)
        if not os.path.isdir(folder_path) and not folder_pattern.match(folder_name):
            return

        log_file_path = os.path.join(folder_path, 'log.txt')
        if not os.path.exists(log_file_path):
            return 

        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()
            tx_packets = sum(map(int, re.findall(r'Tx Packets: (\d+)', log_content)))
            rx_packets = sum(map(int, re.findall(r'Rx Packets: (\d+)', log_content)))
            mean_delay_match = re.search(r' Mean flow delay:\s+([\d.]+)', log_content)
            
            if mean_delay_match:
                mean_delay = float(mean_delay_match.group(1))
                total_tx_packets += tx_packets
                total_rx_packets += rx_packets
                total_mean_delay += mean_delay * (rx_packets / tx_packets)
                flow_count += 1

    if flow_count > 0:
        avg_tx_packets = total_tx_packets / flow_count
        avg_rx_packets = total_rx_packets / flow_count
        avg_mean_delay = total_mean_delay / flow_count
        reached_amount = total_rx_packets / total_tx_packets
        
        print(f"Deney: {experiment_folder}")
        print(f"Ortalama Tx Paket Sayısı: {avg_tx_packets}")
        print(f"Ortalama Rx Paket Sayısı: {avg_rx_packets}")
        print(f"Ortalama Gecikme: {avg_mean_delay} ms")
        print(f"PDR: {reached_amount}")
    else:
        print(f"Deney: {experiment_folder}")
        print("Hiç geçerli log dosyası bulunamadı.")

    return


experiment_folders = [
        './experiments/Test_20_2/', 
        './experiments/Test_20_5/', 
        './experiments/Test_60_5/', 
        './experiments/Test_20_10/'
    ]

for experiment_folder in experiment_folders:
    process(experiment_folder)
